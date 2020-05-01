import requests
from bs4 import BeautifulSoup

def zero(str):
    if len(str) ==0:
        return 0
    else:
        return int(str)

def scrape():
    text = requests.get("https://corona.kuduskab.go.id/").text
    soup = BeautifulSoup(text,'lxml')
    kv = dict()
    v = soup.find("section",id = "monitoring")
    otg = v.find("h3",string="OTG").parent.find_next_sibling("table")
    kv["otg_pantau"] = int(otg.findChild("th",string="Masih Dipantau").find_next_sibling().text)
    kv["otg_selesai"] = zero(otg.findChild("th",string="Selesai Dipantau").find_next_sibling().text)

    odp = v.find("h3",string="ODP").parent.find_next_sibling("table")
    kv["odp_pantau"] = int(odp.findChild("th",string="Masih Dipantau").find_next_sibling().text)
    kv["odp_selesai"] = zero(odp.findChild("th",string="Selesai Dipantau").find_next_sibling().text)

    pdp = v.find("h3",string="PDP").parent.find_next_sibling("table")
    kv["pdp_negatif"] = int(pdp.findChild("th",string="Negatif").find_next_sibling().text)
    kv["pdp_positif"] = zero(pdp.findChild("th",string="Total Positif").find_next_sibling().text)
    kv["pdp_sehat"] = int(pdp.findChild("th",string="Pulang Sehat").find_next_sibling().text)
    kv["pdp_dirawat"] = zero(pdp.findChild("th",string="Dalam Perawatan").find_next_sibling().text)
    kv["pdp_dirujuk"] = int(pdp.findChild("th",string="Dirujuk").find_next_sibling().text)
    kv["pdp_meninggal"] = zero(pdp.findChild("th",string="Meninggal").find_next_sibling().text)

    covid = v.find("h3",string="POSITIF").parent.find_next_sibling("table")
    dirawat = covid.findChild("th",string="Dirawat")
    kv["covid_dirawat_dalam"] = zero(dirawat.find_next_sibling().text)
    kv["covid_dirawat_luar"] = zero(dirawat.find_next_sibling().find_next_sibling().text)

    sembuh = covid.findChild("th",string="Sembuh")
    kv["covid_sembuh_dalam"] = zero(sembuh.find_next_sibling().text)
    kv["covid_sembuh_luar"] = zero(sembuh.find_next_sibling().find_next_sibling().text)

    meninggal = covid.findChild("th",string="Meninggal")
    kv["covid_meninggal_dalam"] = zero(meninggal.find_next_sibling().text)
    kv["covid_meninggal_luar"] = zero(meninggal.find_next_sibling().find_next_sibling().text)

    return text,kv


