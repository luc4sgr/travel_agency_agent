import pytest
from unittest.mock import patch, MagicMock
from controllers.trip_controller import TripController

@pytest.fixture(autouse=True)
def mock_kickoff():
    """Automatically mock Crew.kickoff for all tests."""
    with patch("crewai.Crew.kickoff") as mock:
        mock_result = MagicMock()
        mock_result.raw = "mocked itinerary"
        mock_result.metrics = {"total_tokens": 12345}

        mock_result.tasks_output = [
            MagicMock(
                description="Mock task description",
                expected_output="Expected output format",
                summary="Task summary",
                raw="Task result content",
                agent="Mock Agent"
            )
        ]

        mock.return_value = mock_result
        yield mock

@pytest.fixture
def trip_controller():
    return TripController()
