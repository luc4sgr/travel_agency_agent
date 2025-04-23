# def test_run_trip_plan_returns_result(trip_controller):
#     result = trip_controller.run_trip_plan(
#         "Fortaleza", "Lisbon, Madrid, Rome", "2025-06-10 to 2025-06-17", "history, food, culture"
#     )
#     assert result.raw == "mocked itinerary"
def test_run_trip_plan_returns_structured_result(trip_controller):
    result = trip_controller.run_trip_plan(
        origin="São Paulo",
        cities="Lisbon, Madrid, Rome",
        date_range="2025-06-10 to 2025-06-17",
        interests="history, food, culture"
    )

    # Verifica estrutura principal
    assert isinstance(result, dict)
    assert "final_summary" in result
    assert "task_outputs" in result
    assert "token_usage" in result

    # Verifica que o resumo final é uma string
    assert isinstance(result["final_summary"], str)

    # Verifica se há pelo menos uma tarefa
    assert isinstance(result["task_outputs"], list)
    assert len(result["task_outputs"]) > 0

    # Verifica campos em uma das tarefas
    first_task = result["task_outputs"][0]
    assert "description" in first_task
    assert "raw" in first_task
    assert "agent" in first_task
    assert isinstance(first_task["raw"], str)

    # Verifica métrica (mockada)
    assert isinstance(result["token_usage"], dict) or result["token_usage"] is None
