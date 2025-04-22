import streamlit as st

def run_ui(controller):
    st.title("🧭 Trip Planner Crew")

    with st.sidebar:
        st.header("✈️ Detalhes da sua viagem")
        origin = st.text_input("Origem")
        cities = st.text_input("Cidades para considerar")
        date_range = st.text_input("Período da viagem (ex: 10/06/2025 a 17/06/2025)")
        interests = st.text_input("Interesses (ex: cultura, gastronomia, natureza)")

    if st.button("Gerar Itinerário"):
        if not all([origin, cities, date_range, interests]):
            st.error("❌ Por favor, preencha todos os campos.")
        else:
            with st.spinner("⏳ Gerando roteiro..."):
                result = controller.run_trip_plan(origin, cities, date_range, interests)

            # Resumo final do Crew
            if "cru" in result and result["cru"]:
                st.subheader("✅ Resumo final da IA")
                st.markdown(result["cru"])

            # Detalhes por tarefa
            if "tarefas_saída" in result and result["tarefas_saída"]:
                st.subheader("📋 Tarefas executadas")
                for i, task in enumerate(result["tarefas_saída"]):
                    with st.expander(f"{i+1}. {task.get('agent', 'Agente')}"):
                        st.markdown(f"**Descrição:** {task['description']}")
                        st.markdown(f"**Resultado:**\n\n{task['raw']}")

            # Métricas de uso
            if "uso de token" in result and result["uso de token"]:
                st.subheader("📊 Métricas de uso")
                st.json(result["uso de token"])
