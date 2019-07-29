import csv
import urllib.request
import numpy as np
from bs4 import BeautifulSoup as bs

def getDataDecebal():
    data_to_write = []
    url = urllib.request.urlopen('https://www.trafic-web.ro/index.php?statie=863&plecari_din_statia_Piata_Decebal_Brasov')
    data = url.read()
    file = open('./dataset/bus_data_decebal.data', 'w')
    parsed = bs(data, 'html.parser')
    for tr in parsed.find_all('tr'):
        tds = tr.find_all('td')
        if 'Livada' in tds[1].text:
            data_to_write.append([tds[0].text, tds[1].text, tds[2].text])
        if 'Stadionul' in tds[1].text:
            data_to_write.append([tds[0].text, tds[1].text, tds[2].text])
        if 'Triaj' in tds[1].text:
            data_to_write.append([tds[0].text, tds[1].text, tds[2].text])
        if 'Rulmentul' in tds[1].text:
            data_to_write.append([tds[0].text, tds[1].text, tds[2].text])
        if 'Gara' in tds[1].text:
            data_to_write.append([tds[0].text, tds[1].text, tds[2].text])
    array_data = np.array(data_to_write)
    writer = csv.writer(file)
    writer.writerows(array_data)
    file.close()
    return array_data

def getDataJudetean():
    data_to_write = []
    url = urllib.request.urlopen('https://www.trafic-web.ro/index.php?statie=48&plecari_din_statia_Spitalul_Judetean_Brasov')
    data = url.read()
    file = open('./dataset/bus_data_judetean.data', 'w')
    parsed = bs(data, 'html.parser')
    for tr in parsed.find_all('tr'):
        tds = tr.find_all('td')
        if 'Livada' in tds[1].text:
            data_to_write.append([tds[0].text, tds[1].text, tds[2].text])
        if 'Stadionul' in tds[1].text:
            data_to_write.append([tds[0].text, tds[1].text, tds[2].text])
        if 'Rulmentul' in tds[1].text:
            data_to_write.append([tds[0].text, tds[1].text, tds[2].text])
        if 'Gara' in tds[1].text:
            data_to_write.append([tds[0].text, tds[1].text, tds[2].text])
    array_data = np.array(data_to_write)
    writer = csv.writer(file)
    writer.writerows(array_data)
    file.close()
    return array_data
