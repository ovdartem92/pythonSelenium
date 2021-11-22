from pathlib import Path
import random
import requests


def get_project_root() -> Path:
    return Path(__file__).parent.parent.parent


def get_random_world():
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    words = response.content.splitlines()
    return random.choice(words)


if __name__ == '__main__':
    print(get_random_world())
