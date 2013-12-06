'''
Created on 06.12.2013

@author: soerenkroell
'''

import urllib2
import time
import socket
import nltk
from bs4 import BeautifulSoup
from model import *


URL = 'http://www.spiegel.de/'

class Spider(object):
    
    def __init__(self, start_url):
        '''
        Constructor
        '''
        self.start_url = start_url
        self.pages = []
    
    
    def initSpider(self, docurl):
    
        try:
            #response = urllib2.urlopen(docurl,timeout=5)
            response = urllib2.urlopen(docurl)
        except urllib2.HTTPError, error:
            print "HTTP error: %r" % error.code
            response = urllib2.urlopen(URL)
        except Exception, error:
            print "Error: %r" % error
            response = urllib2.urlopen(URL)

    
        html = response.read()
        response.close() 
        
        soup = BeautifulSoup(html)
        title = soup.title.string
        description = soup.find("meta", {"property":"og:description"})
        if(description):
            description = description['content']
        else:
            description = soup.find("meta", {"name":"description"})
            if (description):
                description = description['content']
        print description
        created = modified = time.time()
        page = Page(html, docurl, title, description, created, modified)
        self.pages.append(page)
        
        for link in soup.find_all('a'):
            url = link.get('href')
            if url.startswith('/') or url.startswith(self.start_url):
                if url.startswith('/'):
                    url = self.start_url + url[1:]
                if url not in [page.url for page in self.pages]:
                    print url
                    #time.sleep(5) 
                    self.initSpider(url)
        
    
    def preparePage(self):
        print len(self.pages)
        for page in self.pages:
            page.raw = nltk.clean_html(page.html)
            page.tokens = nltk.word_tokenize(page.raw)
  
        
    