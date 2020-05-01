import requests
import json
def scrape():
    data = requests.get("http://corona.grobogan.go.id/data.json").text
    j = json.loads(data)
    kv = dict()
    kv["odp"] = j["odp"]
    kv["pdp"] = j["pdp"]
    kv["covid"] = j["positif"]
    kv["meninggal"] = j["dead"]
    return data,kv