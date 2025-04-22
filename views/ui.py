import streamlit as st

def run_ui(controller):
    st.title("Trip Planner Crew")

    with st.sidebar:
        st.header("Enter Your Trip Details")
        origin = st.text_input("From where will you be traveling from?")
        cities = st.text_input("Which cities are you interested in visiting?")
        date_range = st.text_input("What is the date range of your trip?")
        interests = st.text_input("What are your interests and hobbies?")

    if st.button("Generate Itinerary"):
        if not all([origin, cities, date_range, interests]):
            st.error("Please fill in all the fields to continue.")
        else:
            result = controller.run_trip_plan(origin, cities, date_range, interests)
            st.subheader("Your Personalized Trip Plan:")
            st.write(result)
