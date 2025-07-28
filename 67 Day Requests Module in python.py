# Day 67 -> Requests Module in python


import requests
from bs4 import BeautifulSoup


response= requests.get("https://github.com/Saboor-Ul-Fajr-24CS032/100-Day-Challenge-of-Learning-Python")
print(response.text)


url = "https://github.com/Saboor-Ul-Fajr-24CS032/100-Day-Challenge-of-Learning-Python"
r= requests.get(url)
print(r.text)


soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h1"):
    print(heading.text)