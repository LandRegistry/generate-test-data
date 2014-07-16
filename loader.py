from data_generator import DataGenerator
import json
import requests

def loadTitle(title):
    print "Loading title: " + title.get('title_id')

    # I'm hardcoding the mint URL for the dev environment here for the moment.
    requests.post("http://localhost:8001/titles", data=json.dumps(title))


if __name__ == '__main__':
    raw_data = DataGenerator.loadJson()
    titles = map(DataGenerator.convertItem, raw_data)
    map(loadTitle, titles)