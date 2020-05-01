import requests
from bs4 import BeautifulSoup
import re
def scrape():
    text = requests.get("https://awasicorona.klatenkab.go.id/",verify=False).text
    soup = BeautifulSoup(text,'lxml')
    kv = dict()
    odp = soup.find("h2",string="Orang Dalam Pantauan (ODP)")
    kv["odp"] = int(odp.find_next_sibling().text.strip())
    odp = odp.parent.parent.find_next_sibling().find_all("b")
    kv["odp_kumulatif"] = int(odp[1].string.strip())
    kv["odp_selesai"] = int(odp[2].string.strip())

    otg = soup.find("h2",string="Orang Tanpa Gejala (OTG)")
    kv["otg"] = int(otg.find_next_sibling().text.strip())
    otg = otg.parent.parent.find_next_sibling().find_all("b")
    kv["otg_kumulatif"] = int(otg[1].string.strip())
    kv["otg_selesai"] = int(otg[2].string.strip())

    pdp = soup.find("h2",string="Pasien Dalam Pengawasan (PDP)")
    kv["pdp"] = int(pdp.find_next_sibling().text.strip())
    pdp = pdp.parent.parent.find_next_sibling().find_all("b")
    kv["pdp_md_neg"] = int(pdp[1].string.strip())
    kv["pdp_md_menunggu"] = int(pdp[2].string.strip())
    kv["pdp_md_tanpa"] = int(pdp[3].string.strip())
    kv["pdp_menunggu"] = int(pdp[4].string.strip())
    kv["pdp_odp"] = int(pdp[5].string.strip())
    kv["pdp_kumulatif"] = int(pdp[6].string.strip())

    covid = soup.find(string=re.compile("Positif ")).find_parent()
    kv["covid"] = int(covid.find_next_sibling().text.strip())
    covid = covid.parent.parent.find_next_sibling().find_all("b")
    kv["covid_kumulatif"] = int(covid[0].string.strip())

    covid = soup.find(string=re.compile("Sembuh ")).find_parent()
    kv["covid_sembuh"] = int(covid.find_next_sibling().text.strip())
    return text,kv


