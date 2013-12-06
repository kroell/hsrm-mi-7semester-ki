'''
Created on 06.12.2013

@author: soerenkroell
'''

from model import Spider


URL = 'http://www.spiegel.de/'



if __name__ == '__main__':

    URL = 'http://www.spiegel.de/'
    spider = Spider(URL)
    print "start crawling...\n"
    spider.initSpider(URL)
    print "\n...finished crawling"
    spider.preparePage()
    
    print len(spider.pages) #330