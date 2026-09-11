# BeautifulSoup is a Python library used to parse HTML and navigate through its structure.
import requests
from bs4 import BeautifulSoup
#select return list

url = "https://books.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    print("Requset succedded")

soup = BeautifulSoup(response.text , "html.parser")
#all books details
details_books = []

# 1. Grab the all book containers
all_books = soup.find_all('article',class_='product_pod')

for book in all_books[:20]:
    # 2. Extract full title from the 'title' attribute of the <a> tag
    title = book.find('h3').find('a')['title']

    # 3. Extract price and clean it into a float
    raw_price = book.find('p',class_="price_color").text
    price = float(raw_price.replace("Â£","").strip())

    # 4. Extract rating from the class list: ['star-rating', 'Three']
    rating = book.find("p",class_= "star-rating")['class'][1]
    #['class'] give value of class attributes in list nd we fetch index 1
     
    # 5. Extract stock availability
    available = book.find("p" ,class_="instock availability").text.strip()

    book_data = {
        'title' : title,
        'price' : price,
        'ratings' : rating,
        "stock availability" : available
    }
    details_books.append(book_data)


for index,data in enumerate(details_books,start=1):
    print(index,data)
    print(f"\n")

#cheap books
cheap_book = [b for b in details_books if b['price'] < 20.0 ]

print(f"There is {len(cheap_book)} has cost less than 20.0")