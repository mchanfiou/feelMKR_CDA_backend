from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
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
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if not email or not password:
            raise serializers.ValidationError("Email and password are required")

        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError("No active account found with the given credentials")

        return super().validate(attrs)
