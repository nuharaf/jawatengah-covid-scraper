import requests
from bs4 import BeautifulSoup
def scrape():
    text = requests.get("https://covid19.boyolali.go.id/").text
    soup = BeautifulSoup(text,'lxml')
    kv = dict()
    covid = soup.find("h4",string="Positif")
    covids = covid.find_next_sibling().findChildren("span")
    kv["covid_kumulatif"] = int(covids[0].text)
    kv["covid_dirawat"] = int(covids[1].text)
    kv["covid_sembuh"] = int(covids[2].text)
    kv["covid_meninggal"] = int(covids[3].text)

    pp = soup.find("h4",string="PP")
    kv["pp_proses"] = int(pp.find_next_sibling("span").text)
    pps = pp.find_next_sibling("div").findChildren("span")
    kv["pp_kumulatif"] = int(pps[0].text)
    kv["pp_selesai"] = int(pps[1].text)

    odp = soup.find("h4",string="ODP")
    kv["odp_proses"] = int(odp.find_next_sibling("span").text)
    odps = odp.find_next_sibling("div").findChildren("span")
    kv["odp_kumulatif"] = int(odps[0].text)
    kv["odp_selesai"] = int(odps[1].text)

    pdp = soup.find("h4",string="PDP")
    kv["pdp_proses"] = int(pdp.find_next_sibling("span").text)
    pdps = pdp.find_next_sibling("div").findChildren("span")
    kv["pdp_kumulatif"] = int(pdps[0].text)
    kv["pdp_selesai"] = int(pdps[1].text)

    otg = soup.find("h4",string="OTG")
    kv["otg_proses"] = int(otg.find_next_sibling("span").text)
    otgs = otg.find_next_sibling("div").findChildren("span")
    kv["otg_kumulatif"] = int(otgs[0].text)
    kv["otg_selesai"] = int(otgs[1].text)

    return text,kv