import bs4
import requests
from bs4 import BeautifulSoup
from time import sleep
from lookup_symbol import *

#Given a specific symbol of a stock, this function will
#lookup that stock's price on finance.yahoo.com.
#Param: the symbol of a stock
#Return: the price of that stock
def parsePrice(symbol):
	url = 'https://finance.yahoo.com/quote/' + symbol + '/'
	r = requests.get(url)
	soup = bs4.BeautifulSoup(r.text, 'xml')

	#Price will be the result of the web scraping of the website for
	#the price of the stock with the symbol parameter. 
	price = soup.find('span',{'class':"Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)"}).text

	return price

#Prints the price of the stock with symbol parameter.
#In this function, we'll call the parsePrice() function
#to find the price of the stock. 
def printPrice():
	symbol = str(processRequest())
	print('Current price is: ' + str(parsePrice(symbol)))

printPrice()