"""
Extracts ore until the hull is almost full.
"""
import json
import os
from time import sleep

import requests
import snoop
from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def orbit():
    """
    First you have to orbit the asteroid field.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": os.environ.get("SPACETOKEN"),
    }
    url = "https://api.spacetraders.io/v2/my/ships/MCLDS-2/orbit"

    response = requests.post(url, headers=headers)
    print(response.json())


@snoop
def extraction():
    """
    Function will be called by capacity_checker module,
    to mine until it has almost the hull full.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": os.environ.get("SPACETOKEN"),
    }
    url = "https://api.spacetraders.io/v2/my/ships/MCLDS-2/extract"

    response = requests.post(url, headers=headers)
    print(response.json())


@snoop
def start():
    """
    Initiates the former functions.
    """
    orbit()
    sleep(1)
    extraction()


if __name__ == "__main__":
    start()
