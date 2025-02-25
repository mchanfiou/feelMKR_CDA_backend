from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Utilisateur, Portfolio, Media, Service, Reservation, Devis, Facture, Personnalisation
from .serializers import (UtilisateurSerializer, PortfolioSerializer, MediaSerializer,
                          ServiceSerializer, ReservationSerializer, DevisSerializer,
                          FactureSerializer, PersonnalisationSerializer)

# Vues Utilisateur
class UtilisateurListCreate(generics.ListCreateAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Utilisation du gestionnaire pour créer l'utilisateur
        utilisateur = Utilisateur.objects.create_user(
            email=serializer.validated_data['email'],
            nom=serializer.validated_data['nom'],
            password=serializer.validated_data['password'],
            type_utilisateur=serializer.validated_data['type_utilisateur']
        )

        return Response(status=status.HTTP_201_CREATED)

class UtilisateurRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [IsAuthenticated]

class IsVideaste(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.type_utilisateur == 'videaste'
    
# Vues Portfolio
class PortfolioListCreate(generics.ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class PortfolioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

# Vues Media
class MediaListCreate(generics.ListCreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class MediaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

# Vues Service
class ServiceListCreate(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# Vues Reservation
class ReservationListCreate(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

# Vues Devis
class DevisListCreate(generics.ListCreateAPIView):
    queryset = Devis.objects.all()
    serializer_class = DevisSerializer

class DevisRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Devis.objects.all()
    serializer_class = DevisSerializer

# Vues Facture
class FactureListCreate(generics.ListCreateAPIView):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer

class FactureRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer

# Vues Personnalisation
class PersonnalisationListCreate(generics.ListCreateAPIView):
    queryset = Personnalisation.objects.all()
    serializer_class = PersonnalisationSerializer

class PersonnalisationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personnalisation.objects.all()
    serializer_class = PersonnalisationSerializer
