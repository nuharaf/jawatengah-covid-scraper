import requests
from bs4 import BeautifulSoup
def scrape():
    text = requests.get("http://corona.pekalongankab.go.id/").text
    soup = BeautifulSoup(text,'lxml')
    kv = dict()

    odp = soup.find("h3",string="ODP").find_next_sibling("div").findChild("h3")
    kv["odp_total"] = int(odp.text)
    odp = odp.find_next_sibling("div").find_all("div")
    kv["odp_pantau"] = int(odp[0].h3.text)
    kv["odp_selesai"] = int(odp[1].h3.text)
    kv["odp_meninggal"] = int(odp[2].h3.text)

    pdp = soup.find("h3",string="PDP").find_next_sibling("div").findChild("h3")
    kv["pdp_total"] = int(pdp.text)
    pdp = pdp.find_next_sibling("div").find_all("div")
    kv["pdp_dirawat"] = int(pdp[0].h3.text)
    kv["pdp_pulang"] = int(pdp[1].h3.text)
    kv["pdp_meninggal"] = int(pdp[2].h3.text)

    cvd = soup.find("h3",string="Positif").find_next_sibling("div").findChild("h3")
    kv["covid"] = int(cvd.text)
    cvd = cvd.find_next_siblings("div")
    row = cvd[0].find_all("div")
    kv["covid_dirawat"] = int(row[0].h3.text)
    kv["covid_sembuh"] = int(row[1].h3.text)
    kv["covid_meninggal"] = int(row[2].h3.text)
    kv["covid_isolasi_mandiri"] = int(cvd[1].h3.text)
    return text,kv