import requests
from bs4 import BeautifulSoup
def scrape():
    text = requests.get("https://infocorona.pemalangkab.go.id/data").text
    soup = BeautifulSoup(text,'lxml')
    kv = dict()
    odp = soup.find("th",string="Pemantauan").parent.parent.findChild("td",string="1")
    odp = odp.find_next_sibling().find_next_sibling()
    kv["odp_pantau"] = int(odp.text)
    odp = odp.find_next_sibling()
    kv["odp_selesai"] = int(odp.text)
    odp = odp.find_next_sibling()
    kv["odp_jumlah"] = int(odp.text)

    pdp = soup.find("th",string="Pengawasan").parent.parent.findChild("td",string="1")
    pdp = pdp.find_next_sibling().find_next_sibling()
    kv["pdp_pengawasan"] = int(pdp.text)
    pdp = pdp.find_next_sibling()
    kv["pdp_selesai"] = int(pdp.text)
    pdp = pdp.find_next_sibling()
    kv["pdp_meninggal"] = int(pdp.text)
    pdp = pdp.find_next_sibling()
    kv["pdp_jumlah"] = int(pdp.text)

    covid = soup.find("th",string="Dirawat").parent.parent.findChild("td",string="1")
    covid = covid.find_next_sibling().find_next_sibling()
    kv["covid_dirawat"] = int(covid.text)
    covid = covid.find_next_sibling()
    kv["covid_sembuh"] = int(covid.text)
    covid = covid.find_next_sibling()
    kv["covid_meninggal"] = int(covid.text)
    covid = covid.find_next_sibling()
    kv["covid_jumlah"] = int(covid.text)

    
    return text,kv
