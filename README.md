## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

### Workflow CircleCI

Déploiement automatique à l'aide du pipeline CircleCI à chaque push du projet dans GitHub en suivant le wokflow suivant:

1. Récupération du code (checkout)
2. Installation des packages listés dans requirements.txt avec pip
3. Lancement des tests avec pytest
4. Vérification du linting avec flake8
5. Création du container avec l'image du projet dans le dépôt DockerHub
6. Déploiement web sous Heroku
7. Suivi des erreurs et des performances avec Sentry

### Configuration requise

Les comptes suivants sont nécessaires:

- GitHub
- CircleCI
- DockerHub
- Heroku
- Sentry

Il est utile d'installer en local les programmes suivants:

- Docker Desktop

### Guide de déploiement

### Étape1: DockerHub

- Se connecter à Docker
- Créer un dépôt (Create Repository)
- Renseigner le nom du dépôt: oc_lettings_site_build

### Étape2: Heroku

- Se connecter à Heroku
- Cliquer sur New\Create new app
- Renseigner le nom de l'application: lettings-project-heroku

### Étape3: Sentry

- Se connecter à Sentry
- Menu Projects\Create Project
- Choisir la plateforme: django
- Renseigner le nom du projet: python-django

### Étape4: CircleCI

- Se connecter à CircleCI avec son compte GitHub
- Menu Projects: rechercher le projet Python-OC-Lettings-FR
- Set Up Poject: choisir "if you already have.circleci/config.yml" et branche main

### Étape5: Récupérer l'image sur DockerHub et lancer le site en local

- Ouvrir Docker Desktop
- Récupérer l'image en local: `docker pull your_docker_login/oc_lettings_site_build:tag`
- Tag se trouve dans DockerHub
- Lister les images: `docker images`
- Lancer le container Docker avec le fichier des variables d'environnement locales: `docker compose up --build`
- Tester le site dans votre navigateur: `http://127.0.0.1:8000/`