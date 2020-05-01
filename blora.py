import requests
from bs4 import BeautifulSoup
url = r'https://docs.google.com/spreadsheets/d/e/2PACX-1vQ6Lo4uLOT8s72XkKo69u2SrRECDKEshtxzq3QN08DyGa6GwhH4JXe-H2CNbTXIgyJ2gNcZt6G3wxqG/pubhtml?gid=1895238016&single=true'
def scrape():
    text = requests.get(url).text
    soup = BeautifulSoup(text,'lxml')
    kv = dict()
    v = soup.find("td",string="TOTAL")
    v = v.find_next_sibling()
    kv["otg"] = int(v.text)
    v = v.find_next_sibling()
    kv["odp"] = int(v.text)
    v = v.find_next_sibling()
    kv["odp_selesai"] = int(v.text)
    v = v.find_next_sibling()
    kv["odp_proses"] = int(v.text)
    v = v.find_next_sibling()
    kv["pdp"] = int(v.text)
    v = v.find_next_sibling()
    kv["pdp_proses"] = int(v.text)
    v = v.find_next_sibling()
    kv["pdp_selesai"] = int(v.text)
    v = v.find_next_sibling()
    kv["pdp_meninggal"] = int(v.text)
    v = v.find_next_sibling()
    kv["covid"] = int(v.text)
    v = v.find_next_sibling()
    kv["covid_dirawat"] = int(v.text)
    v = v.find_next_sibling()
    kv["covid_sembuh"] = int(v.text)
    v = v.find_next_sibling()
    kv["covid_meninggal"] = int(v.text)
    return text,kv
