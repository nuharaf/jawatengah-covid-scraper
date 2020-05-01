import requests
from bs4 import BeautifulSoup
def scrape():
    text = requests.get("http://corona.banjarnegarakab.go.id").text
    soup = BeautifulSoup(text,'lxml')
    data = soup.find('section',id='data')
    kv = dict()
    v = data.find('div',string="COVID Dirawat").find_previous_sibling().text
    kv["covid_dirawat"] = int(v)
    v = data.find('div',string="COVID Sembuh").find_previous_sibling().text
    kv["covid_sembuh"] = int(v)
    v = data.find('div',string="COVID Meninggal").find_previous_sibling().text
    kv["covid_meninggal"] = int(v)
    v = data.find('div',string="PDP Dirawat").find_previous_sibling().text
    kv["pdp_dirawat"] = int(v)
    v = data.find('div',string="PDP Sembuh").find_previous_sibling().text
    kv["pdp_sembuh"] = int(v)
    v = data.find('div',string="PDP Meninggal").find_previous_sibling().text
    kv["pdp_meninggal"] = int(v)
    v = data.find('div',string="ODP").find_previous_sibling().text
    kv["odp"] = int(v)
    v = data.find('div',string="OTG").find_previous_sibling().text
    kv["otg"] = int(v)
    return (text,kv)
    


