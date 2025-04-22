from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from crewai_tools import SerperDevTool, WebsiteSearchTool


class TravelAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(
            model="openai/gpt-3.5-turbo", max_tokens=4000, temperature=0.2
        )
        self.groq = ChatGroq(
            temperature=0, groq_api_key="DUMMY_GROQ_KEY", model="groq/llama3-8b-8192"
        )
        self.search_tool = SerperDevTool()
        self.web_rag_tool = WebsiteSearchTool()

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent("Expert in travel planning and logistics."),
            goal=dedent("Create a 7-day travel itinerary."),
            tools=[self.search_tool, self.web_rag_tool],
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent("Expert in city recommendation based on user interests."),
            goal=dedent("Select the best cities based on season, price and interest."),
            tools=[self.search_tool, self.web_rag_tool],
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent("Informed local expert on attractions and customs."),
            goal=dedent("Provide best local insights."),
            tools=[self.search_tool, self.web_rag_tool],
            verbose=True,
            llm=self.OpenAIGPT35,
        )
