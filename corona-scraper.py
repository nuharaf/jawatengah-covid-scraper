from datetime import datetime
import importlib
import sys
import shelve

database = shelve.open("state.shelve")


def scrape(web, t):
    print(f'scraping {web}')
    m = importlib.import_module(web)
    html, kv = m.scrape()
    doc = open(f'snapshot/{t} {web}.html', "w")
    doc.write(html)
    doc.close()
    data = open(f'data/{web}.txt', "a")
    for k, v in kv.items():
        data.write(f'{t},{k},{v}\n')
    print(f'scraping {web} done')


if len(sys.argv) >= 2:
    m = sys.argv[1]
    t = datetime.now()
    scrape(m, t)
    database[m] = t
    exit(1)

weblist = ["banjarnegara", "banyumas", "batang", "brebes", "blora", "demak", "grobogan", "jepara",
           "karanganyar",  "kudus",   "kebumen", "klaten", "magelang", "pati", "pemalang", "pekalongan", "purworejo", "purbalingga", "semarang", "boyolali2", "kendal2"]

for web in weblist:
    t = datetime.now()
    doscrape = False
    if web not in database:
        doscrape = True
    elif (t - database[web]).seconds > 14400:
        doscrape = True
    if doscrape:
        scrape(web, t)
        database[web] = t
    else:
        print(f"skipping {web}")
