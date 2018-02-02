'''
Created on Jan 12, 2018

@author: Admin
'''



from utils import TransType

class TransactionHistory(object):
    '''
    classdocs
    '''
    debitAccountNumber=None
    creditAccountNumber=None
    transactiontype=None
    transactionAmount=None
    transactionDate=None;
    transactionFlow=None 
    

    def __init__(self, debitAccount,creditAccount,transactionType,transactionDate,amount,transflow):
        '''
        Constructor
        '''
        self.creditAccountNumber =creditAccount
        self.debitAccountNumber = debitAccount
        self.transactiontype = transactionType
        self.transactionDate = transactionDate
        self.transactionAmount = amount
    
        self.transactionFlow = transflow
        
        