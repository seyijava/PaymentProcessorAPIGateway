'''
Created on Jan 13, 2018

@author: Admin
'''
from  enum import Enum
from sqlalchemy.dialects.mysql import ENUM

class TransactionChannel(ENUM):
    '''
    classdocs
    '''


    def __str__(self):
             return str(self.value)
    ATM = 1
    #POS = 'POS'
    #BRANCH='BRANCH'
    #INTERNETBANKING='INTERNETBANKING'
    #USSD = 'USSD'
    #MOBILE= 'MOBILE'
    #WIRETRANSFER = 'WIFERTRANSFER'
        
        