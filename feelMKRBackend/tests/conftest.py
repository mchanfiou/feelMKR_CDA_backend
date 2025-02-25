import os
import pytest

@pytest.fixture(autouse=True)
def set_django_env():
    # Sauvegarde l'état actuel de DJANGO_ENV
    original_env = os.getenv("DJANGO_ENV")

    # Définit DJANGO_ENV sur test avant les tests
    os.environ["DJANGO_ENV"] = "test"

    yield  # Laisse le test s'exécuter

    # Rétablit DJANGO_ENV à sa valeur d'origine après les tests
    if original_env is not None:
        os.environ["DJANGO_ENV"] = original_env
    else:
        del os.environ["DJANGO_ENV"]  # Supprime la variable si elle n'existait pas
