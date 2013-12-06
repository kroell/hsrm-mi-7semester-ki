'''
Created on 06.12.2013

@author: soerenkroell
'''
import urllib2
import time
import socket
import threading
from bs4 import BeautifulSoup
from model import *

URL = 'http://www.spiegel.de/'
pages = []


def initPage(docurl):
    try:
        #request = urllib2.Request(docurl)
        response = urllib2.urlopen(docurl)
    except urllib2.URLError, e:
        raise Exception("URL error: %r" % e)
    except socket.timeout, e:
        raise Exception("Socket.timeout error: %r" % e)

    html = response.read()
    soup = BeautifulSoup(html)
    title = soup.title.string
    created = modified = time.time()
    page = Page(html, docurl, title, created, modified)
    response.close() 
    
    pages.append(page)
    
    for link in soup.find_all('a'):
        url = link.get('href')
        if url.startswith('/') or url.startswith(URL):
            if url.startswith('/'):
                url = URL + url[1:]
            if url not in [page.url for page in pages]:
                print url
                time.sleep(5) #funzt nit
                initPage(url)
            


if __name__ == '__main__':
    initPage(URL)

    