'''
Created on Jan 11, 2018

@author: Admin
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from model import Account, BankBranch
from model import Transaction
from model import Customer 

from model import Base 
from contextlib import contextmanager


class BankDao(object):
    '''
    classdocs
    '''
  

    #session = None
    def __init__(self):
        '''
        '''
        
      
    # engine = create_engine('mysql://root:password@192.168.0.100/bankdb', echo=True)
        #Base.Base.metadata.create_all(engine)
       
        #Session  = sessionmaker(bind=engine)
        #self.session = Session()
       
        
    def saveEntity(self,session,param):
        session.add(param)
        session.commit()
        print(param.id)
        return param
        
         
        
        
    def findAccountById(self,session,param):
        return session.query(Account.Account).filter(Account.Account.id==param).first()

    def findCustomerByNumber(self,session,param):
        return session.query(Customer.Customer).filter(Customer.Customer.customerNumber == param).first() 
    
    def findAccountByAcctNumber(self,session,param):
        return session.query(Account.Account).filter(Account.Account.acctNumber== param).first()   
    
    
    def findAllAccount(self,session):
        return session.query(Account).all() 
    
    def findTansactionById(self,session,param,):
        return session.query(Transaction.Transaction).filter(Transaction.Transaction.id==param).first() 
    
    def findAllTransction(self,session):
        return session.query(Transaction.Transaction).all()
    
    def findBranchById(self,session,param):
        
        return session.query(BankBranch.BankBranch).filter(BankBranch.BankBranch.branchId == param).first()
    

    @contextmanager
    def session_scope(self):
        engine = create_engine('mysql://root:password@192.168.0.100/bankdb', echo=True)
        Base.Base.metadata.create_all(engine)
       
        Session  = sessionmaker(bind=engine)
        session = Session()
        try:
            yield session
           
            session.commit()

        except:
            session.rollback()
            raise
        finally:
            print('close')
            ##session.close()
    
    