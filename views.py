from rest_framework import viewsets
from .models import Utilisateur, Portfolio, Media, Service, Reservation, Devis, Facture, Personnalisation
from .serializers import (UtilisateurSerializer, PortfolioSerializer, MediaSerializer,
                          ServiceSerializer, ReservationSerializer, DevisSerializer,
                          FactureSerializer, PersonnalisationSerializer)

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class DevisViewSet(viewsets.ModelViewSet):
    queryset = Devis.objects.all()
    serializer_class = DevisSerializer

class FactureViewSet(viewsets.ModelViewSet):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer

class PersonnalisationViewSet(viewsets.ModelViewSet):
    queryset = Personnalisation.objects.all()
    serializer_class = PersonnalisationSerializer
