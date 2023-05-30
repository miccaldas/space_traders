"""
This module checks  hourly if the ship's hull is almost full.
If it's not it'll start the prospecting.py module.
"""
import json
import os
from time import sleep

import requests
import requests_cache
import snoop
from dotenv import load_dotenv
from extraction import start
from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])

load_dotenv()


@snoop
def capacity_check(payload):
    """"""
    headers = {
        "Content-Type": "application/json",
        "Authorization": os.environ.get("SPACETOKEN"),
    }
    url = "https://api.spacetraders.io/v2/my/ships/MCLDS-2"

    payload["format"] = "json"
    response = requests.get(url, headers=headers, params=payload)
    return response


r = capacity_check({"method": "GET"})


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    with open("capacity.json", "w") as f:
        f.write(text)


jprint(r.json())

carga = r.json()
capacity = carga["data"]["cargo"]["capacity"]
pp(capacity)
loot = carga["data"]["cargo"]["units"]
pp(loot)
if capacity - loot > 3:
    start()
