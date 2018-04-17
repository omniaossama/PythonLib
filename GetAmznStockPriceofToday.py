# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://www.marketwatch.com/investing/stock/amzn'

# query the website and return the html to the variable ‘page’
page = urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
name_box= soup.find('bg-quote', attrs={'class': 'value'})

stock = name_box.text.strip() # strip() is used to remove starting and trailing
print('Amazon Stock Price Today: '  + str(stock) )

# get the index price
#price_box = soup.find('div', attrs={'class':'price'})
#price = price_box.text
#print(price)