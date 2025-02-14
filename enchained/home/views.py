from django.shortcuts import render, get_object_or_404, redirect
from home.models import Product, Category
from django.contrib.auth.decorators import login_required, user_passes_test
from home.models import Product, Category
from home.forms import ProductForm


# Create your views here.

def home_page(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    if 'title' in request.GET and request.GET['title']:
        products = products.filter(title__icontains=request.GET['title'])

    if 'category' in request.GET and request.GET['category']:
        category = request.GET['category']
        products = products.filter(category__name=category)

    return render(request, 'home/home.html', {
        'products': products,
        'categories': categories,
    })

def details_product(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'home/details_product.html', {"product": product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})  

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'title': product.title,
            'price': product.price,
            'quantity': 1,
            'image': product.image.url if product.image else None,
        }

    request.session['cart'] = cart
    return redirect('cart_view')

def cart_view(request):
    cart = request.session.get('cart', {}) 
    total = sum(item['price'] * item['quantity'] for item in cart.values()) 
    return render(request, 'home/cart.html', {'cart': cart, 'total': total})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('cart_view')


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = ProductForm()
    return render(request, 'home/add_product.html', {'form': form})