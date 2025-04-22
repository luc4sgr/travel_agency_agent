from crewai import Task
from textwrap import dedent

class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itinerary(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(f"""
                **Task**: Develop a 7-Day Travel Itinerary
                **Description**: Expand the city guide into a full 7-day travel itinerary with detailed 
                per-day plans, including weather forecasts, places to eat, packing suggestions, 
                and a budget breakdown. You MUST suggest actual places to visit, hotels to stay, 
                and restaurants to go to.

                **Parameters**: 
                - City: {city}
                - Trip Date: {travel_dates}
                - Traveler Interests: {interests}

                **Note**: {self.__tip_section()}
            """),
            agent=agent,
            expected_output=dedent("""
                A fully detailed 7-day itinerary, including:
                - Day-wise breakdown of activities
                - Recommended hotels, restaurants, and attractions
                - Estimated budget and weather forecast
            """),
        )

    def identify_city(self, agent, origin, cities, interests, travel_dates):
        return Task(
            description=dedent(f"""
                **Task**: Identify the Best City for the Trip
                **Description**: Compare cities based on weather, events, costs, and user interests. 
                Suggest the best one with supporting data including flight costs and cultural value.

                **Parameters**:
                - Origin: {origin}
                - Cities: {cities}
                - Interests: {interests}
                - Travel Dates: {travel_dates}

                **Note**: {self.__tip_section()}
            """),
            agent=agent,
            expected_output=dedent("""
                - Best city selected with justification
                - Cost, weather, and events included
                - Flight price estimates
            """),
        )

    def gather_city_info(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(f"""
                **Task**: Gather In-depth City Information
                **Description**: Create a detailed city guide including landmarks, local customs,
                weather, and hidden gems. Should support planning for the user interests and timeline.

                **Parameters**:
                - City: {city}
                - Interests: {interests}
                - Travel Dates: {travel_dates}

                **Note**: {self.__tip_section()}
            """),
            agent=agent,
            expected_output=dedent("""
                - Attractions and cultural details
                - Forecasts and high-level expenses
                - Local customs and hidden spots
            """),
        )
