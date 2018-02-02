'''
Created on Jan 11, 2018

@author: Admin
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

from sqlalchemy import Column, Integer, String
from sqlalchemy_dao import Model

class BaseDao(object):
    '''
    classdocs
    '''
   
    session = None
    engine = None

    def __init__(self):
        '''
        Constructor
        '''
        self.engine = create_engine('sqlite:///:memory:', echo=True)
        Session  = sessionmaker(bind=self.engine)
        self.session = Session()
        
        
    def createSession(self):
       
        return self.session   
        