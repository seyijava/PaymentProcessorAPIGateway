'''
Created on Jan 12, 2018

@author: Admin
'''
from dao import  BankDao
from  model import Account
from model import Transaction
from model.Customer import Customer
from model import BankBranch
from sqlalchemy.dialects.mysql import ENUM
from services import TransactionService
import json
from sqlalchemy.ext.serializer import loads, dumps

if __name__ == '__main__':
    
    transactionService = TransactionService.TransactionService()
    actyp = '99ddd'
    account = Account.Account(accountType=actyp)
    transaction = Transaction.Transaction(transactionChannel='ATM')
    customer = Customer()
    bankBranch = BankBranch.BankBranch(address=actyp)
    transssd= bankBranch.as_json()
    
    print(transssd)
    #bankDao.saveEntity(bankBranch)
    branch= transactionService.findBranchById(11)
    serialized_obj = branch.toDict()
    jsondata=json.dumps(serialized_obj)
    print(jsondata)
    
    transactionList = transactionService.findAllTransction();
    trans= json.dumps([dict(r) for r in transactionList])
    print(trans)
   