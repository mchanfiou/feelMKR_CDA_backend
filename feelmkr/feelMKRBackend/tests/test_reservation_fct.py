import pytest
from rest_framework.test import APIClient
from feelMKRBackend.models import Utilisateur, Service, Reservation

@pytest.mark.django_db
def test_reservation_service():
    client = APIClient()

    utilisateur = Utilisateur.objects.create_user(
        email="client@test.com", 
        nom="Client Test", 
        type_utilisateur="client", 
        password="test1234"
    )
    service = Service.objects.create(
        utilisateur=utilisateur, 
        nom="Séance Photo", 
        description="Shooting en studio", 
        tarif=150.00
    )

    response = client.post(
        "/reservations/", 
        {"client": utilisateur.id, "service": service.id, "date_reservee": "2025-03-04", "statut": "en attente"}, 
        format="json"
    )
    assert response.status_code == 201
    assert response.data["message"] == "Réservation réussie"

    # Vérification en base de données
    assert Reservation.objects.count() == 1
    reservation = Reservation.objects.first()
    assert reservation.client == utilisateur
    assert reservation.service == service
