Le projet Centre Equestre :horse:
=======



:notebook: Documentation de référence 
-----------

- [x] [La base de données sqlite](https://www.sqlite.org)
- [x] [Usage de sqlite3 avec Python](https://docs.python.org/3/library/sqlite3.html)
- [x] [Outils en ligne de commande pour la manipulation de la base de données](https://www.sqlite.org/cli.html)
- [x] [Outils graphique pour la manipulation de la base de données (sqlitebrowser) ](https://sqlitebrowser.org)



:computer: Instructions d'installation 
-----------


### Récupération du code source

- Télécharger le code source du projet via le bouton Code -> Download ZIP
- Décompresser le projet
- Couper/coller le sous répertoire du projet ProjetCentreEquestre-main dans `D:\Projets`.
- Renommer le répertoire en `ProjetCentreEquestre`



:bicyclist: Execution 
-----------


###  Execution de l'application

`cd D:\Projets\ProjetCentreEquestre\src`

`python main.py`


###  Execution des tests unitaires

`cd D:\Projets\ProjetCentreEquestre\test`

`python test_gestion_chevaux.py`


:floppy_disk: Procédure de sauvegarde des données 
-----------
La commande .dump dans SQLite permet de prendre un cliché de votre base de données.

`cd D:\Projets\ProjetCentreEquestre\bdd`

`D:\Applis\Sqlite\sqlite3.exe`

```txt
.open centreEquestre.db
.output backup.sql
.dump
.output stdout
```
