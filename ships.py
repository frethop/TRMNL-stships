import requests
import re
import random
from bs4 import BeautifulSoup
from datetime import datetime
#from PIL import Image, ImageEnhance

PLUGIN_UUID = "68eefdd3-c546-4542-aa2a-8f93ec1adedd"

random.seed()

# Start by fetching onthisday page
URL = "https://sto.fandom.com/wiki/List_of_canon_starships"
page = requests.get(URL)

# Parse the page with BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")
lines = soup.find_all("a", class_="image")
#print(lines)

imageURLs = []
for line in lines:
    linetext = line.attrs["href"]
    linetext = re.sub('/revision.*$', '', linetext)
    # USS = line.attrs["alt"]
    # linetext = linetext + "|" + USS
    imageURLs.append(linetext)
    print(linetext)

shipNumber = random.randint(0, len(imageURLs))
shipURL = imageURLs[shipNumber]

url = "https://usetrmnl.com/api/custom_plugins/" + PLUGIN_UUID
variables = {"merge_variables": {"shipURL": shipURL }}
result = requests.post(url, json=variables)
