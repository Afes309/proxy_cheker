import requests
from bs4 import BeautifulSoup

url = 'https://free.proxy-sale.com/?proxy_page=2'

def get_col_url(url):
	r = requests.get(url)
	return r.text


def get_proxy(html):
	soup = BeautifulSoup(html, 'html.parser')
	tr_info = soup.find('div', {'class':'main__table-wrap'}).find_all('tr')

	for i in tr_info:
		ip = i.find('td', {'class':'ip'}).find('a').get_text()
		#print(ip.split(' ')[0].split('\t')[0])
		port = i.find('td', {'class':'ip'}).find_next_sibling('div')
		print(port)






get_proxy(get_col_url(url))