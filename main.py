from bs4 import BeautifulSoup
import requests

url = 'http://quotes.toscrape.com'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
# print(soup)

#print(soup.find_all('p', class_ = "copyright"))

#print(soup.find('span', class_ = "text").text.strip())

print(soup.find_all('span', itemprop = 'text')) #finds all items with 'span' tag and itemprop atribute

first_p = soup.find('span', itemprop = 'text') #finds the first item with those attributes

second_p = first_p.find_next('span', itemprop = 'text') # finds the next item with those attributes

print(first_p.text)
print(second_p.text)
