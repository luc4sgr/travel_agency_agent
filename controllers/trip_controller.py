from models.agents import TravelAgents
from models.tasks import TravelTasks
from crewai import Crew

class TripController:
    def __init__(self):
        self.agents = TravelAgents()
        self.tasks = TravelTasks()

    def run_trip_plan(self, origin, cities, date_range, interests):
        # Agentes
        expert_travel_agent = self.agents.expert_travel_agent()
        city_selection_expert = self.agents.city_selection_expert()
        local_tour_guide = self.agents.local_tour_guide()

        # Tarefas
        plan_itinerary = self.tasks.plan_itinerary(
            expert_travel_agent, cities, date_range, interests
        )
        identify_city = self.tasks.identify_city(
            city_selection_expert, origin, cities, interests, date_range
        )
        gather_city_info = self.tasks.gather_city_info(
            local_tour_guide, cities, date_range, interests
        )

        # Crew
        crew = Crew(
            agents=[expert_travel_agent, city_selection_expert, local_tour_guide],
            tasks=[plan_itinerary, identify_city, gather_city_info],
            verbose=True,
        )

        result = crew.kickoff()

        # Estrutura esperada pelo Streamlit
        structured_result = {
            "final_summary": getattr(result, "raw", None),  # resumo final
            "task_outputs": [],
            "token_usage": getattr(result, "metrics", None),
        }

        # Verifica se há resultados de tarefas detalhados
        if hasattr(result, "tasks_output"):
            for task in result.tasks_output:
                structured_result["task_outputs"].append({
                    "description": task.description,
                    "expected_output": task.expected_output,
                    "summary": task.summary,
                    "raw": task.raw,
                    "agent": getattr(task, "agent", "Desconhecido")
                })

        return structured_result
