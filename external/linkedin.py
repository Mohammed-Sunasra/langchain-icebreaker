import os
import requests


def scrape_linkedin_profile(linkedin_profile_url):
    """
    Scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile
    """
    #response = requests.get("https://gist.githubusercontent.com/paul-villalobos/c59167135dea9081021d53b2faebad66/raw/88ec8ce557de26be827cd29a617dceee3eb9306d/eden-marco.json")
    
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
