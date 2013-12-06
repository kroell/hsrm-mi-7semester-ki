'''
Created on 06.12.2013

@author: soerenkroell
'''

from model import *

URL = 'http://www.spiegel.de/'
SHOP = 'http://www.spiegel.de/shop/'
pages = []


if __name__ == '__main__':
    #initPage(URL)
    URL = 'http://www.spiegel.de/'
    spider = Spider(URL)
    spider.initSpider(URL)

    