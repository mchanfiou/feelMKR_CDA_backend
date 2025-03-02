from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    DevisListCreate, DevisRetrieveUpdateDestroy,
    FactureListCreate, FactureRetrieveUpdateDestroy,
    MediaListCreate, MediaRetrieveUpdateDestroy,
    PersonnalisationListCreate, PersonnalisationRetrieveUpdateDestroy,
    PortfolioListCreate, PortfolioRetrieveUpdateDestroy,
    ReservationListCreate, ReservationRetrieveUpdateDestroy,
    ServiceListCreate, ServiceRetrieveUpdateDestroy,
    UtilisateurListCreate, UtilisateurRetrieveUpdateDestroy,
    UtilisateurList, UtilisateurByTypeList,
    PortfolioList, PortfolioByUtilisateurList,
    MediaList,  MediaByPortfolioList,
    ServiceList, ReservationList,
    ReservationByDateList, ReservationByUtilisateurList,
    DevisList, DevisByUtilisateurList,
    FactureList, FactureByUtilisateurList,
    PersonnalisationList,generer_devis_ia,
)

urlpatterns = [
    # Authentification
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Utilisateurs
    path("utilisateurs/", UtilisateurListCreate.as_view(), name="utilisateur-list-create"),
    path("utilisateurs/<int:pk>/", UtilisateurRetrieveUpdateDestroy.as_view(), name="utilisateur-detail"),
    path('utilisateurs/all/', UtilisateurList.as_view(), name='utilisateur-list'),
    path('utilisateurs/type/', UtilisateurByTypeList.as_view(), name='utilisateur-by-type'),

    # Portfolios
    path("portfolios/", PortfolioListCreate.as_view(), name="portfolio-list-create"),
    path("portfolios/<int:pk>/", PortfolioRetrieveUpdateDestroy.as_view(), name="portfolio-detail"),
    path('portfolios/all/', PortfolioList.as_view(), name='portfolio-list'),
    path('portfolios/utilisateur/', PortfolioByUtilisateurList.as_view(), name='portfolio-by-utilisateur'),

    # Medias
    path("medias/", MediaListCreate.as_view(), name="media-list-create"),
    path("medias/<int:pk>/", MediaRetrieveUpdateDestroy.as_view(), name="media-detail"),
    path('media/all/', MediaList.as_view(), name='media-list'),
    path('media/portfolio/', MediaByPortfolioList.as_view(), name='media-by-portfolio'),

    # Services
    path("services/", ServiceListCreate.as_view(), name="service-list-create"),
    path("services/<int:pk>/", ServiceRetrieveUpdateDestroy.as_view(), name="service-detail"),
    path('services/all/', ServiceList.as_view(), name='service-list'),

    # Réservations
    path("reservations/", ReservationListCreate.as_view(), name="reservation-list-create"),
    path("reservations/<int:pk>/", ReservationRetrieveUpdateDestroy.as_view(), name="reservation-detail"),
    path('reservations/all/', ReservationList.as_view(), name='reservation-list'),
    path('reservations/date/', ReservationByDateList.as_view(), name='reservation-by-date'),
    path('reservations/utilisateur/', ReservationByUtilisateurList.as_view(), name='reservation-by-utilisateur'),

    # Devis
    path("devis/", DevisListCreate.as_view(), name="devis-list-create"),
    path("devis/<int:pk>/", DevisRetrieveUpdateDestroy.as_view(), name="devis-detail"),
    path('devis/all/', DevisList.as_view(), name='devis-list'),
    path('devis/utilisateur/', DevisByUtilisateurList.as_view(), name='devis-by-utilisateur'),

    # Factures
    path("factures/", FactureListCreate.as_view(), name="facture-list-create"),
    path("factures/<int:pk>/", FactureRetrieveUpdateDestroy.as_view(), name="facture-detail"),
    path('factures/all/', FactureList.as_view(), name='facture-list'),
    path('factures/utilisateur/', FactureByUtilisateurList.as_view(), name='facture-by-utilisateur'),

    # Personnalisations
    path("personnalisations/", PersonnalisationListCreate.as_view(), name="personnalisation-list-create"),
    path("personnalisations/<int:pk>/", PersonnalisationRetrieveUpdateDestroy.as_view(), name="personnalisation-detail"),
    path('personalisations/all/', PersonnalisationList.as_view(), name='personnalisation-list'),

    path("devis/generer-ia/", generer_devis_ia, name="generer_devis_ia"),
]