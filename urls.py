from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UtilisateurViewSet, PortfolioViewSet, MediaViewSet,
                    ServiceViewSet, ReservationViewSet, DevisViewSet,
                    FactureViewSet, PersonnalisationViewSet)

router = DefaultRouter()
router.register(r'utilisateurs', UtilisateurViewSet)
router.register(r'portfolios', PortfolioViewSet)
router.register(r'medias', MediaViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'devis', DevisViewSet)
router.register(r'factures', FactureViewSet)
router.register(r'personnalisation', PersonnalisationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
