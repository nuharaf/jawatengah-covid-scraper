import requests
from bs4 import BeautifulSoup
import re

def scrape():
    text = requests.get("http://corona.sukoharjokab.go.id/").text
    soup = BeautifulSoup(text, 'lxml')
    kv = dict()
    otg = soup.find("div",string="Orang Tanpa Gejala (OTG)").find_next_sibling("div")
    kv["otg_total"] = int(otg.p.text)
    l = otg.div.find_all("p")
    kv["otg_baru"] = int(l[0].text)
    kv["otg_lama"] = int(l[1].text)
    kv["otg_selesai"] = int(l[2].text)

    odp = soup.find("div",string="Orang Dalam Pemantauan (ODP)").find_next_sibling("div")
    kv["odp_total"] = int(odp.p.text)
    l = odp.div.find_all("p")
    kv["odp_selesai"] = int(l[0].text)
    kv["odp_isolasi"] = int(l[1].text)
    kv["odp_rawat"] = int(l[2].text)
    kv["odp_meninggal"] = int(l[3].text)

    pdp = soup.find("div",string="Pasien Dalam Pengawasan (PDP)").find_next_sibling("div")
    kv["pdp_total"] = int(pdp.p.text)
    l = pdp.div.find_all("p")
    kv["pdp_rawat"] = int(l[0].text)
    kv["pdp_isolasi"] = int(l[1].text)
    kv["pdp_negatif"] = int(l[2].text)
    kv["pdp_meninggal"] = int(l[3].text)

    covid = soup.find("div",string="Positif COVID-19").find_next_sibling("div")
    kv["covid_total"] = int(covid.p.text)
    l = covid.div.find_all("p")
    kv["covid_sembuh"] = int(l[0].text)
    kv["covid_isolasi"] = int(l[1].text)
    kv["covid_dirawat"] = int(l[2].text)
    kv["covid_meninggal"] = int(l[3].text)

    return text,kv