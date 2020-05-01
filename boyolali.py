import requests
from bs4 import BeautifulSoup
def scrape():
    text = requests.get("https://covid19.boyolali.go.id/").text
    soup = BeautifulSoup(text,'lxml')
    kv = dict()
    v = soup.find('p',string="Proses pemantauan")
    kv["odp_proses"] = int(v.find_previous_sibling().text)
    kv["odp_kumulatif"] = int(v.find_next_sibling().div.span.text)
    kv["odp_selesai"] = int(v.find_next_sibling().div.find_next_sibling().span.text)
    v = soup.find('p',string="Proses pengawasan")
    kv["pdp_proses"] = int(v.find_previous_sibling().text)
    kv["pdp_kumulatif"] = int(v.find_next_sibling().div.span.text)
    kv["pdp_selesai"] = int(v.find_next_sibling().div.find_next_sibling().span.text)
    v = soup.find('p',string="Dirawat")
    kv["covid_dirawat"] = int(v.find_previous_sibling().text)
    kv["covid_kumulatif"] = int(v.find_next_sibling().div.span.text)
    kv["covid_sembuh"] = int(v.find_next_sibling().div.find_next_sibling().span.text)
    kv["covid_meninggal"] = int(v.find_next_sibling().div.find_next_sibling().find_next_sibling().span.text)
    return text,kv
    

