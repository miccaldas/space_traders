"""
This module follows the capacity_check module, after it fills the inventory.
Here will dock our swhip and and sell our wares in the market.
"""
import json
import os
from time import sleep

import requests
import snoop
from dotenv import load_dotenv
from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])

load_dotenv()


@snoop
def prod_lst():
    """"""
    with open("capacity.json", "r") as f:
        fungibles = json.load(f)

    wares = fungibles["data"]["cargo"]["inventory"]
    products = []
    for i in wares:
        products.append((i["symbol"], i["units"]))

    return products


@snoop
def dock():
    """"""
    headers = {
        "Content-Type": "application/json",
        "Authorization": os.environ.get("SPACETOKEN"),
    }
    url = "https://api.spacetraders.io/v2/my/ships/MCLDS-2/dock"

    response = requests.post(url, headers=headers)
    print(response)


@snoop
def selling(symbol, units):
    """"""

    headers = {
        "Content-Type": "application/json",
        "Authorization": os.environ.get("SPACETOKEN"),
    }
    url = "https://api.spacetraders.io/v2/my/ships/MCLDS-2/sell"

    payload = {}
    payload["symbol"] = symbol
    payload["units"] = units
    response = requests.post(url, headers=headers, json=payload)
    # return response
    print(response.json())


@snoop
def start():
    """"""
    products = prod_lst()
    # dock()

    # for i in range(len(products)):
    selling("SILVER_ORE", 5)


if __name__ == "__main__":
    start()
