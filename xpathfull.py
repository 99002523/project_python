import requests
from bs4 import BeautifulSoup
import re
import itertools

def xpath_soup(element):
    # type: (typing.Union[bs4.element.Tag, bs4.element.NavigableString]) -> str
    components = []
    child = element if element.name else element.parent
    for parent in child.parents:  # type: bs4.element.Tag
        siblings = parent.find_all(child.name, recursive=False)
        components.append(
            child.name if 1 == len(siblings) else '%s[%d]' % (
                child.name,
                next(i for i, s in enumerate(siblings, 1) if s is child)
                )
            )
        child = parent
    components.reverse()
    return '/%s' % '/'.join(components)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

URL = 'https://www.guru99.com/selenium-tutorial.html'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='g-top')

print(results.prettify())

job_elems = results.find_all('div', class_='g-container')
for job_elem in job_elems:
    print(job_elem, end='\n'*2)

#content = BeautifulSoup(soup, 'lxml')
elem = soup.find(string=re.compile(' Trending Course'))
print(xpath_soup(elem))

print(xpath_soup(results))

for job_elem in job_elems:
    print(xpath_soup(job_elem))
