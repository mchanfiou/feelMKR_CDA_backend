import pytest

from feelMKRBackend.models import Utilisateur


@pytest.mark.django_db
def test_create_user():
    user = Utilisateur.objects.create_user(
        email="test@test.com",
        nom="test",
        mot_de_passe="1234test",
        type_utilisateur="client",
    )
    assert user.nom == "test"
