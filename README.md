# Restaurants en île de france
Ce projet a été développé dans le cadre du `4ème projet d'expertise` durant ma formation en M2 Expert IT big data & application intelligentes.

Ce projet est développé en PYTHON en utiliant des bases de données HIVE et MYSQL

## How to install ?
***
After cloning the repo in your local computer, run the application as a Flask project 

## Architctute
***
![Alt text](mcd.jpg?raw=true "Title")

## SCREEN SHOTS 
***
### Listing 
![Alt text](connexion.PNG?raw=true "Title")
### Noter un restaurant
![Alt text](projects.PNG?raw=true "Title")
### Cluster du map
![Alt text](newproject.PNG?raw=true "Title")
### Modification d'un projet
![Alt text](editproject.PNG?raw=true "Title")
### Détails d'un projet
![Alt text](projectdetails.PNG?raw=true "Title")
### Modification d'une tâche
![Alt text](update task.PNG?raw=true "Title")

## Gems utilisés
***
### devise
pour la gestion de l'authentification
### sqllite3
la Base de données pour l'ORM ACTIVE RECORD
### nested_scaffold
Pour assurer la relation entre les tables project et task (notion de cl étrangère avec l'ORM)