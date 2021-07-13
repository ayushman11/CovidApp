from os import error
import requests
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
LANGUAGE = "en-US,en;q=0.5"
session = requests.Session()
session.headers['User-Agent'] = USER_AGENT
session.headers['Accept-Language'] = LANGUAGE
session.headers['Content-Language'] = LANGUAGE
text= session.get('https://www.google.com/search?q=Coronavirus+delhi&biw=1366&bih=625&tbm=nws&sxsrf=ALeKk02EjSFMS4VAFdmugQbCo6PXEPWIYg%3A1626179779235&ei=w4jtYN3cDd_B3LUPxo-GaA&oq=Coronavirus+india&gs_l=psy-ab.3..0i433i131k1j0i433k1l2j0i433i131k1j0i433k1j0i433i131k1j0i433k1j0i433i131k1l2j0i433k1.112257.113775.0.114002.10.9.0.0.0.0.260.1002.0j2j3.5.0....0...1c.1.64.psy-ab..6.4.859...0j0i433i67k1j0i67k1j0i433i131i273k1j0i273k1.0.uaiWtMRTDTI').text


from bs4 import BeautifulSoup
soup= BeautifulSoup(text, 'html5lib')
articles= soup.find_all('div', class_="kCrYT")
news= []

# print(articles)

for article in articles:
    try:
        url_temp= article.a['href']
        url= (url_temp.split("/url?q=")[1]).split("&sa=U&ved")[0]
        newspaperx= article.find('div', class_='BNeawe UPmit AP7Wnd').text
        # newspaper= newspaperx.split('<div class="BNeawe UPmit AP7Wnd">')[1].split('</div>')[0]

        headline= article.find('div', class_='vvjwJb').text
        # print(headline)   
        news.append([newspaperx, headline, url])
    except AttributeError:
        continue


print(news)
