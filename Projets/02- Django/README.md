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

# Postgres psql
## Demarer le service postgresql
1. sudo -s
2. service postgresql [start/stop/kill] OR sudo systemctl [start/stop] postgresql : démarrer le serveur
3. service postgresql status OR sudo systemctl status postgresql : vérifier le statut
## Connecter a postgresql
- sudo -u [superuser] psql -> connection avec un utilisateur
- psql -U [superuser] -d [database] -h [host] -> connection avec un utilisateur a une base de données.


## Afficher les utilisateur
- \du
## ajouter un utilisateur
- CREATE ROLE med063197 WITH LOGIN PASSWORD 'tharalina06';
## Afficher les roles d'un utilisateur
- SELECT rolname, rolsuper, rolcreaterole, rolcreatedb, rolcanlogin FROM pg_roles WHERE rolname = 'med063197';
## Ajouter un role
- ALTER ROLE [username] WITH [CREATEROLE, CREATEDB]
- ALTER USER med063197 CREATEDB; : ajouter des privilèges

## Donner a l'utilisateur med063197 tout les privileges sur toutes les tables
- GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO med063197;

## Afficher les bases de données
\list : pour lister tout les base de données qui sont dans l'ordianteur
## Creation d'une base de données
CREATE DATABASE [name_database];
## Connection en une base de données
\c [database]
## Afficher les table d'une base de données
\dt
## Affichier les champs d'une table
\d [tablename]


# Sass:
pour généré un fichier

{chemin de l'executable qui se tronve dans .dart-sass/sass} 