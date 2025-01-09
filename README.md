E-commerce App

Description

Ce projet est une application d'e-commerce développée avec Django, permettant aux utilisateurs de naviguer, ajouter des produits à leur panier et finaliser leurs achats. L'application inclut un système d'authentification permettant aux utilisateurs de se connecter pour gérer leur panier et leurs commandes. Un formulaire d'ajout de produits est également disponible pour les administrateurs afin de mettre à jour l'inventaire. L'interface est simple et fonctionnelle, avec une gestion complète des produits et des paniers d'achat.

Fonctionnalités

Inscription et connexion des utilisateurs
Visualisation des produits disponibles à l'achat
Ajout, suppression et mise à jour des quantités de produits dans le panier
Gestion du panier et des commandes
Interface utilisateur simple et intuitive
Authentification sécurisée pour l'accès aux fonctionnalités du panier
Formulaire d'ajout de produits (réservé aux administrateurs)
Prérequis

Avant de pouvoir exécuter l'application, assure-toi d'avoir installé les éléments suivants :

Python 3.x
Django 3.x+
pip (pour la gestion des dépendances)
Installation

Clone ce repository :

git clone https://github.com/ton-utilisateur/ecommerce-app.git
Accède au répertoire du projet :
cd ecommerce-app
Crée un environnement virtuel :
python3 -m venv venv
Active l'environnement virtuel :
Sur Windows :
venv\Scripts\activate
Sur macOS/Linux :
source venv/bin/activate
Installe les dépendances :
pip install -r requirements.txt

Configuration

Configure les paramètres de la base de données dans settings.py. Par défaut, l'application utilise SQLite, mais tu peux configurer une autre base de données si nécessaire.
Applique les migrations de la base de données :
python manage.py migrate
Crée un superutilisateur pour accéder au panneau d'administration :
python manage.py createsuperuser
Lancer l'application

Démarre le serveur de développement :

python manage.py runserver
Ouvre ton navigateur et va sur http://127.0.0.1:8000 pour voir l'application en action.
Structure du projet

ecommerce-app/
│
├── ecommerce/
│ ├── migrations/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── forms.py
│ └── admin.py
│
├── templates/
│ └── home/
│ ├── cart.html
│ └── home.html
│
├── static/
│ └── home/
│ └── cart.css
│
├── manage.py
└── requirements.txt

Technologies utilisées

Django : Framework web Python pour développer l'application.
SQLite (par défaut) : Base de données relationnelle légère.
HTML/CSS : Pour la structure et le style de l'interface utilisateur.

Matteo Livrozet
Tom Julliat
License

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
