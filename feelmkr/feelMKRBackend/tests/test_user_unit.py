import pytest
from feelMKRBackend.models import UtilisateurManager

def test_create_user_without_email():
    manager = UtilisateurManager()
    
    with pytest.raises(ValueError, match="L'email doit être renseigné"):
        manager.create_user(email="", nom="Test", type_utilisateur="client", password="test1234")