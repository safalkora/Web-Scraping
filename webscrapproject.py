import requests
import bs4 
import BeautifulSoup
url = "https://codewithharry.com"

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title

paras = soup.find_all('p')

print(soup.find('p'))

print(soup.find('p')['class'])

print(soup.find_all("p", class_ = "lead"))

print(soup.find('p').get_text())
print(soup.get_text()) 

anchors = soup.find_all('a')
all_links = set()

for link in anchors:
    if(link.get('herf') != '#'):
        linkText = "http://codewithharry.com" +link.get('href')
        all_links.add(link)
        print(linkText)

navbarSupportedContent = soup.find(id ='navbarSupportedContent')

element = soup.select('.modal-footer')
print(element)