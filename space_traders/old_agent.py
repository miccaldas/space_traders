"""
Module Docstring
"""
import json

# from configs.config import Efs, tput_config
import os

import requests
import snoop

# import subprocess
from dotenv import load_dotenv
from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])

load_dotenv()


@snoop
def test(payload):
    """"""
    headers = {
        "Content-Type": "application/json",
        "Authorization": os.environ.get("SPACETOKEN"),
    }
    url = "https://api.spacetraders.io/v2/my/agent"

    response = requests.get(url, headers=headers)
    return response


r = test({"method": "POST"})

r.status_code


# def jprint(obj):
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)


# jprint(r.json())
