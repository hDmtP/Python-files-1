from bs4 import BeautifulSoup, UnicodeDammit
import re

from bs4 import dammit

with open('tut26.html') as html_doc:
    soup = BeautifulSoup(html_doc, "html.parser")

# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.a)
# print(soup.find_all('div'))
# print(soup.find(id='item2'))

# for tag in soup.find_all(re.compile('b')):
#     print(tag.name)

# dammiT = UnicodeDammit("Sacr\xc3\xa9 bleu!")
# print(dammiT.unicode_markup)
# print(dammiT.original_encoding)


