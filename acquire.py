from bs4 import BeautifulSoup
import requests
import os

def scrape_codeup(url):
    '''
    function that scrapes codeups blog site
    '''
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


def scrape_one_page(topic):
    '''
    function that scrapes articles from one topic
    '''
    base_url = 'https://inshorts.com/en/read/'
    response = get(base_url + topic)
    soup = BeautifulSoup(response.content, 'html.parser')
    titles = soup.find_all('span', itemprop='headline')
    summaries = soup.find_all('div', itemprop='articleBody')
    summary_list = []
    for i in range(len(titles)):  
        temp_dict = {'category': topic,
                     'title': titles[i].text,
                     'content': summaries[i].text}
        summary_list.append(temp_dict)
    return summary_list    


#Define a function that will scrape information about an array of topics
def get_news_articles(topic_list):
    '''
    function takes in a list of topics and then returns articles
    '''
    file = 'news_articles.json'
    if os.path.exists(file):
        with open(file) as f: 
            return json.load(f)
    final_list = []
    for topic in topic_list:
        final_list.extend(scrape_one_page(topic))
    with open(file, 'w') as f:
        json.dump(final_list, f)
    return final_list    