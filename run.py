from bs4 import BeautifulSoup
import requests, json

r = requests.get('https://covid19.saglik.gov.tr/TR-66935/genel-koronavirus-tablosu.html')
soup = BeautifulSoup(r.text, 'html.parser')

script = soup.find_all("script",attrs={"type":"text/javascript"})
say = 0

dosya = open("pythonassets/jsonfull.txt", "w")
dosya.write(str(script[8]))
dosya.close()