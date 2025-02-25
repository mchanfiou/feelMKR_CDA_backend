from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (UtilisateurListCreate, UtilisateurRetrieveUpdateDestroy,
                    PortfolioListCreate, PortfolioRetrieveUpdateDestroy,
                    MediaListCreate, MediaRetrieveUpdateDestroy,
                    ServiceListCreate, ServiceRetrieveUpdateDestroy,
                    ReservationListCreate, ReservationRetrieveUpdateDestroy,
                    DevisListCreate, DevisRetrieveUpdateDestroy,
                    FactureListCreate, FactureRetrieveUpdateDestroy,
                    PersonnalisationListCreate, PersonnalisationRetrieveUpdateDestroy)

urlpatterns = [
    path('utilisateurs/', UtilisateurListCreate.as_view(), name='utilisateur-list-create'),
    path('utilisateurs/<int:pk>/', UtilisateurRetrieveUpdateDestroy.as_view(), name='utilisateur-detail'),
    
    path('portfolios/', PortfolioListCreate.as_view(), name='portfolio-list-create'),
    path('portfolios/<int:pk>/', PortfolioRetrieveUpdateDestroy.as_view(), name='portfolio-detail'),
    
    path('medias/', MediaListCreate.as_view(), name='media-list-create'),
    path('medias/<int:pk>/', MediaRetrieveUpdateDestroy.as_view(), name='media-detail'),
    
    path('services/', ServiceListCreate.as_view(), name='service-list-create'),
    path('services/<int:pk>/', ServiceRetrieveUpdateDestroy.as_view(), name='service-detail'),
    
    path('reservations/', ReservationListCreate.as_view(), name='reservation-list-create'),
    path('reservations/<int:pk>/', ReservationRetrieveUpdateDestroy.as_view(), name='reservation-detail'),
    
    path('devis/', DevisListCreate.as_view(), name='devis-list-create'),
    path('devis/<int:pk>/', DevisRetrieveUpdateDestroy.as_view(), name='devis-detail'),
    
    path('factures/', FactureListCreate.as_view(), name='facture-list-create'),
    path('factures/<int:pk>/', FactureRetrieveUpdateDestroy.as_view(), name='facture-detail'),
    
    path('personnalisations/', PersonnalisationListCreate.as_view(), name='personnalisation-list-create'),
    path('personnalisations/<int:pk>/', PersonnalisationRetrieveUpdateDestroy.as_view(), name='personnalisation-detail'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
]
