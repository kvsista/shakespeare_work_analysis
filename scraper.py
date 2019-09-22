import requests
from bs4 import BeautifulSoup

def page_links(url):
    """
    This function will a get a list of all the links in the home page of website.
    """
    source = requests.get(url).text # Get the html text from the url
    soup = BeautifulSoup(source, 'lxml') # Create a soup using the 'lxml' parser
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
    
    return home_links, internal_links

def textfromlink(linklist):
    """
    This function goes into each link, extracts the text from each link, and stiches it together with
    the text from the other links creating a single string of text from the entire website.
    """

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

# def textfromtitles(linklist):

#     titles_texts = []

#     for link in linklist:
        
#         if 'full.html' in link:
#         source = requests.get(link).text
#         soup = BeautifulSoup(source, 'html.parser')
#         texts = soup.find_all('blockquote')

#             for text in texts:
#                 title_text = []
#                 for txt in text.find_all('a'):
#                     title_text.append(txt.text)
#                 title_text_string = ' '.join(title_text)
    
#         titles_texts.append(title_text_string)
    
#     return titles_texts
