from django.db import models
from django.contrib.auth.models import User

class Utilisateur(models.Model):
    TYPE_UTILISATEUR_CHOICES = [
        ('videaste', 'Videaste'),
        ('client', 'Client'),
    ]

    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=255)
    type_utilisateur = models.CharField(max_length=20, choices=TYPE_UTILISATEUR_CHOICES)

class Portfolio(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    description = models.TextField()

class Media(models.Model):
    TYPE_MEDIA_CHOICES = [
        ('photo', 'Photo'),
        ('video', 'Vidéo'),
    ]

    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_MEDIA_CHOICES)
    url = models.TextField()
    description = models.TextField()

class Service(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    description = models.TextField()
    tarif = models.DecimalField(max_digits=10, decimal_places=2)

class Reservation(models.Model):
    STATUT_CHOICES = [
        ('en attente', 'En attente'),
        ('confirmée', 'Confirmée'),
        ('annulée', 'Annulée'),
    ]

    client = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='reservations')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date_reservee = models.DateField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)

class Devis(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)
    date_creation = models.DateTimeField(auto_now_add=True)

class Facture(models.Model):
    devis = models.ForeignKey(Devis, on_delete=models.CASCADE)
    montant_paye = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateTimeField(auto_now_add=True)

class Personnalisation(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    couleur_principale = models.CharField(max_length=7, null=True, blank=True)
    couleur_secondaire = models.CharField(max_length=7, null=True, blank=True)
    logo_url = models.TextField(null=True, blank=True)
