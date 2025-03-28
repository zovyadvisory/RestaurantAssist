import streamlit as st
import requests
import os
import random

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

def fetch_images(query):
    return [
        f"https://source.unsplash.com/400x300/?{query.replace(' ', '+')},vegetarian",
        f"https://source.unsplash.com/400x300/?{query.replace(' ', '+')},vegan-food",
        f"https://source.unsplash.com/400x300/?{query.replace(' ', '+')},restaurant"
    ]

# ✅ Real Google Search using Serper API
def search_location(restaurant_name):
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key:
        return {"lat": [51.5074], "lon": [-0.1278]}, None

    headers = {"X-API-KEY": api_key}
    params = {"q": restaurant_name, "gl": "uk", "hl": "en"}
    response = requests.get("https://google.serper.dev/places", headers=headers, params=params)

    if response.status_code != 200:
        return {"lat": [51.5074], "lon": [-0.1278]}, None

    data = response.json()
    if not data.get("places"):
        return {"lat": [51.5074], "lon": [-0.1278]}, None

    place = data["places"][0]
    lat = place.get("latitude", 51.5074)
    lon = place.get("longitude", -0.1278)
    phone = place.get("phoneNumber", None)
    website = place.get("website", None)
    title = place.get("title", restaurant_name)

    return {
        "lat": [lat],
        "lon": [lon]
    }, {
        "name": title,
        "phone": phone,
        "website": website
    }