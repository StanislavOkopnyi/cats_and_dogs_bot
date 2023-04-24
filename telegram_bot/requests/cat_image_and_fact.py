import requests


async def get_cat_photo_url():
    cat_request = requests.get("https://api.thecatapi.com/v1/images/search")
    cat_json = cat_request.json()
    cat_image_url = cat_json[0]["url"]
    return cat_image_url


async def get_cat_fact():
    cat_request = requests.get("https://catfact.ninja/fact")
    cat_json = cat_request.json()
    cat_fact = cat_json["fact"]
    return cat_fact
