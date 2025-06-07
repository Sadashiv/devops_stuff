import requests
req = requests.get("https://example.com/")
print(type(req))
print(req.text)

import bs4

soup = bs4.BeautifulSoup(req.text, "lxml")
print(soup)
print(dir(soup))
print(soup.select('title')[0].getText())
print(soup.select('p'))
print(soup.select('p')[0].getText())

res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
print(res.text)
soup = bs4.BeautifulSoup(req.text, "lxml")
print(soup.select(".vector-toc-text"))


krish = requests.get("https://en.wikipedia.org/wiki/Krishna")
soup = bs4.BeautifulSoup(krish.text, "lxml")
computer = soup.select('.mw-file-element')[2]
print(computer['src'])
reqimg = requests.get(f"https:{computer['src']}")
print(reqimg.content)

f = open("Sri_Mariamman_Temple_Singapore_2_amk.jpg", 'wb')
f.write(reqimg.content)
f.close()

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
bres = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(bres.text, "lxml")
products = soup.select(".product_pod")
print(products[0])
example = products[0]
print("star-rating Three" in products[0])
#print(example.select(".star-rating.Three"))
#print(example.select("a")[1]['title'])

two_star_title = []

for n in range(1, 51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    books = soup.select(".product_pod")
    for book in books:
        if len(book.select("star-rating.Two")) != 0:
            book_title = book.select('a')[1]['title']
            two_star_title.append(book_title)
print(two_star_title)
