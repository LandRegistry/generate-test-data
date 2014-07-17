from data_generator import DataGenerator
import json
import requests
import sys

def loadTitle(title):
    print "Loading title: " + title.get('title_number')

    headers = { "Content-Type" : "application/json"}
    # I'm hardcoding the mint URL for the dev environment here for the moment.
    requests.post("http://localhost:8001/titles", data=json.dumps(title), headers=headers)


if __name__ == '__main__':
    quantity = 'all'
    if len(sys.argv) > 1:
        quantity = sys.argv[1]

    raw_data = DataGenerator.loadJson()
    if quantity.isdigit():
        n = int(quantity)
        if n <= len(raw_data):
            raw_data = raw_data[:n]

    print "Loading", len(raw_data), "titles"
    titles = map(DataGenerator.convertItem, raw_data)
    map(loadTitle, titles)
    print "Done loading", len(titles), "titles"
    
