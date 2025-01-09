from django.urls import path
from . import views
from home.views import home_page, details_product, add_to_cart, cart_view, remove_from_cart


urlpatterns = [
    path('', home_page, name='home_page'),
    path('<int:id>/', details_product, name='details_product'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]
