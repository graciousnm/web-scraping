from bs4 import BeautifulSoup
import requests
import pandas as pd

books = []
for i in range(1,31):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    response = requests.get(url).text

    soup = BeautifulSoup(response, "html.parser")
    ol = soup.find("ol")
    article = ol.find_all("article", class_= "product_pod")

    for image in article:
        img = image.find("img")
        title = img.attrs["alt"]
        star = image.find("p")
        star = star["class"][1]
        price = image.find("p", class_= "price_color").text
        price = float(price[2:])
        books.append([title, price, star])

df = pd.DataFrame(books, columns = ["Title", "Price", "Star Ratings"])
df.to_csv("books.csv", index=None)
