import requests
from bs4 import BeautifulSoup
#Fetching data from a website
response = requests.get('https://www.codingtemple.com/')
print(response.status_code)

#Check the status of our request response
print(response.text)
print(response.content) #print entire contensts of the response object- not pretty

#use beautiful soup to parse the html- make it pretty

soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())

print(soup.title.text)  #print response.content.title.text

print(soup.a)
print(soup.h1.text)
#Thats all for BeautifulSoup 


