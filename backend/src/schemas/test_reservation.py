import pytest
from datetime import date
from reservation import Reservation

def test_my_reservation_in_all_reservations(my_reservation, all_reservations):
    assert my_reservation in all_reservations