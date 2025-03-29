def mock_gpt_response(type, prompt=None):
    if type == "review":
        return "🌱 A peaceful veggie haven! Their jackfruit tacos and vegan chocolate tart were divine. Cozy setting, warm staff. Highly recommended!"
    if type == "social_posts":
        return "\\n".join([
            "🥦 Just discovered the best vegan lasagna at GreenFork Bistro! #VeganEats #PlantPowered 💚",
            "🌿 Taste meets ethics! Try the tofu tikka at GreenFork today! 🌱 #MeatlessMonday",
            "🍃 Cozy, crunchy, cruelty-free. Dinner was amazing at GreenFork! #VeganFoodie"
        ])
    if type == "menu":
        return "**Starter**: Zucchini Fritters with Herbed Yogurt Dip\\n**Main**: Jackfruit Rendang with Coconut Rice\\n**Dessert**: Vegan Chocolate Mousse with Raspberry Coulis"
    if type == "booking":
        return "Book now at [OpenTable](https://www.opentable.com) or [TheFork](https://www.thefork.com), or call them directly via Google listings."
    if type == "real_call":
        return f"🤖 [Simulated GPT Response for Prompt]: {prompt.strip()[:80]}..."
    return ""