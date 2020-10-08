from bs4 import BeautifulSoup
import requests
import re

result=requests.get("https://www.investopedia.com")
web_re= r'[httphttps]+[://]+[www.]+[a-zA-z0-9]+[.com.org]+'
email_re= r'[a-zA-Z0-9_.-]+[^!#$%^&*()]@[a-zA-Z]+[.com]+'
corpus = BeautifulSoup(result.content, "html.parser")
corpus=str(corpus)
data1=re.findall(web_re,corpus)
print (data1)

#alternative
print ("\n\n Second time \n\n")

with open('investing.html') as f:
    corpus = f.read()
    #print (type(corpus))

data = re.findall(web_re,corpus)
print (data)


with open ('emails.txt') as f:
    read = f.read()
email_data=re.findall(email_re,read)
print(email_data)

