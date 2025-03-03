from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import (
    Devis,
    Facture,
    Media,
    Personnalisation,
    Portfolio,
    Reservation,
    Service,
    Utilisateur,
)


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = "__all__"
        extra_kwargs = {
            "mot_de_passe": {"write_only": True}
        }  # Exclure le mot de passe de la lecture


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = "__all__"


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"


class DevisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devis
        fields = "__all__"


class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = "__all__"


class PersonnalisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnalisation
        fields = "__all__"

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username = serializers.EmailField()  # Change le champ username par email
    
    def validate(self, attrs):
        # Personnalise la validation si nécessaire
        return super().validate(attrs)