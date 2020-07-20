import requests
from bs4 import BeautifulSoup
url ="http://localhost:8080/request.html"
r = requests.get(url)
y = BeautifulSoup(r.content, 'html.parser')
a = []
for letter in y.find_all('p'):
    b = letter.get_text()
    a.append(b)
print(a[0])
