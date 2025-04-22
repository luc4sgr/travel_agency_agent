import pytest
from controllers.trip_controller import TripController

@pytest.fixture
def trip_controller():
    return TripController()

def test_run_trip_plan_returns_result(trip_controller):
    origin = "São Paulo"
    cities = "Lisbon, Madrid, Rome"
    date_range = "2025-06-10 to 2025-06-17"
    interests = "history, food, culture"

    result = trip_controller.run_trip_plan(origin, cities, date_range, interests)
    
    assert result is not None
    assert isinstance(result, str)
