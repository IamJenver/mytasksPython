from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://quote.rbc.ru/?utm_source=topline')
html = req.read()

soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('a', class_='q-item__link')
 
results = []

for item in news:
    title = item.find('span', class_='q-item__title').get_text(strip=True)
    desc = item.find('span', class_='q-item__description').get_text(strip=True)
    href = item.get('href')
    results.append({
        'title': title,
        'desc': desc,
        'href': href,
    })

f = open('rbk.news.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    f.write(f'Новость №{i}\n\nHead: {item["title"]}\nDescription: {item["desc"]}\nReference:{item["href"]}\n\n******************************\n')
    i += 1
f.close()