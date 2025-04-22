from models.agents import TravelAgents
from models.tasks import TravelTasks
from crewai import Crew

class TripController:
    def __init__(self):
        self.agents = TravelAgents()
        self.tasks = TravelTasks()

    def run_trip_plan(self, origin, cities, date_range, interests):
        # Agents
        expert_travel_agent = self.agents.expert_travel_agent()
        city_selection_expert = self.agents.city_selection_expert()
        local_tour_guide = self.agents.local_tour_guide()

        # Tasks
        plan_itinerary = self.tasks.plan_itinerary(
            expert_travel_agent, cities, date_range, interests
        )
        identify_city = self.tasks.identify_city(
            city_selection_expert, origin, cities, interests, date_range
        )
        gather_city_info = self.tasks.gather_city_info(
            local_tour_guide, cities, date_range, interests
        )

        # Crew execution
        crew = Crew(
            agents=[expert_travel_agent, city_selection_expert, local_tour_guide],
            tasks=[plan_itinerary, identify_city, gather_city_info],
            verbose=True,
        )

        result = crew.kickoff()

        return {
            "final_summary": getattr(result, "raw", None),
            "task_outputs": [
                {
                    "description": task.description,
                    "expected_output": task.expected_output,
                    "summary": task.summary,
                    "raw": task.raw,
                    "agent": getattr(task, "agent", "Unknown")
                }
                for task in getattr(result, "tasks_output", [])
            ],
            "token_usage": getattr(result, "metrics", None)
        }
