import pandas as pd
import requests
from bs4 import BeautifulSoup
items = []
url = "https://www.ebay.ca/deals/trending/all"

response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")
start = soup.find_all("div", class_ = "col")
for img in start:
    title = img.find("h3")
    title = title.attrs["title"]
    price = img.find("span", class_= "first").text
    price = price[3:]
    items.append([title, price])

df = pd.DataFrame(items, columns = ["ITEM NAME", "PRICE ($)"])
df.to_csv("ebay.csv", index=None)
