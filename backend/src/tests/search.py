from datetime import datetime
from unittest.mock import patch

from fastapi import status
from src.api.accommodations import get_accommodations

@patch("src.api.accommodations.firebase_config")
def test_get_accommodations(mock_firebase_config):
    # Mock data
    mock_accommodations = [
        {
            "name": "Accommodation 1",
            "id": 1,
            "description": "Description 1",
            "bedrooms": 2,
            "location": "Location 1",
            "max_capacity": 4,
        },
        {
            "name": "Accommodation 2",
            "id": 2,
            "description": "Description 2",
            "bedrooms": 3,
            "location": "Location 2",
            "max_capacity": 6,
        },
    ]
    mock_accommodations_each = [
        {
            "name": "Accommodation 1",
            "id": 1,
            "description": "Description 1",
            "bedrooms": 2,
            "location": "Location 1",
            "max_capacity": 4,
            "reservations": {
                "2022-01-01": {"disponibility": True},
                "2022-01-02": {"disponibility": False},
            },
        },
        {
            "name": "Accommodation 2",
            "id": 2,
            "description": "Description 2",
            "bedrooms": 3,
            "location": "Location 2",
            "max_capacity": 6,
            "reservations": {
                "2022-01-01": {"disponibility": True},
                "2022-01-02": {"disponibility": True},
            },
        },
    ]

    # Mock firebase_config
    mock_db = mock_firebase_config.db
    mock_db.child.return_value.order_by_child.return_value = mock_db
    mock_db.limit_to_first.return_value.get.return_value = mock_accommodations_each

    # Test case 1: No filters
    result = get_accommodations()
    assert result == mock_accommodations

    # Test case 2: Filter by location
    result = get_accommodations(location="Location 1")
    assert result == [mock_accommodations[0]]

    # Test case 3: Filter by guests
    result = get_accommodations(guests=5)
    assert result == [mock_accommodations[1]]

    # Test case 4: Filter by checkin and checkout
    result = get_accommodations(
        checkin=datetime(2022, 1, 1),
        checkout=datetime(2022, 1, 2)
    )
    assert result == [mock_accommodations[1]]

    # Test case 5: No accommodations found
    mock_db.limit_to_first.return_value.get.return_value = []
    result = get_accommodations()
    assert result == status.HTTP_204_NO_CONTENT

    # Test case 6: Exception raised
    mock_db.limit_to_first.side_effect = Exception
    try:
        get_accommodations()
    except Exception as e:
        assert str(e) == "Failed looking for accommodations."