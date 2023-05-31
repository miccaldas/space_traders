"""
This module checks, in three minutes intervals, if the ship's hull is almost full.
If it's not it'll start the prospecting.py module, if it is, it'll start the
selling midule.
"""
import json
import os
from time import sleep

import requests
import snoop
from dotenv import load_dotenv
from extraction import start
from selling import sell_start
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

    response = requests.get(url, headers=headers)
    return response.json()


r = capacity_check({"method": "GET"})


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    with open("capacity.json", "w") as f:
        f.write(text)


jprint(r)


capacity = r["data"]["cargo"]["capacity"]
pp(capacity)
loot = r["data"]["cargo"]["units"]
pp(loot)
if capacity - loot > 4:
    start()
else:
    sell_start()
