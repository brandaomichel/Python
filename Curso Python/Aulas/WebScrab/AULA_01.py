import pandas as pd
import urllib3
from bs4 import BeautifulSoup

def faz_request(site):
  urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
  manager = urllib3.PoolManager()
  return manager.request('GET', site, headers={'User-Agent': 'Mozilla/5.0'})

def le_site(site):
  response = faz_request(site)
  return BeautifulSoup(response.data, 'html.parser')

bs = le_site('https://www.horariodebrasilia.org/')
tag_hora = bs.find('p', id='relogio')
tag_hora.text

tag_data = bs.find('h3', id='dia-topo')
tag_data.text