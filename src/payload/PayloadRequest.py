'''
Created on Jan 14, 2018

@author: Admin
'''
from datetime import datetime

class PayloadRequest(object):
    '''
    classdocs
    '''
    def __init__(self, dict_):
        self.__dict__.update(dict_)
        
    