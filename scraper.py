import requests 
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('https://www.scrapethissite.com/pages/simple/')

soup = BeautifulSoup(response.text, 'html.parser')

countries_list = []
countries = soup.find_all('h3', class_='country-name')
for country in countries: 
    countries_list.append(country.text)
    #print(countries_list)


capitals_list = []
capitals = soup.find_all('span', class_='country-capital')
for capital in capitals:
    capitals_list.append(capital.text)
    #print(capitals_list)


population_list = []
populations = soup.find_all('span', class_='country-population')
for population in populations:
    population_list.append(population.text)
    #print(population_list)


area_list = []
areas = soup.find_all('span', class_='country-area')
for area in areas:
    area_list.append(area.text)
    #print(are_list)


info = { 
    'country': '',
    'capital': '',
    'population': '',
    'area': ''
}


dane = [] 

for i in range(len(countries_list)):
    dane.append({
        'country': countries_list[i],
        'capital': capitals_list[i],
        'population': population_list[i],
        'area': area_list[i]
    })

#print(info)


df = pd.DataFrame(dane)
print(df.head())

df.to_csv('countries.csv', index=False)
