import requests
from bs4 import BeautifulSoup
import pandas as pd

books = []

# Loop through pages 1 to 50
for i in range(1, 51):

    # Corrected URL to iterate through pages
    url = f"https://books.toscrape.com/catalogue/category/books_1/page-{i}.html"
    response = requests.get(url)
    
    # Check if the page exists
    if response.status_code != 200:
        print(f"Page {i} not found, stopping the scraping process.")
        break
    
    soup = BeautifulSoup(response.content, 'html.parser')
    ol = soup.find('ol')
    articles = ol.find_all('article', class_='product_pod')

    # Loop through each book on the page
    for article in articles:
        image = article.find('img')
        title = image.attrs['alt']
        star = article.find('p')
        star = star['class'][1]  # Extracting the star rating from class
        
        price = article.find('p', class_='price_color').text
        price = float(price[1:])  

        books.append([title, price, star])

# Creating a DataFrame with the collected data
df = pd.DataFrame(books, columns=['Title', 'Price', 'Star Rating'])

# Saving data to CSV without an index
df.to_csv('books.csv', index=False)

print("Scraping completed and data saved to books.csv")
