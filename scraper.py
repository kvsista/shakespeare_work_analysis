import requests
from bs4 import BeautifulSoup
import os
import pickle

def folder_structure():

    # Let's create a folder named 'data'
    data = 'data'
    if not os.path.exists(data):
        os.mkdir(data)
        print("Folder Created: 'data'")
    else:
        print("Folder Exists: 'data'")
    
    # Let's create a folder named 'data/links'
    links = data + '/links'
    if not os.path.exists(links):
        os.mkdir(links)
        print("Folder Created: 'data/links'")
    else:
        print("Folder Exists: 'data/links'")
    
    # Let's create a folder named 'texts'
    texts = data + '/texts'
    if not os.path.exists(texts):
        os.mkdir(texts)
        print("Folder Created: 'data/texts'")
    else:
        print("Folder Exists: 'data/texts'")
    
    # Let's create a folder named 'tokens'
    tokens = data + '/tokens'
    if not os.path.exists(tokens):
        os.mkdir(tokens)
        print("Folder Created: 'data/tokens'")
    else:
        print("Folder Exists: 'data/tokens'")
    


def page_links(url):
    """
    This function will a get a list of all the links in the home page of website.
    """
    source = requests.get(url).text # Get the html text from the url
    soup = BeautifulSoup(source, 'html.parser') # Create a soup using the 'lxml' parser
    urls = soup.find_all('a') # Get a list of urls from the 'a' tags
    
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

    folder_structure()
    pickle.dump(home_links, open("data/links/home_links.pkl", "wb"))
    pickle.dump(internal_links, open("data/links/internal_links.pkl", "wb"))

    return

def textfromlink(linklist):
    """
    This function goes into each link, extracts the text from each link, and stiches it together with
    the text from the other links creating a single string of text from the entire website.
    """

    fulltext_list = []
    
    for link in linklist:
        if 'full.html' in link:
            source = requests.get(link).text
            soup = BeautifulSoup(source, 'html.parser')
            blockquotes = soup.find_all('blockquote')

            text_string = []
            for blockquote in blockquotes:
                a_tags_text = []
                for txt in blockquote.find_all('a'):
                    a_tags_text.append(txt.text)
                text_string.append(' '.join(a_tags_text))
            
            fulltext_list.append(text_string)

    folder_structure()
    pickle.dump(fulltext_list, open("data/texts/texts_list.pkl", "wb"))

    return
