import requests


def get_weather(city=None):
    response = requests.get(
        "https://wttr.in/{}".format(city or ""),
        params={
            "nmMTqu": "",
            "lang": "ru",
        }
    )
    if response.status_code != requests.codes.ok:
        return "Something went wrong"
    return response.text


if __name__ == "__main__":
    for city in ["Лондон", "Шереметьево", "Череповц"]:
        print(get_weather(city))
