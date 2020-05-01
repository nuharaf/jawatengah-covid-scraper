import requests
from bs4 import BeautifulSoup
import re


def scrape():
    text = requests.get("http://corona.sragenkab.go.id/").text
    soup = BeautifulSoup(text, 'lxml')
    kv = dict()
    pp = soup.find("h3", string="Pelaku Perjalanan (PP)")
    kv["pp"] = int(pp.find_next_sibling("h2").text)
    pp = pp.parent.find_next_sibling("table")
    kv["pp_dn"] = int(pp.findChild(
        "td", string="Dalam Negeri").find_next_sibling().find_next_sibling().text)
    kv["pp_ln"] = int(pp.findChild(
        "td", string="Luar Negeri").find_next_sibling().find_next_sibling().text)
    kv["pp_selesai"] = int(pp.findChild(
        "td", string="Lolos 14 Hari").find_next_sibling().find_next_sibling().text)
    kv["pp_isolasi"] = int(pp.findChild(
        "td", string="PP Isolasi Mandiri").find_next_sibling().find_next_sibling().text)

    odp = soup.find("h3", string=re.compile(r" Total ODP"))
    kv["odp"] = int(odp.text.split("=")[1])
    l = odp.findParent("tr").find_next_sibling(
    ).find_next_sibling().findChildren("td")
    kv["odp_lama"] = int(l[0].text)
    kv["odp_baru"] = int(l[1].text)
    kv["odp_lolos"] = int(l[2].text)

    pdp = soup.find("h3", string=re.compile(r"Total PDP"))
    kv["pdp"] = int(pdp.text.split("=")[1])
    l = pdp.findParent("tr").find_next_sibling(
    ).find_next_sibling().findChildren("td")
    kv["pdp_rawat"] = int(l[0].text)
    kv["pdp_rujuk"] = int(l[1].text)
    kv["pdp_sembuh"] = int(l[2].text)
    kv["pdp_meninggal"] = int(l[3].text)

    covid = soup.find("h3", string=re.compile(r"Total Positif"))
    kv["covid"] = int(covid.text.split("=")[1])
    l = covid.findParent("tr").find_next_sibling(
    ).find_next_sibling().findChildren("td")
    kv["covid_rawat"] = int(l[0].text)
    kv["covid_rujuk"] = int(l[1].text)
    kv["covid_sembuh"] = int(l[2].text)
    kv["covid_meninggal"] = int(l[3].text)
    return text,kv
