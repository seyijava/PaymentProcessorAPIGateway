'''
Created on Jan 16, 2018

@author: Admin
'''




from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DateTime,Sequence
from model import Base
from sqlalchemy import inspect
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import ENUM

class CardDetails(Base.Base):
    __tablename__ = 'cardDetailstbl'
    
    id = Column(Integer, Sequence('card_id_seq'), primary_key=True)
    cardNumber=Column(String(4000),nullable = False)
    cardType =Column(ENUM('VISA','MASTER','AMEX','DISCOVERY'),nullable=False)
    account_id=Column(Integer,ForeignKey('accounttbl.id'),nullable=False)
    
    account = relationship("Account", foreign_keys="[CardDetails.account_id]")
    
    
   
