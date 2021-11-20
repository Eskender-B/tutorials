from bs4 import BeautifulSoup
import requests
import sys
title_list = []
for i in range(50):
	print(f"page {i+1}")
	resp = requests.get(f"https://books.toscrape.com/catalogue/page-{i+1}.html")
	if resp.status_code != 200:
		sys.exit('could not open url')
		

	html_doc = resp.content.decode()

	soup = BeautifulSoup(html_doc, 'html.parser')

	ol_res = soup.find_all("ol", class_="row")[0]
	ls_res = ol_res.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")


	for l in ls_res:
		#print('Title:', l.find('img').get('alt'))
		title_list.append(l.find('img').get('alt'))

with open('title_list.txt', 'w') as f:
	f.write('\n'.join(title_list))
		
