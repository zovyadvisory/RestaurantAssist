import requests
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import mock_gpt_response, search_location, fetch_images

def review_agent(context):
    if context["mock"]:
        return mock_gpt_response("review")

    # Step 1: Get real review snippets using Serper
    api_key = context.get("serper_key")
    headers = {"X-API-KEY": api_key}
    params = {
        "q": context["restaurant"],
        "gl": "uk",
        "hl": "en"
    }

    response = requests.get("https://google.serper.dev/places", headers=headers, params=params)

    if response.status_code != 200:
        return "Unable to fetch real reviews at this time."

    data = response.json()
    places = data.get("places", [])
    if not places:
        return "No real reviews found for this restaurant."

    place = places[0]
    reviews = place.get("reviews", [])
    extracted_reviews = [r.get("snippet", "") for r in reviews][:3]

    review_text = "\n".join(f"- {r}" for r in extracted_reviews if r)

    # Step 2: Generate a blog-style review summary using GPT
    prompt = f"""
    Based on the following real customer reviews for the restaurant "{context['restaurant']}", write a polished blog-style and Google-style review.
    Focus on vegetarian and vegan food experiences, quality, service, and ambience.

    Reviews:
    {review_text}
    """

    return mock_gpt_response("real_call", prompt)

def social_media_agent(context):
    if context["mock"]:
        return mock_gpt_response("social_posts").split("\n")

    prompt = f"""
    Write 3 fun and engaging social media posts for the vegetarian restaurant "{context['restaurant']}".
    Include emojis, hashtags, and a friendly tone.
    """
    return mock_gpt_response("real_call", prompt).split("\n")  

def menu_agent(context):
    if context["mock"]:
        return mock_gpt_response("menu")

    prompt = f"""
    Create a 3-course vegetarian sampler menu for the restaurant "{context['restaurant']}".
    Include a starter, main course, and dessert, each with a short description.
    """
    return mock_gpt_response("real_call", prompt)


def booking_agent(context):
    if context["mock"]:
        return mock_gpt_response("booking")

    info = context.get("location_info", {})
    phone = info.get("phone", "Not available") if info else "Not available"
    website = info.get("website", "Not listed") if info else "Not listed"
    name = info.get("name", context["restaurant"]) if info else context["restaurant"]

    return f"""
    📞 Book **{name}** via:
    - [OpenTable](https://www.opentable.com)
    - [TheFork](https://www.thefork.com)
    - Website: {website}
    - Phone: {phone}
    """

def map_agent(context):
    location, info = search_location(context["restaurant"])
    context["location_info"] = info  # share with booking agent
    images = fetch_images(context["restaurant"]) if not context["mock"] else [
        "https://source.unsplash.com/400x300/?vegetarian-restaurant",
        "https://source.unsplash.com/400x300/?plant-based-food",
        "https://source.unsplash.com/400x300/?vegan-meal"
    ]
    return location, images