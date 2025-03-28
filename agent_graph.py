from agents import review_agent, social_media_agent, menu_agent, booking_agent, map_agent

def run_agents(restaurant_name, api_key, serper_key, mock):
    context = {
        "restaurant": restaurant_name,
        "api_key": api_key,
        "serper_key": serper_key,
        "mock": mock
    }

    review = review_agent(context)
    social_posts = social_media_agent(context)
    menu = menu_agent(context)
    booking = booking_agent(context)
    map_data, images = map_agent(context)

    return {
        "review": review,
        "social_posts": social_posts,
        "menu": menu,
        "booking": booking,
        "map": map_data,
        "images": images
    }
