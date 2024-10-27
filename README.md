Le projet Centre Equestre :horse:
=======

_Note : Projet à destination des Terminales NSI_

:warning: :construction: Le projet est en construction. **Il n'est pas utilisable en l'état.** 

Documentation de référence
-----------

- [x] [sqlite3 avec Python](https://docs.python.org/3/library/sqlite3.html)
- [x] https://flask-login.readthedocs.io/en/latest/



Instructions d'installation
-----------

0) Prérequis

Le système d'exploitation à un répertoire de base : `C:\Projets`.

Lancer une invite de commandes.

Lancer les commandes suivantes :

`cd C:\`

`cd Projets`


2) Créer un environnement virtuel sur votre PC

Un environnement virtuel permet de créer un groupe indépendant de bibliothèques Python, un pour chaque projet. Les packets installés pour un projet n'affecteront pas d'autres projets.

`mkdir monProjectCentreEquestre`

`cd monProjectCentreEquestre`

`py -3 -m venv env_ProjetCentreEquestre`

2) Activation de l'environnement

`C:\Projets\monProjectCentreEquestre\env_ProjetCentreEquestre\Scripts\activate.bat`

On obtient alors le prompt suivant :

`(env_ProjetCentreEquestre) C:\Projets\monProjectCentreEquestre>`
 
3) Installation de Flask

`pip install Flask`
`pip install flask-login`

4) Mise en place de la base de données

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

Execution
-----------

Execution du serveur web :   `flask --app app run --debug`

Procédure de sauvegarde des données
-----------
