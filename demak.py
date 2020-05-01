import requests
import json
def scrape():
    data = requests.get("https://corona.demakkab.go.id/api/publik").text
    j = json.loads(data)
    kv = dict()
    kv["odp"] = j["data"][2]["jumlah"]
    kv["odp_proses"] = j["data"][2]["data"][0]["jumlah"]
    kv["odp_selesai"] = j["data"][2]["data"][1]["jumlah"]
    kv["pdp"] = j["data"][1]["jumlah"]
    kv["pdp_pantau"] = j["data"][1]["data"][0]["jumlah"]
    kv["pdp_meninggal"] = j["data"][1]["data"][1]["jumlah"]
    kv["pdp_selesai"] = j["data"][1]["data"][2]["jumlah"]
    kv["pdp_negatif"] = j["data"][1]["data"][3]["jumlah"]
    kv["covid"] = j["data"][0]["jumlah"]
    kv["covid_dirawat"] = j["data"][0]["data"][0]["jumlah"]
    kv["covid_sembuh"] = j["data"][0]["data"][1]["jumlah"]
    kv["covid_meninggal"] = j["data"][0]["data"][2]["jumlah"]
    return data,kv