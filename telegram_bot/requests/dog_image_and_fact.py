import requests


def get_dog_photo_url() -> str:
    dog_request = requests.get("https://dog.ceo/api/breeds/image/random")
    dog_json = dog_request.json()
    dog_photo_url = dog_json["message"]
    return dog_photo_url


def get_dog_fact() -> str:
    dog_request = requests.get("https://dogapi.dog/api/v2/facts")
    dog_json = dog_request.json()
    dog_fact = dog_json["data"][0]["attributes"]["body"]
    return dog_fact
