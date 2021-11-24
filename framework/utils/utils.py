import random
from pathlib import Path

import requests


def get_project_root() -> Path:
    """
    This method returns the path to the root of the project
    """
    return Path(__file__).parent.parent.parent


def get_random_word():
    """
    The method works through an api request.
    Receives a list of words and returns a random word.
    """
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    words = response.text.splitlines()
    return random.choice(words)


if __name__ == '__main__':
    print(get_random_word())
