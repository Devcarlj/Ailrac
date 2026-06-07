from database import get_settings

# Verbs/phrases that indicate the user wants to actually access/navigate to a platform
ACCESS_INTENTS = [
    "open", "go to", "visit", "access", "login to", "log in to",
    "sign in to", "check my", "look at my", "show my", "browse",
    "load", "navigate to", "take me to", "bring up",
]


def check_security(user_input: str) -> tuple[bool, str]:
    """
    Returns (is_blocked, refusal_message).
    If is_blocked is True, the request should NOT be processed further.
    """
    settings = get_settings()
    blocked_domains = settings.get("blocked_domains", [])

    lower_input = user_input.lower()

    for domain in blocked_domains:
        domain_lower = domain.lower().strip()
        # Extract base platform name e.g. "facebook" from "facebook.com"
        platform_name = domain_lower.split(".")[0]

        # Match either full domain or just the platform name in the input
        domain_hit = domain_lower in lower_input or platform_name in lower_input

        if domain_hit:
            # Only block if there's an action intent (not just mentioning the platform)
            for intent in ACCESS_INTENTS:
                if intent in lower_input:
                    return True, (
                        f"🔒 **Access Blocked** — I'm configured not to access or interact with "
                        f"**{domain}**. This platform is on your security blocklist.\n\n"
                        f"To change this, go to **⚙️ Settings → Security & Access Control** "
                        f"and remove `{domain}` from the blocked list."
                    )

    return False, ""


def check_safe_search(url: str) -> str:
    """Append SafeSearch param to Google searches if the setting is enabled."""
    settings = get_settings()
    if settings.get("safe_search") and "google.com/search" in url:
        if "safe=" not in url:
            url += "&safe=active"
    return url
