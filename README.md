#### Déploiement d'une base de données postgresql dans un container docker et une api fastapi
-----------------

#### Connexion en ssh pour pouvoir afficher l'interface de l'api
-----------------
Exécuter le commande suivante pour afficher l'interface fastapi
```bash
$ ssh -i data_enginering_machine.pem -L 8000:127.0.0.1:8000 user@ip-machine-distante
```
-----------------

#### Déploiement de l'api
-----------------
Exécuter la commande suivante pour déployer l'api
```bash
$ docker-compose up --build
```
-----------------

#### affichage des endpoints
-----------------
Charger cette url pour afficher est tester les endpoints
```bash
$ http://127.0.0.1:8000/docs#/
```
-----------------
