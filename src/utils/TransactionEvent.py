'''
Created on Jan 18, 2018

@author: Admin
'''
from utils.TransactionChannel import TransactionChannel

class TransactionEvent(object):
    '''
    classdocs
    '''
   
   
    transactionAmount=None
    tranactionType =None
    longitude = None
    latitude =  None
    narration = None
    transactionDate = None
    transactionRef =None
    paymentChannel =None
    debitAccount = None
    creditAccount = None
    

    def __init__(self, transactionAmount,transactionType,longitude,latitude,narration,transactionDate,transactionRef,paymentChannel, debitAccount,creditAccount):
        '''
        Constructor
        '''
        self.transactionAmount =transactionAmount
        self.tranactionType = transactionType
        self.longitude = longitude
        self.latitude = latitude
        self.narration = narration
        self.transactionDate =transactionDate
        self.transactionRef = transactionRef
        self.paymentChannel = paymentChannel
        self.debitAccount = debitAccount
        self.creditAccount = creditAccount
        self.transactionRef = transactionRef
        
        