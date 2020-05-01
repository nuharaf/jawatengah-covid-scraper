import requests
from bs4 import BeautifulSoup
import re

def scrape():
    text = requests.get("http://covid19.purworejokab.go.id/").text
    soup = BeautifulSoup(text, 'lxml')
    kv = dict()
    t = soup.find("span",string=re.compile(r"ODP = \d+")).text
    kv["odp"] = int(re.search(r"(\d+)",t).group(0))
    kv["odp_pantau"] = int(soup.find("b",string="DALAM PEMANTAUAN ").parent.find_previous_sibling().text)
    kv["odp_selesai"] = int(soup.find("b",string="SELESAI PEMANTAUAN ").parent.find_previous_sibling().text)

    # t = soup.find("span",string=re.compile(r" OTG = \d+ ")).text
    # kv["otg"] = int(re.search(r"(\d+)",t).group(0))
    # kv["otg_rdt"] = int(soup.find("b",string=re.compile("RDT")).parent.find_previous_sibling().text)

    t = soup.find("span",string=re.compile(r" PDP =  \d+")).text
    kv["pdp"] = int(re.search(r"(\d+)",t).group(0))
    kv["pdp_negatif"] = int(soup.find("b",string="HASIL LAB NEGATIF ").parent.find_previous_sibling().text)
    kv["pdp_dirawat"] = int(soup.find("b",string="DIRAWAT ").parent.find_previous_sibling().text)
    kv["pdp_sembuh"] = int(soup.find("b",string="SEMBUH ").parent.find_previous_sibling().text)
    kv["pdp_meninggal"] = int(soup.find("b",string="MENINGGAL").parent.find_previous_sibling().text)

    t = soup.find("span",string=re.compile(r"  POSITIF COVID-19 =  \d+")).text
    kv["covid"] = int(re.search(r"(\d+)",t).group(0))
    kv["covid_dirawat"] = int(soup.find("b",string="DIRAWAT ").parent.find_previous_sibling().text)
    kv["covid_sembuh"] = int(soup.find("b",string="SEMBUH ").parent.find_previous_sibling().text)
    kv["covid_meninggal"] = int(soup.find("b",string=" MENINGGAL").parent.find_previous_sibling().text)
    
    return text,kv
    
