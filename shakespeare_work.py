import requests
from bs4 import BeautifulSoup

def page_links(url):
    
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    urls = soup.find_all('a')
    
    home_links = []
    for link in urls:
        if '.html' in link.get('href'):
            home_links.append(url + link.get('href'))
    
    links = []
    
    for lnk in home_links:
        
        try:
            source = requests.get(lnk).text
            soup = BeautifulSoup(source, 'lxml')
            urls = soup.find_all('a')

            for a_tag in urls:
                links.append(str(lnk[:-10])+str(a_tag.get('href')))
        
        except requests.exceptions.ConnectionError:
            requests.get(lnk).status_code = "connection refused"
    
        internal_links = []
        for link in links:
            if '.html' in link:
                internal_links.append(link)
    
    return home_links, internal_links

def textfromlink(linklist):

    fulltext_list = []

    for link in linklist:
        source = requests.get(link).text
        soup = BeautifulSoup(source, 'html.parser')
        texts = soup.find_all('blockquote')

        if 'full.html' in link:
            for text in texts:
                for txt in text.find_all('a'):
                    fulltext_list.append(txt.text)
    
    fulltext_string = ' '.join(fulltext_list)

    return fulltext_string

url = 'http://shakespeare.mit.edu/'
home_links, internal_links = page_links(url)
full_text = textfromlink(internal_links)