import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re


def checkDirectory(url):
    if(url.endswith('/')):
        return True
    else:
        return False

def findURLs(url):
    page = requests.get(url).content
    bsObj = BeautifulSoup(page, 'html.parser')
    anchor_list = bsObj.findAll('a', href=True)

    for link in anchor_list:
        print("link['href']",link['href'])
        print("checkDirectory(link['href'])",checkDirectory(link['href']))
        if(checkDirectory(link['href'])):
            newUrl = url + link['href']         
            findURLs(newUrl) #recursive
        else:
	    #.jpg as example
            if(link['href'].endswith('.jpg')):    
                #print("FOUND IMAGES!")
                #print("URL :",url)
                #print("link['href'] :",link['href'])
                link_download = url+link['href']
                print("link_download=",link_download)
                urllib.request.urlretrieve(link_download, link['href'])

#put your desired URL here
startUrl = "http://baituljannah.sch.id/assets/upload/image/"
findURLs(startUrl)
