import requests
from bs4 import BeautifulSoup
def scrape():
    text = requests.get("https://corona.jepara.go.id/",timeout=10).text
    soup = BeautifulSoup(text,'lxml')
    data = soup.find('section',id='service')
    kv = dict()
    kv["odp_proses"] = int(data.find("p",string="ODP SAAT INI").find_next_sibling().text)
    kv["odp"] = int(data.find("p",string="TOTAL ODP").find_next_sibling().text)
    kv["odp_selesai"] = int(data.find("p",string="SELESAI PEMANTAUAN").find_next_sibling().text)

    kv["pdp"] = int(data.find("p",string="TOTAL PDP").find_next_sibling().text)
    kv["pdp_meninggal"] = int(data.find("p",string="PDP MENINGGAL").find_next_sibling().text)
    kv["pdp_proses"] = int(data.find("p",string="PDP SAAT INI").find_next_sibling().text)
    kv["pdp_sehat"] = int(data.find("p",string="SEHAT").find_next_sibling().text)

    kv["covid"] = int(data.find("p",string="POSITIF TOTAL").find_next_sibling().text)
    kv["covid_meninggal"] = int(data.find("p",string="MENINGGAL DUNIA").find_next_sibling().text)
    kv["covid_proses"] = int(data.find("p",string="POSITIF SAAT INI").find_next_sibling().text)
    kv["covid_sembuh"] = int(data.find("p",string="SEMBUH").find_next_sibling().text)

    return text,kv
    
