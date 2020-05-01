import requests
from bs4 import BeautifulSoup
import re


def scrape():
    text = requests.get("https://infocorona.magelangkab.go.id/").text
    soup = BeautifulSoup(text, 'lxml')
    kv = dict()

    odp = soup.find(
        "div", id="diagrambarstatusodp39").parent.find_next_sibling("div")
    t = odp.find(string=re.compile("ODP")).parent.text.strip().split(" ")
    kv["odp_pantauan"] = int(t[1])

    pdp = soup.find(
        "div", id="diagrambarstatuspdp39").parent.find_next_sibling("div")
    t = pdp.find("th", string=re.compile(r"PDP \d+")
                 ).parent.text.strip().split(" ")
    kv["pdp_total"] = int(t[1])
    kv["pdp"] = int(
        pdp.find("p", string="PDP").find_previous_sibling().text.strip())
    kv["pdp_sembuh"] = int(pdp.find(
        "p", string="PDP Pulang Kondisi Membaik").find_previous_sibling().text.strip())
    kv["pdp_md"] = int(pdp.find(
        "p", string="PDP Meninggal Dunia").find_previous_sibling().text.strip())

    covid = soup.find(
        "div", id="diagrambarstatuskonfirmasi39").parent.find_next_sibling("div")
    t = covid.find("th", string=re.compile(r"Konfirmasi \d+")
                 ).parent.text.strip().split(" ")
    kv["covid_total"] = int(t[1])
    kv["covid_dirawat"] = int(
        covid.find("p", string="Konfirmasi (masih dirawat)").find_previous_sibling().text.strip())
    kv["covid_sembuh"] = int(covid.find(
        "p", string="Konfirmasi Sembuh").find_previous_sibling().text.strip())
    kv["covid_md"] = int(covid.find(
        "p", string="Konfirmasi Meninggal").find_previous_sibling().text.strip())

    return text,kv
