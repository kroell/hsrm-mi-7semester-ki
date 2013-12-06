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
SHOP = 'http://www.spiegel.de/shop/'

class Spider(object):
    
    def __init__(self, start_url):
        '''
        Constructor
        '''
        self.start_url = start_url
        self.pages = []
    
    
    def initSpider(self, docurl):
    
        try:
            response = urllib2.urlopen(docurl,timeout=4)
        except urllib2.HTTPError, error:
            #raise Exception("HTTP error: %r" % error, error.code)
            print "HTTP error: %r" % error.code
        except socket.timeout, error:
            print "Socket Timout: %r" % error
        finally:
            response = urllib2.urlopen(URL)
    
        html = response.read()
        response.close() 
        
        soup = BeautifulSoup(html)
        title = soup.title.string
        created = modified = time.time()
        page = Page(html, docurl, title, created, modified)
        self.pages.append(page)
        
        for link in soup.find_all('a'):
            url = link.get('href')
            #print url
           # print self.start_url
            if url.startswith('/') or url.startswith(self.start_url):
                if url.startswith('/'):
                    url = self.start_url + url[1:]
                if url not in [page.url for page in self.pages]:
                    print url
                    #time.sleep(5) 
                    self.initSpider(url)
        
    
    