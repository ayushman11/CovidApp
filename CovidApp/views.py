from django.http import request,HttpResponse
from django.shortcuts import render


# Create your views here.

def html_content_world():
    import requests
    text= requests.get('https://www.worldometers.info/coronavirus/').text

    return text


def html_content_india():
    import requests
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    text= session.get('https://www.mygov.in/corona-data/covid19-statewise-status/').text

    return text

def india_headline():
    from bs4 import BeautifulSoup
    html_text= html_content_india()
    soup= BeautifulSoup(html_text, 'html.parser')

def india_data():
    from bs4 import BeautifulSoup
    html_text= html_content_india()
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


    for row in rows_state:
        state.append(row.find('div', class_='field-item').text)
    for row in rows_confirmed:
        confirmed.append(row.find('div', class_='field-item').text)
    for row in rows_cured:
        cured.append(row.find('div', class_='field-item').text)
    for row in rows_death:
        death.append(row.find('div', class_='field-item').text)

    for i in range(36):
        data.append([state[i],confirmed[i],cured[i],death[i]])

    return data

def worldwide_data():
    from bs4 import BeautifulSoup
    html_text= html_content_world()
    soup= BeautifulSoup(html_text, 'html.parser')
    data= soup.find_all('div', {'id': 'maincounter-wrap'})
    world_info=[]

    for x in data:
        world_info.append(int(x.div.span.text.replace(',','')))

    world_info.insert(1,world_info[0]-world_info[2])

    for i in range(4):
        world_info[i]='{:,}'.format(world_info[i])

    return world_info

def country_cases():
    from bs4 import BeautifulSoup
    html_text= html_content_world()
    soup= BeautifulSoup(html_text, 'html.parser')
    name_active= [['Country', 'Total Cases']]
    rows= soup.find_all('tr')

    for row in rows:
        try:
        # table_data= row.find_all('td')
            country= row.find('a',class_='mt_a').text
            if country=='USA': country='United States'
            case= row.find_all('td')[2].text.replace(',','')
            name_active.append([country,int(case)])
        except AttributeError:
            continue
    
    return name_active


def index(request):
    import json
    worldwide= worldwide_data()
    world_data= country_cases()
    india= india_data()
    country_data= json.dumps(world_data)
    return render(request, 'CovidApp/index.html', {
        'worldwide': worldwide,
        'india_data': india,
        'world_data': country_data
    })
