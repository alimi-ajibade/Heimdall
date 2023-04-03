import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user(api_client):
    def do_create_user(
        data={
            "email": "test_user@domain.com",
            "first_name": "Test",
            "last_name": "User",
            "password": "qpdkri1230",
        }
    ):
        return api_client.post("/auth/users/", data)

    return do_create_user


@pytest.fixture
def activate_user(api_client, create_user):
    def do_activate_user(data):
        create_user()

        return api_client.post("/auth/users/activation/", data)

    return do_activate_user
