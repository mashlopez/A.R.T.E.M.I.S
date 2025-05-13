# Utiliser une image Python officielle comme base
FROM python:3.11-slim

# Installer les dépendances système nécessaires pour Tkinter et d'autres bibliothèques
RUN apt-get update && apt-get install -y \
    tk \
    && apt-get clean

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le contenu du répertoire local dans le conteneur
COPY . /app

# Installer les dépendances Python
RUN pip install --upgrade pip
RUN pip install transformers torch

# Exposer le port si nécessaire (par exemple pour une API ou un service web)
# EXPOSE 5000

# Exécuter l'application lorsque le conteneur démarre
CMD ["python", "artemis_with_memory.py"]
