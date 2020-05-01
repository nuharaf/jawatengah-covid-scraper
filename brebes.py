import requests
from bs4 import BeautifulSoup
import re
def scrape():
    text = requests.get("http://www.corona.brebeskab.go.id/").text
    soup = BeautifulSoup(text,'lxml')
    kv = dict()
    v = soup.find_all("span",class_="info-box-number")
    l = v[0].text.strip().split("\n")
    c = re.compile("(\d+)")
    kv["odp_total"] = int(c.search(l[0]).group(0))
    kv["odp_pantau"] = int(c.search(l[1]).group(0))
    kv["odp_selesai"] = int(c.search(l[2]).group(0))
    kv["odp_meninggal"] = int(c.search(l[3]).group(0))
    l = v[1].text.strip().split("\n")
    kv["pdp_total"] = int(c.search(l[0]).group(0))
    kv["pdp_dirawat"] = int(c.search(l[1]).group(0))
    kv["pdp_pulang"] = int(c.search(l[2]).group(0))
    kv["pdp_meninggal"] = int(c.search(l[3]).group(0))
    l = v[2].text.strip().split("\n")
    kv["covid_total"] = int(c.search(l[0]).group(0))
    kv["covid_pantau"] = int(c.search(l[1]).group(0))
    kv["covid_selesai"] = int(c.search(l[2]).group(0))
    kv["covid_meninggal"] = int(c.search(l[3]).group(0))
    return text,kv
