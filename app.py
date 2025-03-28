import streamlit as st
import logging
import os
from agent_graph import run_agents
from utils import apply_theme

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

st.set_page_config(page_title="Zovy's Multi-agent Vegetarian Assistant 🤖", layout="wide")
apply_theme()

st.markdown("<h1 style='text-align: center;'>Zovy's Multi-agent Vegetarian Assistant 🤖</h1>", unsafe_allow_html=True)
st.write("✅ App interface loaded successfully.")

try:
    mock_mode = st.sidebar.checkbox("🔌 Enable Mock Mode (no real API calls)", value=False)
    api_key = os.getenv("OPENAI_API_KEY")
    serper_key = os.getenv("SERPER_API_KEY")
    restaurant_name = st.text_input("Enter the restaurant name or details")

    if st.button("Run Multi-Agent Assistant") and restaurant_name and (mock_mode or (api_key and serper_key)):
        with st.spinner("Running agents..."):
            results = run_agents(restaurant_name, api_key if not mock_mode else None, serper_key if not mock_mode else None, mock_mode)

            if results.get("review"):
                st.subheader("📝 Blog Article and Google Review") 
                st.write(results['review'])

            if results.get("social_posts"):
                st.subheader("📣 Social Media Posts")
                for post in results['social_posts']:
                    st.markdown(f"- {post}")

            if results.get("menu"):
                st.subheader("🥗 Vegetarian Sampler Menu")
                st.write(results['menu'])

            if results.get("booking"):
                st.subheader("📞 Booking Info and Links")
                st.write(results['booking'])

            if results.get("map") and results.get("images"):
                st.subheader("🗺️ Map View")
                st.map(results['map'])
                st.subheader("📸 Restaurant Images")
                st.image(results['images'], width=250)
    else:
        st.info("Please enter a restaurant and ensure API keys are available via secrets or mock mode.")

except Exception as e:
    logger.error(f"An error occurred: {e}")
    st.error(f"An unexpected error occurred: {e}")
