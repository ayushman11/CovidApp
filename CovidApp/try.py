import requests
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
LANGUAGE = "en-US,en;q=0.5"
session = requests.Session()
session.headers['User-Agent'] = USER_AGENT
session.headers['Accept-Language'] = LANGUAGE
session.headers['Content-Language'] = LANGUAGE
text= session.get('https://www.mygov.in/corona-data/covid19-statewise-status/').text

from bs4 import BeautifulSoup
html_text= text
soup= BeautifulSoup(html_text, 'html5lib')
state= []
confirmed= []
cured= []
death= []
data= []

rows= soup.find_all('div', {'class': 'content'})

for row in rows:

    rows_state= soup.find_all('div', {'class': 'field field-name-field-select-state field-type-list-text field-label-above'})
    rows_confirmed= soup.find_all('div', {'class': 'field field-name-field-total-confirmed-indians field-type-number-integer field-label-above'})
    rows_cured= soup.find_all('div', {'class': 'field field-name-field-cured field-type-number-integer field-label-above'})
    rows_death= soup.find_all('div', {'class': 'field field-name-field-deaths field-type-number-integer field-label-above'})

    data.append([rows_state, rows_confirmed, rows_cured, rows_death])


for row in rows_state:
    state.append(row.find('div', class_='field-item').text)
for row in rows_confirmed:
    confirmed.append(row.find('div', class_='field-item').text)
for row in rows_cured:
    cured.append(row.find('div', class_='field-item').text)
for row in rows_death:
    death.append(row.find('div', class_='field-item').text)
