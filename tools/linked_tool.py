from tools.tools import CustomSerpAPIWrapper


def get_profile_url(text):
    """Searches for Linked or Twitter URL"""
    search = CustomSerpAPIWrapper()
    result = search.run(text)
    return result