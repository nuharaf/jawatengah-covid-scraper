import requests
from bs4 import BeautifulSoup

def scrape():
    text = requests.get("http://corona.kendalkab.go.id/").text
    soup = BeautifulSoup(text,'lxml')
    kv = dict()
    covid = soup.find("h4",string="COVID-19").find_next_sibling("div")
    kv["covid_total"] = int(covid.findChild("h2").text)
    l = covid.find_next_sibling("div").findChildren("h2")
    kv["covid_sembuh"] = int(l[0].text)
    kv["covid_dirawat"] = int(l[1].text)
    kv["covid_isolasi"] = int(l[2].text)

    pdp = soup.find("h4",string="PDP").find_next_sibling("div")
    kv["pdp_total"] = int(pdp.findChild("h2").text)
    l = pdp.find_next_sibling("div").findChildren("h2")
    kv["pdp_sembuh"] = int(l[0].text)
    kv["pdp_isolasi"] = int(l[1].text)
    kv["pdp_dirujuk"] = int(l[2].text)
    kv["pdp_aps"] = int(l[3].text)
    kv["pdp_dirawat"] = int(l[4].text)
    kv["pdp_meninggal"] = int(l[5].text)

    odp = soup.find("h4",string="ODP").find_next_sibling("div")
    kv["odp_total"] = int(odp.findChild("h2").text)
    l = odp.find_next_sibling("div").findChildren("h2")
    kv["odp_selesai"] = int(l[0].text)
    kv["odp_pantau"] = int(l[1].text)

    ppdt = soup.find("h4",string="PPDT").find_next_sibling("div")
    kv["ppdt_total"] = int(ppdt.findChild("h2").text)
    l = ppdt.find_next_sibling("div").findChildren("h2")
    kv["ppdt_pantau"] = int(l[0].text)
    kv["ppdt_selesai"] = int(l[1].text)

    return text,kv