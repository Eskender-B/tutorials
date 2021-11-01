from bs4 import BeautifulSoup
import requests
import sys
import time

# Get the link of states from the ff URL
base_site = 'https://www.4icu.org/us/universities/'
resp = requests.get(base_site)
if resp.status_code != 200:
    sys.exit("Status Code != 200")

html_doc = resp.content.decode()

soup = BeautifulSoup(html_doc, 'html.parser')
table = soup.find_all('table', attrs={'class':'table'})[0]
state_links = table.find_all('a')


# For each state link, open link and retrieve universities in that state
universities = []

for i, link in enumerate(state_links):
    time.sleep(0.1)
    print(i, link.string)
    resp = requests.get('https://www.4icu.org/'+link.get('href'))
    if resp.status_code != 200:
        continue
    html_doc = resp.content.decode()
    soup = BeautifulSoup(html_doc, 'html.parser')

    table = soup.find_all('table', attrs={'class': 'table table-hover'})[0]
    univ_links = table.find('tbody').find_all('a')
    universities.extend([u.string for u in univ_links])



print(f'Found {len(universities)} universities in the US')
with open('university_list.txt', 'w') as f:
    f.write('\n'.join(universities))









