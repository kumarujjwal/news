

import requests
from bs4 import BeautifulSoup

 
print "THIS IS FROM TOI- BUSINESS" + '\n'

r = requests.get("http://timesofindia.indiatimes.com/business")

soup = BeautifulSoup(r.content)
linksTOImain = soup.find_all("div",{"class":"ct1stry"})



for item in linksTOImain:
    for kuch in item.contents:
        print kuch.text.split('|')[0] 
    
        print kuch.text.split('|')[-1].split(';')[-1] + '\n'



print "THIS IS FROM TOI- BUSINESS - INDIAN BUSINESS" + '\n'

r = requests.get("http://timesofindia.indiatimes.com/business/india-business")

soup = BeautifulSoup(r.content)
linksTOImain = soup.find_all("div",{"class":"ct1stry"})

for item in linksTOImain:
    for kuch in item.contents:
        print kuch.text.split('|')[0] 
    
        print kuch.text.split('|')[-1].split(';')[-1] + '\n'



print "This is from TOI- BUSINESS - INTERNATIONAL" + '\n'

r = requests.get("http://timesofindia.indiatimes.com/business/international-business")
soup = BeautifulSoup(r.content)
linksTOImain = soup.find_all("div",{"class":"ct1stry"})

for item in linksTOImain:
    for kuch in item.contents:
        print kuch.text.split('|')[0] 
    
        print kuch.text.split('|')[-1].split(';')[-1] + '\n'


r = requests.get("http://www.thehindu.com/sci-tech/")
soup = BeautifulSoup(r.content)
latest = soup.find_all("div",{"class":"headlines"})


print "latest Headlines from the Hindu"

for item in latest:
    print item.text

print "most popular Headlines from the Hindu"


mostpopular = soup.find_all('div',{"class":"tab1 tab"})
for item in mostpopular:
    print item.text

print "most commented Headlines from the Hindu" 


mostcommented =soup.find_all('div',{"class":"tab2 tab"})
for item in mostcommented:
    print item.text



print '\n'+ "technology column " + '\n'
technology = soup.find_all('div',{"class":"smltitle1"})
for item in technology:
    print item.text
  
