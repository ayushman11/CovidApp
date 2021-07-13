from django.http import request,HttpResponse
from django.shortcuts import render


# Create your views here.

def html_content_news_india():
    import requests
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    text= session.get(f'https://www.google.com/search?q=Coronavirus+India&biw=1366&bih=625&tbm=nws&sxsrf=ALeKk02EjSFMS4VAFdmugQbCo6PXEPWIYg%3A1626179779235&ei=w4jtYN3cDd_B3LUPxo-GaA&oq=Coronavirus+india&gs_l=psy-ab.3..0i433i131k1j0i433k1l2j0i433i131k1j0i433k1j0i433i131k1j0i433k1j0i433i131k1l2j0i433k1.112257.113775.0.114002.10.9.0.0.0.0.260.1002.0j2j3.5.0....0...1c.1.64.psy-ab..6.4.859...0j0i433i67k1j0i67k1j0i433i131i273k1j0i273k1.0.uaiWtMRTDTI').text

    return text


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
    soup= BeautifulSoup(html_content_news_india(), 'html5lib')
    articles= soup.find_all('div', class_="kCrYT")
    news= []

    # print(articles)

    for article in articles:
        try:
            url_temp= article.a['href']
            url= (url_temp.split("/url?q=")[1]).split("&sa=U&ved")[0]
            newspaper= article.find('div', class_='BNeawe UPmit AP7Wnd').text
            # newspaper= newspaperx.split('<div class="BNeawe UPmit AP7Wnd">')[1].split('</div>')[0]

            headline= article.find('div', class_='vvjwJb').text
            # print(headline)   
            news.append([newspaper, headline, url])
        except AttributeError:
            continue

    # news_final= news[:3]
    return news

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
    headlines= india_headline()
    country_data= json.dumps(world_data)
    return render(request, 'CovidApp/index.html', {
        'headlines': headlines,
        'worldwide': worldwide,
        'india_data': india,
        'world_data': country_data
    })