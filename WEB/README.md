# Web app avec redis

## Le dockerfile
### L'image
On utilise comme base une image python alpine, qu'on update pour appliquer de potentielles mises à jour.

### Le work directory
On se place dans le dossier `/app` du conteneur pour y travailler

### Le port
On expose le port 5000 pour y acceder depuis l'exterieur du conteneur

### Les libs python
On copie le fichier `requirements.txt` qui liste les dépendances nécéssaires, puis on les installes avec la commande nécéssaire

### Le lancement du conteneur
On copie notre fichier python à executer au lancement du conteneur,
puis on fait en sorte que le conteneur execute `python app.py` au lancement.

## Le docker-compose
### Le build
On build directement l'image depuis le compose

### Le restart
On fait en sorte que le conteneur redémarre automatiquement si besoin

### Dépendance
On le fait dépendre d'un autre service dont il a besoin (redis)

### Réseau
On le lie au réseau qu'on crée, un réseau "bridge" qu'on appelle `my_network`

### Ports
On lie le port 5000 du conteneur au 80 de l'hôte, pour y accéder facilement depuis le navigateur (=>80, aussi pour qu'il soit accessible)

### Le service redis
On applique globalement les mêmes stratégies:
- Le restart automatique
- Le lien au network
- L'exposition du port nécéssaire (ici 6379)

On crée un volume pour faire persister les données du sevice redis.
