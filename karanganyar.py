import requests
from bs4 import BeautifulSoup
def scrape():
    text = requests.get("http://covid19.karanganyarkab.go.id/").text
    soup = BeautifulSoup(text,'lxml')
    d = soup.find('section',id='monitor')
    kv = dict()
    kv["odp_proses"] = int(d.find("h4",string="Orang Dalam Pemantauan (ODP)").find_next_sibling().text)
    kv["odp"] = int(d.find("td",string="Komulatif").find_next_sibling().text)
    kv["odp_selesai"] = int(d.find("td",string="Selesai Pemantauan").find_next_sibling().text)
    kv["odp_meninggal"] = int(d.find("td",string="Meninggal Dunia").find_next_sibling().text)

    kv["pdp_proses"] = int(d.find("h4",string="Orang Dalam Pemantauan (ODP)").find_next_sibling().text)
    kv["pdp"] = int(d.find("td",string="Komulatif").find_next_sibling().text)
    kv["pdp_selesai"] = int(d.find("td",string="Selesai Pemantauan").find_next_sibling().text)
    kv["pdp_meninggal"] = int(d.find("td",string="Meninggal Dunia").find_next_sibling().text)

    kv["covid_meninggal"] = int(d.find("tr",class_="cov-mati").findChild(class_="text-right").text)
    kv["covid_proses"] = int(d.find("tr",class_="cov-rawat").findChild(class_="text-right").text)
    kv["covid_sembuh"] = int(d.find("tr",class_="cov-sembuh").findChild(class_="text-right").text)

    return text,kv