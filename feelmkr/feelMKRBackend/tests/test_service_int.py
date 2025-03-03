import pytest
from feelMKRBackend.models import Utilisateur, Service

@pytest.mark.django_db
def test_videaste_create_service():
    videaste = Utilisateur.objects.create_user(
        email="videaste@test.com", 
        nom="Videaste Test", 
        type_utilisateur="videaste", 
        password="test1234"
    )

    service = Service.objects.create(
        utilisateur=videaste, 
        nom="Tournage Mariage", 
        description="Filmer un mariage en HD", 
        tarif=500.00
    )

    assert service.utilisateur == videaste
    assert service.nom == "Tournage Mariage"
    assert Service.objects.count() == 1
