import requests
from bs4 import BeautifulSoup
import re

def scrape():
    text = requests.get("http://corona.sragenkab.go.id/").text
    soup = BeautifulSoup(text, 'lxml')