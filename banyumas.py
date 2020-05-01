import requests
import re
from bs4 import BeautifulSoup
def scrape():
    text = requests.get("http://covid19.banyumaskab.go.id").text
    soup = BeautifulSoup(text,'lxml')
    kv = dict()
    n = soup.find('span',string=re.compile("ODP"))
    kv["odp"] = int(n.text.split(" ")[1])
    n = n.parent.parent
    n = n.find_next_sibling()
    kv["odp_selesai"] = int((n.div.span.text).replace(",",""))
    n = n.find_next_sibling()
    kv["odp_total"] = int((n.div.span.text).replace(",",""))
    n = n.find_next_sibling()
    kv["pdp_dirawat"] = int((n.div.span.text.split(" ")[1]).replace(",",""))
    n = n.find_next_sibling()
    kv["pdp_negatif"] = int((n.div.span.text).replace(",",""))
    n = n.find_next_sibling()
    kv["pdp_tunggu"] = int((n.div.span.text).replace(",",""))
    n = n.find_next_sibling()
    kv["pdp_meninggal"] = int((n.div.span.text).replace(",",""))
    n = n.find_next_sibling()
    kv["pdp_total"] = int((n.div.span.text).replace(",",""))
    n = n.find_next_sibling()
    kv["covid"] = int((n.div.span.text.split(" ")[1]).replace(",",""))
    n = n.next_sibling.next_sibling
    kv["covid_dirawat"] = int((n.div.span.text).replace(",",""))
    n = n.find_next_sibling()
    kv["covid_sembuh"] = int((n.div.span.text).replace(",",""))
    n = n.find_next_sibling()
    kv["covid_meninggal"] = int((n.div.span.text).replace(",",""))
    return text,kv
