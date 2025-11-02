"""Module providing unit tests for the API (src/main.py)."""

from unittest.mock import patch

from fastapi import status
from fastapi.testclient import TestClient

from ..src import main

client = TestClient(main.app)


def test_welcome():
    """Unit test for the welcome endpoint."""
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Welcome to DevOps Project"}


def test_version_success():
    """Unit test for the version endpoint (success)."""
    with patch.object(main, "VERSION", "v0.0.1"):
        response = client.get("/version")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"version": "v0.0.1"}


def test_version_when_config_missing():
    """Unit test for the version endpoint (failure)."""
    with patch.object(main, "VERSION", ""):
        response = client.get("/version")
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.json() == {"detail": "Service configuration unavailable"}
