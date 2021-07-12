from django.http import request,HttpResponse
from django.shortcuts import render


# Create your views here.

def html_content():
    import requests

    # USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    # LANGUAGE = "en-US,en;q=0.5"
    # session = requests.Session()
    # session.headers['User-Agent'] = USER_AGENT
    # session.headers['Accept-Language'] = LANGUAGE
    # session.headers['Content-Language'] = LANGUAGE
    text= requests.get('https://www.worldometers.info/coronavirus/').text

    return text




def country_cases():
    from bs4 import BeautifulSoup
    html_text= html_content()
    soup= BeautifulSoup(html_text, 'html.parser')
    name_active= [['Country', 'Total Cases']]
    rows= soup.find_all('tr')

    for row in rows:
        try:
        # table_data= row.find_all('td')
            country= row.find('a',class_='mt_a').text
            if country=='USA': country='US'
            case= row.find_all('td')[2].text.replace(',','')
            name_active.append([country,int(case)])
        except AttributeError:
            continue
    
    return name_active


def index(request):
    import json
    world_data= country_cases()
    country_data= json.dumps(world_data)
    return render(request, 'CovidApp/index.html', {
        'world_data': country_data
    })
