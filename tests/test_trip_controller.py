def test_run_trip_plan_returns_result(trip_controller):
    result = trip_controller.run_trip_plan(
        "Fortaleza", "Lisbon, Madrid, Rome", "2025-06-10 to 2025-06-17", "history, food, culture"
    )
    assert result.raw == "mocked itinerary"
