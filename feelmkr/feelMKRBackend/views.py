from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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
from .serializers import (
    DevisSerializer,
    FactureSerializer,
    MediaSerializer,
    PersonnalisationSerializer,
    PortfolioSerializer,
    ReservationSerializer,
    ServiceSerializer,
    UtilisateurSerializer,
)
import io
import google.generativeai as genai
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from reportlab.pdfgen import canvas

# Vues Utilisateur
class UtilisateurListCreate(generics.ListCreateAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Utilisation du gestionnaire pour créer l'utilisateur
        Utilisateur.objects.create_user(
            email=serializer.validated_data["email"],
            nom=serializer.validated_data["nom"],
            password=serializer.validated_data["password"],
            type_utilisateur=serializer.validated_data["type_utilisateur"],
        )

        return Response(status=status.HTTP_201_CREATED)


class UtilisateurRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [IsAuthenticated]

# Vues Utilisateur
class UtilisateurList(generics.ListAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [IsAuthenticated]

class UtilisateurDetail(generics.RetrieveAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [IsAuthenticated]

class UtilisateurByTypeList(generics.ListAPIView):
    serializer_class = UtilisateurSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        type_param = self.request.query_params.get('type_utilisateur')
        if type_param:
            return Utilisateur.objects.filter(type_utilisateur=type_param)
        return Utilisateur.objects.none()


class IsVideaste(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.type_utilisateur == "videaste"


# Vues Portfolio
class PortfolioListCreate(generics.ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class PortfolioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

# Vues Portfolio
class PortfolioList(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class PortfolioDetail(generics.RetrieveAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class PortfolioByUtilisateurList(generics.ListAPIView):
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        utilisateur_id = self.request.query_params.get('utilisateur_id')
        if utilisateur_id:
            return Portfolio.objects.filter(utilisateur_id=utilisateur_id)
        return Portfolio.objects.none()


# Vues Media
class MediaListCreate(generics.ListCreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class MediaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

# Vues Media
class MediaList(generics.ListAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class MediaDetail(generics.RetrieveAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class MediaByPortfolioList(generics.ListAPIView):
    serializer_class = MediaSerializer

    def get_queryset(self):
        portfolio_id = self.request.query_params.get('portfolio_id')
        if portfolio_id:
            return Media.objects.filter(portfolio_id=portfolio_id)
        return Media.objects.none()

# Vues Service
class ServiceListCreate(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# Vues Service
class ServiceList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetail(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# Vues Reservation
class ReservationListCreate(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            reservation = serializer.save()
            return Response(
                {
                    "message": "Réservation réussie",
                }, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

# Vues Reservation
class ReservationList(generics.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationDetail(generics.RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationByDateList(generics.ListAPIView):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        date_param = self.request.query_params.get('date')
        if date_param:
            return Reservation.objects.filter(date_reservation=date_param)
        return Reservation.objects.none()

class ReservationByUtilisateurList(generics.ListAPIView):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        utilisateur_id = self.request.query_params.get('utilisateur_id')
        if utilisateur_id:
            return Reservation.objects.filter(utilisateur_id=utilisateur_id)
        return Reservation.objects.none()


# Vues Devis
class DevisListCreate(generics.ListCreateAPIView):
    queryset = Devis.objects.all()
    serializer_class = DevisSerializer


class DevisRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Devis.objects.all()
    serializer_class = DevisSerializer

# Vues Devis
class DevisList(generics.ListAPIView):
    queryset = Devis.objects.all()
    serializer_class = DevisSerializer

class DevisDetail(generics.RetrieveAPIView):
    queryset = Devis.objects.all()
    serializer_class = DevisSerializer

class DevisByUtilisateurList(generics.ListAPIView):
    serializer_class = DevisSerializer

    def get_queryset(self):
        utilisateur_id = self.request.query_params.get('utilisateur_id')
        if utilisateur_id:
            return Devis.objects.filter(utilisateur_id=utilisateur_id)
        return Devis.objects.none()


# Vues Facture
class FactureListCreate(generics.ListCreateAPIView):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer


class FactureRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer

# Vues Facture
class FactureList(generics.ListAPIView):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer

class FactureDetail(generics.RetrieveAPIView):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer

class FactureByUtilisateurList(generics.ListAPIView):
    serializer_class = FactureSerializer

    def get_queryset(self):
        utilisateur_id = self.request.query_params.get('utilisateur_id')
        if utilisateur_id:
            return Facture.objects.filter(utilisateur_id=utilisateur_id)
        return Facture.objects.none()


# Vues Personnalisation
class PersonnalisationListCreate(generics.ListCreateAPIView):
    queryset = Personnalisation.objects.all()
    serializer_class = PersonnalisationSerializer


class PersonnalisationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personnalisation.objects.all()
    serializer_class = PersonnalisationSerializer

    # Vues Personnalisation
class PersonnalisationList(generics.ListAPIView):
    queryset = Personnalisation.objects.all()
    serializer_class = PersonnalisationSerializer

class PersonnalisationDetail(generics.RetrieveAPIView):
    queryset = Personnalisation.objects.all()
    serializer_class = PersonnalisationSerializer

# Configuration de Google Generative AI
genai.configure(api_key="VOTRE_CLE_API")

@csrf_exempt
def generer_devis_ia(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            # Récupération des données du formulaire frontend
            nom = data.get("nom")
            prenom = data.get("prenom")
            adresse = data.get("adresse")
            nom_service = data.get("nom_service")
            prix_service = data.get("prix_service")

            if not all([nom, prenom, adresse, nom_service, prix_service]):
                return HttpResponse("Données manquantes", status=400)

            # Génération du devis via l'IA
            prompt = (
                f"Crée un devis structuré en texte pour {prenom} {nom}, résidant à {adresse}, "
                f"concernant le service '{nom_service}' d'un montant de {prix_service} €. "
                f"Inclus une mise en page formelle avec le titre 'Devis', la date, et les détails du service."
            )

            response = genai.generate_text(prompt)
            texte_devis = response.text if response and response.text else "Erreur lors de la génération du devis."

            # Création du PDF directement à partir du texte généré
            buffer = io.BytesIO()
            pdf = canvas.Canvas(buffer)
            pdf.drawString(100, 800, "Devis AI - feelMKR")
            y = 780

            for line in texte_devis.split("\n"):
                pdf.drawString(100, y, line)
                y -= 20

            pdf.save()

            buffer.seek(0)
            response = HttpResponse(buffer, content_type="application/pdf")
            response["Content-Disposition"] = 'attachment; filename="devis.pdf"'
            return response

        except json.JSONDecodeError:
            return HttpResponse("Format JSON invalide", status=400)

    return HttpResponse("Méthode non autorisée", status=405)