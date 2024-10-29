Le projet Centre Equestre :horse:
=======

_Note : Projet à destination des Terminales NSI_

:warning: :construction: Le projet est en construction. **Il n'est pas utilisable en l'état.** 

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

Le système d'exploitation à un répertoire de base : `C:\Projets`.

Lancer une invite de commandes.

Lancer les commandes suivantes :

`cd C:\`

`cd Projets`


### Créer un environnement virtuel sur votre PC

Un environnement virtuel permet de créer un groupe indépendant de bibliothèques Python, un pour chaque projet. Les packets installés pour un projet n'affecteront pas d'autres projets.

`mkdir ProjectCentreEquestre`

`cd ProjectCentreEquestre`

`py -3 -m venv env_ProjetCentreEquestre`

2) Activation de l'environnement

`C:\Projets\ProjectCentreEquestre\env_ProjetCentreEquestre\Scripts\activate.bat`

On obtient alors le prompt suivant :

`(env_ProjetCentreEquestre) C:\Projets\ProjectCentreEquestre>`
 
### Installation de Flask

`pip install Flask`

`pip install flask-login`

### Installation de la base de données

Aller sur : [https://www.sqlite.org/download.html](https://www.sqlite.org/download.html)

Aller dans la sous-section : Precompiled Binaries for Windows

Télécharger le fichier sqlite-tools-win-x64-<version>.zip

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
