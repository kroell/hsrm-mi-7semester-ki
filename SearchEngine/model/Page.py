'''
Created on 06.12.2013

@author: soerenkroell
'''

class Page(object):
    '''
    classdocs
    '''

    def __init__(self, html=None, url=None, title=None, created=None, modified=None):
        '''
        Constructor
        '''
        self.html = html
        self.url = url
        self.title = title
        self.created = created
        self.modified = modified
    

