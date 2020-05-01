import requests
import json
def scrape():
    data = requests.get("https://corona.batangkab.go.id/api/getData").text
    j = json.loads(data)
    kv = dict()
    kv["odp_pantau"] = j["odp"]["dipantau"]
    kv["odp_selesai"] = j["odp"]["selesai"]
    kv["pdp_dirawat"] = j["pdp"]["dirawat"]
    kv["pdp_selesai"] = j["pdp"]["selesai"]
    kv["pdp_sembuh"] = j["pdp"]["sembuh"]
    kv["pdp_meninggal"] = j["pdp"]["meninggal"]
    kv["covid_dirawat"] = j["positif"]["dirawat"]
    kv["covid_sembuh"] = j["positif"]["sembuh"]
    kv["covid_meninggal"] = j["positif"]["meninggal"]
    return data,kv
