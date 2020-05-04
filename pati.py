import requests
from bs4 import BeautifulSoup
def scrape():
    text = requests.get("https://covid19.patikab.go.id/v2/",timeout=10).text
    soup = BeautifulSoup(text,'lxml')
    kv = dict()
    pdp = soup.find("th",string="Total PDP").findParent("table")
    pdp = pdp.find("h6",string="Total").findParent("tr").td.find_next_sibling()
    kv["pdp_total"] = int(pdp.text)
    pdp = pdp.find_next_sibling()
    kv["pdp_sembuh_neg"] = int(pdp.text)
    pdp = pdp.find_next_sibling()
    kv["pdp_sembuh_pos"] = int(pdp.text)
    pdp = pdp.find_next_sibling()
    kv["pdp_pos"] = int(pdp.text)
    pdp = pdp.find_next_sibling()
    kv["pdp"] = int(pdp.text)
    pdp = pdp.find_next_sibling()
    kv["pdp_meninggal"] = int(pdp.text)

    odp = soup.find("th",string="Total ODP").findParent("table")
    odp = odp.find("h6",string="Total").findParent("tr").td.find_next_sibling()
    kv["odp_total"] = int(odp.text)
    odp = odp.find_next_sibling()
    kv["odp_selesai"] = int(odp.text)
    odp = odp.find_next_sibling()
    kv["odp"] = int(odp.text)

    return text,kv