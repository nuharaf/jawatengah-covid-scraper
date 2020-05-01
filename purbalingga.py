import requests
from bs4 import BeautifulSoup
import re
def scrape():
    text = requests.get("https://corona.purbalinggakab.go.id/").text
    soup = BeautifulSoup(text,'lxml')
    kv = dict()
    t = soup.find("li",string=re.compile(r"Selesai Pemantauan : \d+.\d+ Orang")).text
    kv["odp_selesai"] = int(re.search(r"(\d+.\d+)",t).group(0).replace(".",""))
    t = soup.find("li",string=re.compile(r"Dalam Pemantauan : \d+.\d+ Orang")).text
    kv["odp_pantau"] = int(re.search(r"(\d+.\d+)",t).group(0).replace(".",""))

    t = soup.find(string=re.compile(r"Negatif dan pulang")).parent.parent.text
    kv["pdp_pulang_neg"] = int(re.search(r"(\d+)",t).group(0))
    t = soup.find(string=re.compile(r"Menunggu Hasil Lab")).parent.parent.text
    kv['pdp_menunggu'] = re.search(r"(\d+)",t).group(0)
    t = soup.find(string=re.compile(r": \d+ Orang \(\d+ Negatif\)"))
    match = re.search(r": (\d+) Orang \((\d+) Negatif\)",t).groups()
    kv['pdp_meninggal'] = match[0]
    kv['pdp_meninggal_negatif'] = match[1]

    t = soup.find("strong",string=re.compile(r"Dirawat : \d+ Orang")).text
    kv['covid_dirawat'] = re.search(r"(\d+)",t).group(0)
    t = soup.find(string=re.compile(r"Sembuh"))
    kv['covid_sembuh'] = re.search(r"(\d+)",t).group(0)

    return text,kv