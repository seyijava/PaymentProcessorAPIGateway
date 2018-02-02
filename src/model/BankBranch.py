'''
Created on Jan 11, 2018

@author: Admin
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Sequence
from model import Base
from sqlalchemy import inspect
import json
from utils import Serializer

class BankBranch(Base.Base,Serializer.Serializer):
    '''
    classdocs
    '''
    branchId = None
    __tablename__ = 'bankBranch'
    __public__ = ['branchId', 'name', 'location', 'descrption','address']

    branchId = Column(Integer, Sequence('branch_id_seq'), primary_key=True)
    name=Column(String(4000))
    location=Column(String(4000))
    descrption=Column(String(4000))
    address=Column(String(4000))
    
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    
    def as_json(self):
        return json.dumps(self.to_serializable_dict(),cls=self.alchemyencoder())   