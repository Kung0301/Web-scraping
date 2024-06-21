from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML<a href=\"#\"> Sawasdee")
print(soup.prettify())
print(soup.find(text="bad"))
print(soup.a)