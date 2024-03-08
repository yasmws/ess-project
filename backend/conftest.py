import pytest
from fastapi.testclient import TestClient
from typing import Generator
from src.schemas.reservation import Reservation
from main import app


@pytest.fixture()
def my_reservation():
    return Reservation("123", "123", "123")

@pytest.fixture()
def all_reservations():
    return [Reservation("234","234","234"), my_reservation]


@pytest.fixture(scope="function")
def client() -> Generator:
    """
    Create a test client for the FastAPI app.
    """
    with TestClient(app) as c:
        yield c

@pytest.fixture
def context():
    """
    Variable to store context data between steps.
    Note: remember to always return the context variable at the end of the each steps.
    """
    b = {}
    yield b