import requests
from src.config import ACCESS_TOKEN

def graph_get(url, params=None):
    if params is None:
        params = {}

    params["access_token"] = ACCESS_TOKEN

    response = requests.get(url, params=params, timeout=30)

    if response.status_code != 200:
        raise Exception(f"Erro {response.status_code}: {response.text}")

    return response.json()