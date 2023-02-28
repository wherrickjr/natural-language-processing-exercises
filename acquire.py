from bs4 import BeautifulSoup
import requests
import os

def scrape_codeup(url):
    headers = {'User-Agent': 'Codeup Data Science'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    article = soup.find_all('a', class_='more-link') #(tag beginning, class = 'class name')
    href = []
    for i in article:
        xyz = i['href']
        href.append(xyz)
    dictionary = {}
    lists = []
    for i in href:
        url = i
        headers = {'User-Agent': 'Codeup Data Science'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        dictionary['title'] = soup.find('h1', class_ = 'entry-title').text
        dictionary['content'] = soup.find('div', class_ = 'entry-content').text
        dictionary = {}
        lists.append(dictionary)
    return lists