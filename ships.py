import requests
import re
import random
from bs4 import BeautifulSoup
from datetime import datetime

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
    if linetext.find("Queue") == -1:
        linetext = re.sub('/revision.*$', '', linetext)
        USS = line.next["alt"]
        #print(USS)
        linetext = linetext + "|" + USS
        imageURLs.append(linetext)

shipNumber = random.randint(0, len(imageURLs))
shipPieces = imageURLs[shipNumber].split("|")
shipURL = shipPieces[0]
shipName = shipPieces[1]

url = "https://usetrmnl.com/api/custom_plugins/" + PLUGIN_UUID
variables = {"merge_variables": {"shipURL": shipURL, "shipName": shipName }}
result = requests.post(url, json=variables)
