import requests
from bs4 import BeautifulSoup
import re

def scrape():
    text = requests.get("https://covid19.tegalkab.go.id/",verify=False).text
    soup = BeautifulSoup(text, 'lxml')
    kv = dict()
    covid = soup.find("strong",string="CONFIRM").findParent("center")
    kv["covid_total"] = int(covid.find_next_sibling("center").find_next_sibling("center").h4.text)
    l = covid.findParent("div").find_next_sibling("div").findChildren("span")
    kv["covid_sembuh"]  = int(l[0].text)
    kv["covid_dirawat"]  = int(l[1].text)
    kv["covid_meninggal"]  = int(l[2].text)

    pdp = soup.find("strong",string="PDP (Pasien Dalam Pengawasan)").findParent("center")
    kv["pdp_total"] = int(pdp.find_next_sibling("center").find_next_sibling("center").h4.text)
    l = pdp.findParent("div").find_next_sibling("div").findChildren("span")
    kv["pdp_sembuh"]  = int(l[0].text)
    kv["pdp_dirawat"]  = int(l[1].text)
    kv["pdp_meninggal"]  = int(l[2].text)

    odp = soup.find("strong",string="ODP (Orang Dalam Pantauan)").findParent("center")
    kv["odp_total"] = int(odp.find_next_sibling("center").find_next_sibling("center").h4.text)
    l = odp.findParent("div").find_next_sibling("div").findChildren("span")
    kv["odp_selesai"]  = int(l[0].text)
    kv["odp_pantau"]  = int(l[1].text)

    otg = soup.find("strong",string="OTG (Orang Tanpa Gejala)").findParent("center")
    kv["otg_total"] = int(otg.find_next_sibling("center").find_next_sibling("center").h4.text)
    l = otg.findParent("div").find_next_sibling("div").findChildren("span")
    kv["otg_selesai"]  = int(l[0].text)
    kv["otg_pantau"]  = int(l[1].text)

    pp = soup.find("strong",string="PP (Pelaku Perjalanan)").findParent("center")
    kv["pp_total"] = int(pp.find_next_sibling("center").find_next_sibling("center").h4.text.replace(".",""))
    l = pp.findParent("div").find_next_sibling("div").findChildren("span")
    kv["pp_selesai"]  = int(l[0].text.replace(".",""))
    kv["pp_pantau"]  = int(l[1].text.replace(".",""))

    return text,kv