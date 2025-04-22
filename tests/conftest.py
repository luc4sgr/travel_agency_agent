import pytest
from unittest.mock import patch, MagicMock
from controllers.trip_controller import TripController

@pytest.fixture(autouse=True)
def mock_kickoff():
    """Mock automático para Crew.kickoff() em todos os testes"""
    with patch("crewai.Crew.kickoff") as mock:
        mock_return = MagicMock()
        mock_return.raw = "mocked itinerary"
        mock.return_value = mock_return
        yield mock

@pytest.fixture
def trip_controller():
    return TripController()
