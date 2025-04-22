from crewai import Task
from textwrap import dedent

class TravelTasks:
    def __note_section(self):
        return "Please ensure the information is accurate, comprehensive, and tailored to the user's travel preferences."

    def plan_itinerary(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(f"""
                **Task**: Develop a 7-Day Travel Itinerary
                **Description**: Create a comprehensive 7-day travel itinerary based on the city, user interests, and date range provided. The plan should include:
                - Daily activity schedules
                - Recommended restaurants, hotels, and attractions
                - Forecasted weather per day
                - Suggested items to pack
                - Estimated budget per day

                **Parameters**: 
                - City: {city}
                - Travel Dates: {travel_dates}
                - Traveler Interests: {interests}

                **Note**: {self.__note_section()}
            """),
            agent=agent,
            expected_output=dedent("""
                - Detailed 7-day itinerary
                - Hotels, restaurants, and points of interest
                - Budget breakdown and weather forecast per day
            """),
        )

    def identify_city(self, agent, origin, cities, interests, travel_dates):
        return Task(
            description=dedent(f"""
                **Task**: Identify the Best City for the Trip
                **Description**: Analyze and compare the provided cities to select the best destination for the user, based on:
                - Current and historical weather conditions
                - Local events or festivals during the travel period
                - Travel and accommodation costs
                - Compatibility with user's interests

                **Parameters**:
                - Origin: {origin}
                - Cities: {cities}
                - Interests: {interests}
                - Travel Dates: {travel_dates}

                **Note**: {self.__note_section()}
            """),
            agent=agent,
            expected_output=dedent("""
                - Recommended city with rationale
                - Climate forecast, cultural events, cost estimations
                - Suggested transportation or flight options
            """),
        )

    def gather_city_info(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(f"""
                **Task**: Gather In-depth City Information
                **Description**: Research and compile an in-depth city guide that includes:
                - Main tourist attractions and hidden gems
                - Local customs and travel etiquette
                - Weather expectations and cost of travel/lodging during the selected dates

                **Parameters**:
                - City: {city}
                - Interests: {interests}
                - Travel Dates: {travel_dates}

                **Note**: {self.__note_section()}
            """),
            agent=agent,
            expected_output=dedent("""
                - Complete city overview including cultural and practical travel info
                - Daily weather forecast and cost estimates
                - Suggestions tailored to user interests
            """),
        )
