from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UtilisateurManager(BaseUserManager):
    def create_user(self, email, nom, type_utilisateur, password=None):
        if not email:
            raise ValueError("L'email doit être renseigné")

        email = self.normalize_email(email)
        utilisateur = self.model(
            email=email, nom=nom, type_utilisateur=type_utilisateur
        )

        if password:  # Vérifie si un mot de passe est fourni
            utilisateur.set_password(password)  # Hachage du mot de passe

        utilisateur.save(using=self._db)
        return utilisateur

    def create_superuser(self, email, nom, password=None):
        utilisateur = self.create_user(
            email=email, nom=nom, type_utilisateur="videaste", password=password
        )

        utilisateur.is_staff = True  # Accès au panel admin
        utilisateur.is_superuser = True  # Droits super-utilisateur

        utilisateur.save(using=self._db)
        return utilisateur


class Utilisateur(AbstractBaseUser, PermissionsMixin):
    class Meta:
        app_label = "feelMKRBackend"

    TYPE_UTILISATEUR_CHOICES = [
        ("videaste", "Videaste"),
        ("client", "Client"),
    ]

    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    type_utilisateur = models.CharField(max_length=20, choices=TYPE_UTILISATEUR_CHOICES)
    is_active = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        "auth.Group", related_name="utilisateurs", blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission", related_name="utilisateurs", blank=True
    )

    objects = UtilisateurManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nom", "type_utilisateur"]

    def __str__(self):
        return self.email


class Portfolio(models.Model):
    class Meta:
        app_label = "feelMKRBackend"

    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    description = models.TextField()


class Media(models.Model):
    class Meta:
        app_label = "feelMKRBackend"

    TYPE_MEDIA_CHOICES = [
        ("photo", "Photo"),
        ("video", "Video"),
    ]

    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_MEDIA_CHOICES)
    url = models.TextField()
    description = models.TextField()


class Service(models.Model):
    class Meta:
        app_label = "feelMKRBackend"

    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    description = models.TextField()
    tarif = models.DecimalField(max_digits=10, decimal_places=2)


class Reservation(models.Model):
    class Meta:
        app_label = "feelMKRBackend"

    STATUT_CHOICES = [
        ("en attente", "En attente"),
        ("confirmee", "Confirmee"),
        ("annulee", "Annulee"),
    ]

    client = models.ForeignKey(
        Utilisateur, on_delete=models.CASCADE, related_name="reservations"
    )
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date_reservee = models.DateField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)


class Devis(models.Model):
    class Meta:
        app_label = "feelMKRBackend"

    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)
    date_creation = models.DateTimeField(auto_now_add=True)


class Facture(models.Model):
    class Meta:
        app_label = "feelMKRBackend"

    devis = models.ForeignKey(Devis, on_delete=models.CASCADE)
    montant_paye = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateTimeField(auto_now_add=True)


class Personnalisation(models.Model):
    class Meta:
        app_label = "feelMKRBackend"

    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    couleur_principale = models.CharField(max_length=7, null=True, blank=True)
    couleur_secondaire = models.CharField(max_length=7, null=True, blank=True)
    logo_url = models.TextField(null=True, blank=True)
