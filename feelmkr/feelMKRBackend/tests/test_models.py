import pytest

from feelMKRBackendr.models import Utilisateur


@pytest.mark.django_db
def test_create_user():
    user = Utilisateur.objects.create_user(
        email="test@test.com",
        nom="test",
        password="1234test",
        type_utilisateur="client",
    )
    assert user.nom == "test"
