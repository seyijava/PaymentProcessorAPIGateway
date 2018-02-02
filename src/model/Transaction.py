'''
Created on Jan 11, 2018

@author: Admin
'''

from sqlalchemy import Column, Integer, String,Float,Sequence,DateTime

from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from model import Base
from model import Account

from utils import TransactionChannel
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy import inspect

class Transaction(Base.Base):
    '''
    classdocs
    '''
    __tablename__ = 'transactiontbl'
    
    id = Column(Integer, Sequence('transaction_id_seq'), primary_key=True)
    transactionAmount=Column(Float, nullable = False)
    tranactionType =Column(String(4000),nullable = False)
    debitAccount_id =Column(Integer, ForeignKey('accounttbl.id'),nullable = False )
    creditAccount_id =Column(Integer, ForeignKey('accounttbl.id'),nullable = False)
    longtitute = Column(Float)
    latitutue =  Column(Float)
    narration = Column(String(4000))
    transactionDate =Column(DateTime)
    transactionRef =Column(String(4000))
    
    transactionChannel =Column(ENUM('ATM','POS','MOBILE','BRANCH','USSD','WIRETRANSFER','INTERNETBANKING'),nullable=False)
   
    
  
    debitAccount = relationship("Account", foreign_keys="[Transaction.debitAccount_id]")
    creditAccount = relationship("Account", foreign_keys="[Transaction.creditAccount_id]")
    
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
    
    