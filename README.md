# CovidApp
Web scraping project using Django and BeautifulSoup

## Installation Procedure

Install [`Anaconda`](https://www.anaconda.com/products/individual) on your system and include its bin path in the environment variables  

Clone this repository on your local computer using the command `git clone https://github.com/ayushman11/CovidApp`  

Run the following command in the terminal opened in the location of the repository
to create a virtual environment and install Django:\
`conda create --name myEnv django`  

After the installation, activate the environment using: `activate myEnv`  

Now, install all the dependencies of the project using: `pip install -r requirements.txt`  

Run the Django server on a local host port using: `python manage.py runserver`  

Now, paste the url (like 127.0.0.1:8000/CovidApp) in a web browser, to view the webpage.  

## Dependencies of the Project

  ### Front-end:
  ● HTML for the basic skeleton of the webpage.\
  ● Base CSS for designing and appearance.\
  ● Bootstrap 5 framework for a quick design and customizations.\
  ● FontAwesome for icons and images.  
  
  ### Back-end:
  ● Django (a Python-based web framework) for rapid development and clean,\
  pragmatic design in the model-template-views architectural pattern.\
  ● BeautifulSoup is a Python library that is used for pulling data out of HTML and\
  XML files.\
  ● Requests is a Python library used for making HTTP requests.\
  ● Html5lib, lxml, html.parser are python libraries used for parsing the scraped\
  HTML content.\
  ● Maps JavaScript API provided by Google for incorporating an interactive\
  world-map.
