# Création d'un environement virtuel avec python
python -m venv {nom-environement}

# Activé l'environement 
pour activé : source {nom-environement}/bin/activate (linux)
            : ./venv/Scripts/activate (windows)
pour deactivé

# Créer un fichier requirements
- Je remplis le fichier par les API.
- pip install -r requirements.txt
- pip freeze
- pip freeze > requirements.txt
Remarque:
- Tout projet django apres activation de l'environemnt va utilisé la version propre de l'environement lui meme.
- On peut ne pas créer le projet dans le meme dossier de l'environement

# Créer un projet django n'importe ou dans le disque dur 
- aller au dossier et taper : django-admin startproject {nom-du-projet}
- Accéder au dossier du projet.

# Regarder les modules disponible sur django
- python manage.py
# Lancer le serveur 
- python manage.py runserver


# Django
  Django(MVT) -> AutreFramework(MVC)
- Model -> Model
- View -> Controleur
- Template -> view

# Créer une App
- coupe le serveur Ctrl + C
- python manage.py startapp {nom-app} 

# Make Migrations Of Tables
- python manage.py showmagrations
- python manage.py makemigrations {app:exeple blog}
Une fois satisfait de la base de données je met ca :
- python manage.py migrate

# Sass:
pour généré un fichier

{chemin de l'executable qui se tronve dans .dart-sass/sass} 