import json
import requests
from typing import List, Dict


def get_config(key):
    """
    Fetches the value of a given configuration key from a JSON file.

    :param key: The key for which the value is to be fetched.
    :return: The value of the specified key from the JSON file, or None if the key does not exist.
    """
    try:
        # Open the JSON file and load the data
        with open("config.json", 'r') as file:
            config_data = json.load(file)

        # Return the value associated with the key
        return config_data.get(key)
    except FileNotFoundError:
        # The JSON file was not found
        print("Config file not found.")
        return None
    except json.JSONDecodeError:
        # The JSON file is not properly formatted
        print("Error decoding JSON.")
        return None


def chat(model: str, messages: List) -> Dict:
    data = {
        "model": model,
        "messages": messages
    }
    print(data)
    url = get_config("OPENAI_API_URL")
    response = requests.post(url, data=json.dumps(data))
    response = response.json()["choices"][0]["message"]
    return response


if __name__ == "__main__":
    print(chat(model="gpt-4-1106-preview", messages=[{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Who won the world series in 2020?'}]))
