import streamlit as st

def run_ui(controller):
    st.title("🧭 Trip Planner Crew")

    with st.sidebar:
        st.header("✈️ Your Trip Details")
        origin = st.text_input("Origin")
        cities = st.text_input("Cities to consider")
        date_range = st.text_input("Travel period (e.g. 2025-06-10 to 2025-06-17)")
        interests = st.text_input("Interests (e.g. culture, food, nature)")

    if st.button("Generate Itinerary"):
        if not all([origin, cities, date_range, interests]):
            st.error("❌ Please fill out all fields.")
        else:
            with st.spinner("⏳ Generating your itinerary..."):
                result = controller.run_trip_plan(origin, cities, date_range, interests)

            if "final_summary" in result and result["final_summary"]:
                st.subheader("✅ Final Summary from the AI")
                st.markdown(result["final_summary"])

            if "task_outputs" in result and result["task_outputs"]:
                st.subheader("📋 Completed Tasks")
                for i, task in enumerate(result["task_outputs"]):
                    with st.expander(f"{i+1}. {task.get('agent', 'Agent')}"):
                        st.markdown(f"**Task Description:** {task['description']}")
                        st.markdown(f"**Result:**\n\n{task['raw']}")

            if "token_usage" in result and result["token_usage"]:
                st.subheader("📊 Token Usage")
                st.json(result["token_usage"])
