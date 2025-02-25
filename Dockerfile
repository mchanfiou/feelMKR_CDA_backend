# Utilise une image Python officielle avec la bonne version
FROM python:3.13.2

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port (ajuste si nécessaire)
EXPOSE 8000

# Commande pour lancer le serveur Django
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "feelMKRBackend.wsgi:application"]