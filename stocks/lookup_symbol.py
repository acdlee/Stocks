import bs4
import requests
from bs4 import BeautifulSoup
import re

#In this function, we'll ask the user to input the name
#of the stock they want to buy. 
#First, we'll lookup the symbol for the input stock using
#the website marketwatch.com. 
def processRequest():
	#Asking for and stripping the input. 
	stock_request = input("Please enter the name of the stock you wish to lookup: ")
	stock_request.strip()

	#Scraping for possible results of looking up 
	#the input stock on the marketwatch website.
	#Note: the results are lists of symbols, company names, and  exchanges. 
	url = "https://www.marketwatch.com/tools/quotes/lookup.asp?siteID=mktw&Lookup=" + stock_request + "&Country=us&Type=All"
	r = requests.get(url)
	soup = bs4.BeautifulSoup(r.text, 'html.parser')
	res = soup.find(class_='results').text


	return createList(res)


def createList(res):
	res = res.strip('\n')	#strip preceding and ending newlines
	res = res.replace('\n', ' ')	#replace remaining newlines with spaces

	
	l = list(res.split(" "))
	while '' in l:
		l.remove('')
	#Remove the first three elements of the list (Since they're Symbol Company Exchange)
	return createHash(l[3:])



# Our data is of the form:   	Symbol 	Company 			Exchange
# 							AMZN 	Amazon.com Inc. 	NAS
# ...lets take advantage of this fact...

# how about we make a hash, where the symbol is the key and
# 	the value is a list of the company name and exchange

def createHash(lst):
	exchange_list = [
						"NAS", 
						"OTC"
					]
	h = {}
	curr_key = ""
	new_key_flag = 1
	for info in lst:
		if new_key_flag:
			curr_key = info
			h[curr_key] = []
			new_key_flag = 0
		else:
			if info not in exchange_list:
				if h[curr_key] == []:
					h[curr_key].append(info)
				else:
					h[curr_key][0] += "  " + info
			else:
				new_key_flag = 1
				h[curr_key].append(info)
	return pick_stock(h)

def pick_stock(stocks):
	desired_stock = ""
	for k, v in stocks.items():
		print(k + ": \t" + str(v))
		x = input("Is this your desired stock (Y/N): ")
		if x == 'Y' or x == 'y':
			#we found the user's desired stock's symbol
			desired_stock += k
			break

	return desired_stock
