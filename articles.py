import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'

# load the page
r = requests.get(url)

# parse the page using the text of the HTML that was obtained before
soup = BeautifulSoup(r.text, 'html.parser')

# find all article elements in the HTML
articles = soup.find_all('article')

# the article heading seems to exist inside an h2 element and
# it seems that there is only one h2 element per article
h2s = [article.find('h2') for article in articles]

# extract the text from the h2 element, but be aware that
# sometimes the article has no h2 element
article_titles = [h2.text for h2 in h2s if h2 is not None]

for title in article_titles:
	print(title)