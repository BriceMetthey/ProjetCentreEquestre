Le projet Centre Equestre :horse:
=======

_Note : Projet à destination des Terminales NSI_

:warning: :construction: Le projet est en construction et soumis à d'importantes modifications. :construction: :warning:

:notebook: Documentation de référence 
-----------
- [x] [Le framework Flask](https://flask.palletsprojects.com/en/stable)
- [x] [La base de données sqlite](https://www.sqlite.org)
- [x] [Usage de sqlite3 avec Python](https://docs.python.org/3/library/sqlite3.html)
- [x] [Le module d'authentification Flask](https://flask-login.readthedocs.io/en/latest)
- [x] [Outils en ligne de commande pour la manipulation de la base de données](https://www.sqlite.org/cli.html)
- [x] [Outils graphique pour la manipulation de la base de données (sqlitebrowser) ](https://sqlitebrowser.org)



:computer: Instructions d'installation 
-----------

### Prérequis

Le système d'exploitation contient deux répertoires de base :
- `C:\Projets` _Codes sources des projets._
- `C:\Applis`  _Exécutables des applications tièrces (base de données etc...)._

### Récupération du code source

- Télécharger le code source du projet via le bouton Code -> Download ZIP
- Décompresser le projet
- Couper/coller le sous répertoire du projet ProjetCentreEquestre-main dans `C:\Projets`.
- Renommer le répertoire en `ProjetCentreEquestre`

### Créer un environnement virtuel sur votre PC

Un environnement virtuel permet de créer un groupe indépendant de bibliothèques Python, un pour chaque projet. Les packets installés pour un projet n'affecteront pas d'autres projets.

- Executer les lignes de commandes suivantes :

`cd C:\Projets\ProjetCentreEquestre`

L'execution de la ligne ci-dessous peut prendre du temps ... :watch:

`py -3 -m venv env_ProjetCentreEquestre`

- Activation de l'environnement :

`C:\Projets\ProjetCentreEquestre\env_ProjetCentreEquestre\Scripts\activate.bat`

- On obtient alors le prompt suivant :

`(env_ProjetCentreEquestre) C:\Projets\ProjetCentreEquestre>`
 
### Installation de Flask

`pip install Flask`

`pip install flask-login`

### Installation de la base de données

Aller sur : [https://www.sqlite.org/download.html](https://www.sqlite.org/download.html)

Aller dans la sous-section : Precompiled Binaries for Windows

Télécharger le fichier `sqlite-tools-win-x64-<version>.zip`

C'est un ensemble d'outils en ligne de commande pour la gestion des fichiers de base de données SQLite.

Le fichier est compressé. Donc le décompresser et le placer par exemple dans : `C:\Applis`

Ce qui permet d'avoir l'arborescence suivante :

```txt
C:\Applis\Sqlite
|_sqldiff.exe
|_sqlite3.exe
|_sqlite3_analyzer.exe
|_sqlite3_rsync.exe
```

:bicyclist: Execution 
-----------

### Création de la base de données
 
Cas d'usage :
- [x] Première utilisation
- [x] Réinitialisation complète de la base de données

`cd C:\Projets\ProjectCentreEquestre\bdd`

Ouvrez l'interface de ligne de commande SQLite :

`C:\Applis\Sqlite\sqlite3.exe`

Utilisez la commande .open pour créer et ouvrir une nouvelle base de données :

`.open centreEquestre.db`

Executer les commandes SQL du fichier `schema.sql` :

`.read schema.sql`

`.exit`

###  Execution du serveur web

`cd C:\Projets\ProjectCentreEquestre`

`C:\Projets\ProjectCentreEquestre\env_ProjetCentreEquestre\Scripts\activate.bat`

`flask --app app run --debug`

:floppy_disk: Procédure de sauvegarde des données 
-----------
La commande .dump dans SQLite permet de prendre un cliché de votre base de données.

`cd C:\Projets\ProjectCentreEquestre\bdd`

`C:\Applis\Sqlite\sqlite3.exe`

```txt
.open centreEquestre.db
.output backup.sql
.dump
.output stdout
```
