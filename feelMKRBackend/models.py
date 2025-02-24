from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UtilisateurManager(BaseUserManager):
    def create_user(self, email, nom, mot_de_passe=None, **extra_fields):
        if not email:
            raise ValueError('L\'email doit être renseigné')
        email = self.normalize_email(email)
        utilisateur = self.model(email=email, nom=nom, **extra_fields)
        utilisateur.set_password(mot_de_passe)  # Hachage du mot de passe
        utilisateur.save(using=self._db)
        return utilisateur

    def create_superuser(self, email, nom, mot_de_passe=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, nom, mot_de_passe, **extra_fields)


class Utilisateur(AbstractBaseUser, PermissionsMixin):
    class Meta:
        app_label = 'feelMKRBackend'

    TYPE_UTILISATEUR_CHOICES = [
        ('videaste', 'Videaste'),
        ('client', 'Client'),
    ]

    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=255)
    type_utilisateur = models.CharField(max_length=20, choices=TYPE_UTILISATEUR_CHOICES)

    date_creation = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='utilisateurs',  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='utilisateurs', 
        blank=True
    )

    objects = UtilisateurManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'type_utilisateur']

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        # Hachage du mot de passe avant de sauvegarder
        if self.mot_de_passe:
            self.set_password(self.mot_de_passe)
        super().save(*args, **kwargs)


class Portfolio(models.Model):
    class Meta:
        app_label = 'feelMKRBackend'

    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    description = models.TextField()

class Media(models.Model):
    class Meta:
        app_label = 'feelMKRBackend'

    TYPE_MEDIA_CHOICES = [
        ('photo', 'Photo'),
        ('video', 'Video'),
    ]

    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_MEDIA_CHOICES)
    url = models.TextField()
    description = models.TextField()

class Service(models.Model):
    class Meta:
        app_label = 'feelMKRBackend'

    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    description = models.TextField()
    tarif = models.DecimalField(max_digits=10, decimal_places=2)

class Reservation(models.Model):
    class Meta:
        app_label = 'feelMKRBackend'

    STATUT_CHOICES = [
        ('en attente', 'En attente'),
        ('confirmee', 'Confirmee'),
        ('annulee', 'Annulee'),
    ]

    client = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='reservations')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date_reservee = models.DateField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)

class Devis(models.Model):
    class Meta:
        app_label = 'feelMKRBackend'

    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)
    date_creation = models.DateTimeField(auto_now_add=True)

class Facture(models.Model):
    class Meta:
        app_label = 'feelMKRBackend'

    devis = models.ForeignKey(Devis, on_delete=models.CASCADE)
    montant_paye = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateTimeField(auto_now_add=True)

class Personnalisation(models.Model):
    class Meta:
        app_label = 'feelMKRBackend'
        
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    couleur_principale = models.CharField(max_length=7, null=True, blank=True)
    couleur_secondaire = models.CharField(max_length=7, null=True, blank=True)
    logo_url = models.TextField(null=True, blank=True)