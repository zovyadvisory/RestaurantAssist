from utils import mock_gpt_response, search_location, fetch_images

def review_agent(context):
    if context["mock"]:
        return mock_gpt_response("review")
    
    prompt = f"""
    Write a blog-style and Google-style review for a vegetarian-friendly restaurant called "{context['restaurant']}".
    Focus on the vegetarian and vegan options. Mention ambience, service, and sample dishes.
    """
    return mock_gpt_response("real_call", prompt)

def social_media_agent(context):
    if context["mock"]:
        return mock_gpt_response("social_posts").split("\n")
    
    prompt = f"""
    Write 3 fun and engaging social media posts for the vegetarian restaurant "{context['restaurant']}".
    Include emojis, hashtags, and friendly tone.
    """
    return mock_gpt_response("real_call", prompt).split("\n")

def menu_agent(context):
    if context["mock"]:
        return mock_gpt_response("menu")

    prompt = f"""
    Create a 3-course vegetarian sampler menu for the restaurant "{context['restaurant']}".
    Include a starter, main, and dessert with short descriptions.
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
    Book **{name}** via:
    - [OpenTable](https://www.opentable.com)
    - [TheFork](https://www.thefork.com)
    - Website: {website}
    - Phone: {phone}
    """

def map_agent(context):
    location, info = search_location(context["restaurant"])
    context["location_info"] = info  # pass to other agents
    images = fetch_images(context["restaurant"]) if not context["mock"] else [
        "https://source.unsplash.com/400x300/?vegetarian-restaurant",
        "https://source.unsplash.com/400x300/?plant-based-food",
        "https://source.unsplash.com/400x300/?vegan-meal"
    ]
    return location, images