from bs4 import BeautifulSoup
import requests
import re

result=requests.get("https://www.investopedia.com")
email_re= r'[httphttps://]+[www]+[.]+[a-zA-Z0-9-]+[.com]+'
corpus = BeautifulSoup(result.content, "html.parser")
corpus=str(corpus)
data1=re.findall(email_re,corpus)
print (data1)

#alternative
print ("\n\n Second\n\n")

with open('investing.html') as f:
    corpus = f.read()
    #print (type(corpus))

data = re.findall(email_re,corpus)
print (data)
