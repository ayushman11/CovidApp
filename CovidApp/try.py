import requests
text= requests.get('https://www.worldometers.info/coronavirus/').text

from bs4 import BeautifulSoup
html_text= text
soup= BeautifulSoup(html_text, 'html.parser')
data= soup.find_all('div', {'id': 'maincounter-wrap'})
world_info=[]

for x in data:
    world_info.append(int(x.div.span.text.replace(',','')))

world_info.insert(1,world_info[0]-world_info[2])

for i in range(4):
    world_info[i]='{:,}'.format(world_info[i])
