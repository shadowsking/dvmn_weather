import argparse

import requests


class WeatherException(Exception):
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        if self.message:
            return self.message

        return "Something went wrong"


def get_weather(city=None):
    response = requests.get(
        "https://wttr.in/{}".format(city or ""),
        params={
            "nmMTqu": "",
            "lang": "ru",
        }
    )
    if not response.ok:
        raise WeatherException(response.text)

    return response.text


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        "--name",
        help="name locations",
        default="Лондон Шереметьево Череповец",
    )
    args = parser.parse_args()
    for city in args.name.split():
        print(get_weather(city))
