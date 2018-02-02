'''
Created on Jan 13, 2018

@author: Admin
'''
from enum import Enum

class TransType(Enum):
    '''
    classdocs
    '''


    def __str__(self):
             return str(self.value)
    CREDIT = 'CR'
    DEBIT =  'DR'
  
        
        