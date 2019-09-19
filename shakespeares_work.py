from scraper import page_links, textfromlink

# Let's assign a variable named 'url' to the website we intend to scrape
url = 'http://shakespeare.mit.edu/'

# Let's extract the home_links and internal_links from the entire website
home_links, internal_links = page_links(url)

# Let's extract the text from each internal_link and stitch them together into a single string
full_text = textfromlink(internal_links)