import sys
import requests
from typing import Final, Dict, List
from requests import Response
import json
from datetime import datetime

now = datetime.now()
EXCLUDE: Final[List[str]] = ["ruby", "jekyll-github-metadata", "github-pages", "github-pages-health-check"]
DATETIME_FORMATEE: Final[str] = now.strftime("%Y-%m-%d")

def generate_gemfile(specifications: Dict[str, str]):
    plugins: List[str] = []
    deps: List[str] = []

    for gem, version in specifications.items():
        if gem in EXCLUDE:
            continue
        if gem.startswith('jekyll-'):
            plugins.append("gem '{}', '{}'".format(gem, version))
        else:
            deps.append("gem '{}', '{}'".format(gem, version))

    print("# Date: {}".format(DATETIME_FORMATEE))
    print("source 'https://rubygems.org'\n")
    print("{}\n\n".format("\n".join(deps)))
    print("group :jekyll_plugins do")
    print("{}".format("\n".join(map(lambda x: "  {}".format(x), plugins))))
    print("end\n")
    print("gem 'webrick'")
    print("gem 'rexml'")

# Fetch the GitHub dependencies
URL: Final[str] = 'https://pages.github.com/versions.json'
response: Final[Response] = requests.get(URL)
if response.status_code != 200:
    print("ERROR: cannot fetch {}".format(URL))
    exit(1)
data: Dict[str, str] = json.loads(response.text)

# Generate the required instructions
generate_gemfile(data)
