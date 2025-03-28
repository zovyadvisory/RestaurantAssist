import random
import streamlit as st

# 💡 Theming support for Streamlit
def apply_theme():
    st.markdown("""
    <style>
        body {
            background-color: #f0fff0;
        }
        .stButton>button {
            background-color: #66bb6a;
            color: white;
            font-weight: bold;
        }
        .stTextInput>div>input {
            background-color: #ffffff;
        }
    </style>
    """, unsafe_allow_html=True)

# 🧪 Mock GPT responses for offline/demo use
def mock_gpt_response(type, prompt=None):
    if type == "review":
        return "🌱 A peaceful veggie haven! Their jackfruit tacos and vegan chocolate tart were divine. Cozy setting, warm staff. Highly recommended!"

    if type == "social_posts":
        return "\n".join([
            "🥦 Just discovered the best vegan lasagna at GreenFork Bistro! #VeganEats #PlantPowered 💚",
            "🌿 Taste meets ethics! Try the tofu tikka at GreenFork today! 🌱 #MeatlessMonday",
            "🍃 Cozy, crunchy, cruelty-free. Dinner was amazing at GreenFork! #VeganFoodie"
        ])

    if type == "menu":
        return "**Starter**: Zucchini Fritters with Herbed Yogurt Dip\n**Main**: Jackfruit Rendang with Coconut Rice\n**Dessert**: Vegan Chocolate Mousse with Raspberry Coulis"

    if type == "booking":
        return "Book now at [OpenTable](https://www.opentable.com) or [TheFork](https://www.thefork.com), or call them directly via Google listings."

    if type == "real_call":
        return f"🤖 [Simulated GPT Response for Prompt]: {prompt.strip()[:80]}..."

    return ""

# 🌍 Fake geolocation for map rendering (around central London)
def search_location(restaurant_name):
    return {
        "lat": [51.5074 + random.uniform(-0.01, 0.01)],
        "lon": [-0.1278 + random.uniform(-0.01, 0.01)]
    }

# 🖼️ Generate 3 Unsplash image URLs for food/restaurant
def fetch_images(query):
    return [
        f"https://source.unsplash.com/400x300/?{query.replace(' ', '+')},vegetarian",
        f"https://source.unsplash.com/400x300/?{query.replace(' ', '+')},vegan-food",
        f"https://source.unsplash.com/400x300/?{query.replace(' ', '+')},restaurant"
    ]