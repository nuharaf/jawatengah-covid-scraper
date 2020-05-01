import requests
from bs4 import BeautifulSoup

def num(str):
    return int(str.replace(".",""))
  

def scrape():
    text = requests.get("https://corona.kebumenkab.go.id").text
    soup = BeautifulSoup(text,'lxml')
    kv = dict()
    odp = soup.find("h5",string="Orang Dalam Pemantauan (ODP)")
    kv["odp_total"] = num(odp.find_next_sibling("h2").text.strip())
    kv["odp_proses"] = num(odp.parent.findChild("span",string="Proses Pemantauan").parent.find_previous_sibling("h2").text.strip())
    kv["odp_selesai"] = num(odp.parent.findChild("span",string="Selesai Pemantauan").parent.find_previous_sibling("h2").text.strip())

    pdp = soup.find("h5",string="Pasien Dalam Pengawasan (PDP)")
    kv["pdp_total"] = num(pdp.find_next_sibling("h2").text.strip())
    kv["pdp_proses"] = num(pdp.parent.findChild("span",string="Pengawasan").parent.find_previous_sibling("h2").text.strip())
    kv["pdp_meninggal"] = num(pdp.parent.findChild("span",string="Meninggal Tanpa Hasil Lab").parent.find_previous_sibling("h2").text.strip())
    kv["pdp_selesai"] = num(pdp.parent.findChild("span",string="Selesai Pengawasan").parent.find_previous_sibling("h2").text.strip())
    kv["pdp_negatif"] = num(pdp.parent.findChild("span",string="Negatif").parent.find_previous_sibling("h2").text.strip())

    covid = soup.find("h5",string="Positif")
    kv["covid_total"] = num(covid.find_next_sibling("h2").text.strip())
    kv["covid_proses"] = num(covid.parent.findChild("span",string="Dirawat").parent.find_previous_sibling("h2").text.strip())
    kv["covid_sembuh"] = num(covid.parent.findChild("span",string="Sembuh").parent.find_previous_sibling("h2").text.strip())
    kv["covid_meninggal"] = num(covid.parent.findChild("span",string="Meninggal").parent.find_previous_sibling("h2").text.strip())

    return text,kv
    