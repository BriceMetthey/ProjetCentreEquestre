Le projet Centre Equestre :horse:
=======

_Note : Projet à destination des Terminales NSI_

:warning: :construction: Le projet est en construction. **Il n'est pas utilisable en l'état.** 

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

4) Mise en place de la base de données

Aller sur : [https://www.sqlite.org/download.html](https://www.sqlite.org/download.html)

Aller dans la sous-section : Precompiled Binaries for Windows

Télécharger le fichier sqlite-tools-win-x64-<version>.zip

C'est un ensemble d'outils en ligne de commande pour la gestion des fichiers de base de données SQLite.

Le fichier est compressé. Donc le décompresser et le placer par exemple dans : `C:\Applis`


Execution
-----------


Procédure de sauvegarde des données
-----------
