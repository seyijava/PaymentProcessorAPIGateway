'''
Created on Jan 11, 2018

@author: Admin
'''


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DateTime,Sequence
from model import Base
from sqlalchemy import inspect

class Customer(Base.Base):
    __tablename__ = 'customertbl'
    
    id = Column(Integer, Sequence('customer_id_seq'), primary_key=True)
    customerNumber=Column(String(4000),nullable = False)
    username =Column(String(16))
    password =Column(String(16))
    name=Column(String(4000))
    surname=Column(String(4000))
    gender=Column(String(10))
    nationality=Column(String(4000))
    dob=Column(DateTime)
   
        
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
       