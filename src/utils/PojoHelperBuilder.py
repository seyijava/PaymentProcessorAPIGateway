'''
Created on Jan 13, 2018

@author: Admin
'''

from model import Account
from model import Transaction
from model import Customer
from utils import TransactionHistory
from utils.TransactionHistory import TransactionHistory
from model.Transaction import Transaction

class PojoHelperBuilder(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
     
    def resolveTransactionHistory(self,transaction):
         fromAcct = transaction.debitAccount.acctNumber
         toAcct = transaction.debitAccount.acctNumber
         transType = transaction.tranactionType
         amt = transaction.transactionAmount
         transDate = transaction.transactionDate
         transDirect = 999
         transactionHistory = TransactionHistory(debitAccount=fromAcct,creditAccount=toAcct,transactionType=transType,transactionDate=transDate,amount=amt,transflow=transDirect) 
         return transactionHistory  