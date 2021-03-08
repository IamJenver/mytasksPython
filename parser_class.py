from bs4 import BeautifulSoup
import urllib.request


class Parser:

    raw_html = ''
    html = ''
    results = []
    
    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html, 'html.parser')

    def parsing(self):
        news = self.html.find_all('a', class_='q-item__link')

        for item in news:
            title = item.find('span', class_='q-item__title').get_text(strip=True)
            desc = item.find('span', class_='q-item__description').get_text(strip=True)
            href = item.get('href')
            self.results.append({
                'desc': desc,
                'href': href,
                'title': title,
            })
    
    def save(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            i = 1
            for item in self.results:
                f.write(f'Новость №{i}\n\nHead: {item["title"]}\nDescription: {item["desc"]}\nReference:{item["href"]}\n\n******************************\n')
                i += 1



    def run(self):
        self.get_html()
        self.parsing()
        self.save()
