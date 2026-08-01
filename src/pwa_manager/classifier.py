from .models import PWAApplication


def classify(app: PWAApplication) -> str:
    """
    Detect application type.
    """

    name = app.name.lower()

    pwa_keywords = [
        "chatgpt",
        "copilot",
        "gemini",
        "word",
        "excel",
        "powerpoint",
        "outlook",
    ]

    for keyword in pwa_keywords:
        if keyword in name:
            return "pwa"

    # Chrome generated apps are PWA
    if app.source == "chrome":
        return "pwa"

    return "desktop"
