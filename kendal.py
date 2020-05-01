import requests
from bs4 import BeautifulSoup

def scrape():
    text = requests.get("http://corona.kendalkab.go.id/").text
    soup = BeautifulSoup(text,'lxml')
    kv = dict()
    kv["odp"] = int(soup.find("h4",string = "Total ODP").find_next_sibling("h2").text.strip())
    kv["otg"] = int(soup.find("h4",string = "OTG").find_next_sibling("h2").text.strip())
    kv["pdp_isolasi"] = int(soup.find("h4",string = "Total PDP (Isolasi)").find_next_sibling("h2").text.strip())
    kv["pdp_sembuh"] = int(soup.find("h4",string = "PDP Sembuh").find_next_sibling("h2").text.strip())
    kv["covid"] = int(soup.find("h4",string = "Positif Covid-19").find_next_sibling("h2").text.strip())
    kv["meninggal"] = int(soup.find("h4",string = "Meninggal").find_next_sibling("h2").text.strip())
    return text,kv