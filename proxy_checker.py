import requests
from bs4 import BeautifulSoup
import time




def get_info(html):
	soup = BeautifulSoup(html, 'html.parser')
	ip = soup.find('big',attrs={'id': 'd_clip_button'}).get_text()
	town = soup.find('a', attrs = {'href':'/geoip/'}).find_parent().get_text()
	print(ip)
	print(town)
	



def chek_proxi(proxi,url):
	good_proxi = []
	for i in proxi:
		proxies = {'http': 'http://'+str(i.strip()),'https': 'http://'+str(i.strip())}
		headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'}
		#print(proxies)

		try:
			date_before = time.clock()
			r = requests.get(url,proxies=proxies, headers = headers,timeout=1)
			if r.status_code == requests.codes.ok:
				get_info(r.text)
				good_proxi.append(i.strip())
				date_after = time.clock() - date_before
				print(i.strip())
				print(date_after)
		except:
			print('error')

	print(good_proxi) 




if __name__ == '__main__':
	url = 'https://2ip.ru/'
	proxi = open('test_1.txt', 'r')
	chek_proxi(proxi,url)
	
	#headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	#r = requests.get('https://2ip.ru/', headers = headers)
	#get_info(r.text)
		
