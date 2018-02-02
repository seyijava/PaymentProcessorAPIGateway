'''
Created on Jan 11, 2018

@author: Admin
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Float,Sequence
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from model import Customer
from model import Base 
from sqlalchemy import inspect

class Account(Base.Base):
   
    __tablename__ = 'accounttbl'

    id = Column(Integer, Sequence('account_Id_seq'), primary_key=True)
    acctNumber=Column(String(4000), nullable = False)
    amount=Column(Float,nullable = False)
    accountType=Column(String(4000),nullable = False)
    customer_id=Column(Integer,ForeignKey('customertbl.id'),nullable=False)
    
    customer = relationship("Customer")
   
    
    
       
    
    

   