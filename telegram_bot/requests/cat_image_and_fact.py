import requests


def get_cat_photo_url():
    cat_request = requests.get("https://cataas.com/cat?json=true")
    cat_json = cat_request.json()
    cat_image_url = cat_json["url"]
    return "https://cataas.com" + cat_image_url


def get_cat_fact():
    cat_request = requests.get("https://catfact.ninja/fact")
    cat_json = cat_request.json()
    cat_fact = cat_json["fact"]
    return cat_fact
