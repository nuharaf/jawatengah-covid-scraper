import requests
from bs4 import BeautifulSoup
import re

def scrape():
    text = requests.get("https://corona.semarangkab.go.id/").text
    soup = BeautifulSoup(text, 'lxml')
    kv = dict()
    odp = soup.find("div",string="ODP")
    kv["odp"] = int(odp.find_previous_sibling().text)
    l = re.findall(r"\d+",odp.parent.parent.find_next_sibling("div").text)
    kv["odp_selesai"] =l[1]
    kv["odp_total"] =l[2]

    pdp = soup.find("div",string="PDP")
    kv["pdp"] = int(pdp.find_previous_sibling().text)
    l = re.findall(r"\d+",pdp.parent.parent.find_next_sibling("div").text)
    kv["pdp_negatif"] =l[1]
    kv["pdp_dirawat"] =l[2]
    kv["pdp_meninggal"] =l[3]
    kv["pdp_total"] =l[4]

    covid = soup.find("div",string="COVID-19")
    kv["covid"] = int(covid.find_previous_sibling().text)
    l = re.findall(r"\d+",covid.parent.parent.find_next_sibling("div").text)
    kv["covid_dirawat"] =l[0]
    kv["covid_sembuh"] =l[1]
    kv["covid_meninggal"] =l[2]

    return text,kv