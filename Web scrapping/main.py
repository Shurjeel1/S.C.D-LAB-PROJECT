#If you want to scrap a website
#1) Use th API
#2) HTML Web Scrapping using some tool LIKE BS4

#Step 1 : Install All the  Requirements
#pip install requests 
#pip install html5lib
#pip install bs4
import requests
from bs4 import BeautifulSoup
url= "https://www.omdbapi.com/"
#Step2: Get the HTML 
r = requests.get(url)
htmlContent= r.content
#print(htmlContent)
#Step3: Parse the HTMl
soup= BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)
# #Step4:HTML tree Traversal
#Commonly used types of object
#1.print(type(title))   Tags
#2.print(type(title.string)) Navigable String
#3.print(type(soup))   BeautifulSoup
#4. Comment

markup= "<p><!-- This is a comment, My name is SHARJEEL--></p>"
soup2= BeautifulSoup(markup)
#print(type(soup2.p.string))
#exit()

#Get the Title of HTML page
title = soup.title

#Get all the paragraphs from the page
paras= soup.find_all('p')
#print(paras)

#Get all the anchor tags from the page
anchors= soup.find_all('a')
#print(anchors)

#Get First element in HTML Page
print(soup.find('p'))
#Get classes of any element in HTML Page
print(soup.find('p')['class'])

#find all elements with class lead
print(soup.find_all("p", class_="lead"))

#Get the text from TAGS/soup
print(soup.find('p').get_text())

print(soup.get_text())

#Get all links on the page
all_link =set()
for link in anchors:
    if (link.get('hrf') != '#'):
      linkText= "https://www.omdbapi.com/" + link.get('href')
      all_link.add(link)
      print(linkText)   
navbarSupportContent =  soup.find(id="navbar-main")
print(navbarSupportContent.contents)