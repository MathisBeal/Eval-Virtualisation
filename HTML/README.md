# Web app statique

## Le dockerfile
### L'image
On utilise comme base une image nginx alpine, qu'on update pour appliquer de potentielles mises à jour.

### Le port
On expose le port 80 pour y acceder depuis l'exterieur du conteneur

## Le docker-compose
### Le build
On build directement l'image depuis le compose

### Le restart
On fait en sorte que le conteneur redémarre automatiquement si besoin

### Le port
On réexpose le port 80 pour pouvoir y accéder

### Le volume
On lie le dossier `for_volume` au dossier `/usr/share/nginx/html` du container pour ne pas avoir à les copier, et pouvoir les modifier directement sur l'hôte
