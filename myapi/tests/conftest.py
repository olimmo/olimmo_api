# conftest.py

import pytest
from pytest_django.fixtures import django_db_setup

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass
