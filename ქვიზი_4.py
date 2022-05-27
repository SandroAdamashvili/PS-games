import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

file = open('ps_games.csv', 'w', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(['title', 'price'])

page = 1
while page < 6:
    url = 'https://store.playstation.com/en-us/category/85448d87-aa7b-4318-9997-7d25f4d275a4/' + str(page)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    soup_sub = soup.find('ul', class_='psw-grid-list')
    all_games = soup_sub.find_all('li', class_='psw-l-w-1/2@mobile-s psw-l-w-1/2@mobile-l psw-l-w-1/6@tablet-l'
                                               ' psw-l-w-1/4@tablet-s psw-l-w-1/6@laptop psw-l-w-1/8@desktop'
                                               ' psw-l-w-1/8@max')
    for game in all_games:
        title = game.section.find('span', class_='psw-t-body').text
        price = game.section.find('div', class_='psw-fill-x').div.span.text
        print('title:', title)
        print('price:', price, '\n')
        file_obj.writerow([title, price])
    page += 1
    sleep(randint(3, 8))
