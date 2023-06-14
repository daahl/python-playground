import requests
from bs4 import BeautifulSoup as bs
import json

# fetch the webpage
URL = "https://www.nordpoolgroup.com/api/marketdata/page/29?currency=,SEK,SEK,EUR&endDate=09-08-2022"
page = requests.get(URL)

# parse the good stuff as html
siteSoup = bs(page.content, "html.parser")
siteJson = json.loads(siteSoup.text)
siteRows = siteJson['data']['Rows']

for v in siteRows:
    for i in v.values():
        for j in i:
            print(j)
            print("LINEBREAK")

#print(json.dumps(siteJson, indent=4))