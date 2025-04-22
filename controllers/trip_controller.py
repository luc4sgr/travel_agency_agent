from models.agents import TravelAgents
from models.tasks import TravelTasks
from crewai import Crew

class TripController:
    def __init__(self):
        self.agents = TravelAgents()
        self.tasks = TravelTasks()

    def run_trip_plan(self, origin, cities, date_range, interests):
        expert_travel_agent = self.agents.expert_travel_agent()
        city_selection_expert = self.agents.city_selection_expert()
        local_tour_guide = self.agents.local_tour_guide()

        plan_itinerary = self.tasks.plan_itinerary(
            expert_travel_agent, cities, date_range, interests
        )
        identify_city = self.tasks.identify_city(
            city_selection_expert, origin, cities, interests, date_range
        )
        gather_city_info = self.tasks.gather_city_info(
            local_tour_guide, cities, date_range, interests
        )

        crew = Crew(
            agents=[expert_travel_agent, city_selection_expert, local_tour_guide],
            tasks=[plan_itinerary, identify_city, gather_city_info],
            verbose=True,
        )

        return crew.kickoff()
