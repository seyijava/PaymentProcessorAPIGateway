'''
Created on Jan 11, 2018

@author: Admin
'''
from pandocfilters import Para
import abc

class ITransactionService(object, metaclass=abc.ABCMeta):
   
    '''
    pass
    classdocs
    '''



    @abc.abstractmethod
    def createCustomer(self,param):
        raise NotImplementedError('users must define createCustomer to use this base class')

    @abc.abstractmethod 
    def createAccount(self,param):
        raise NotImplementedError('users must define createCustomer to use this base class')
   
    
    @abc.abstractmethod
    def saveEntity(self,param):
        raise NotImplementedError('users must define createCustomer to use this base class')
    
    def getAccountDetails(self,param):
        pass
    
    
    @abc.abstractmethod
    def transfer(self,param):
        raise NotImplementedError('users must define transfer to use this base class')
   
    
    @abc.abstractmethod
    def findBranchById(self,param):
        raise NotImplementedError('FindBranchId Must be implemented in sub class')
     
    @abc.abstractclassmethod
    def findAllTransction(self):
        raise NotImplementedError("FinallAllTransaction must be implemented by subclass")   
    
   
    
    @abc.abstractclassmethod
    def getBalance(self,acctNumber):
        raise NotImplementedError('getBalance must be implemented by subclass')
    
    @abc.abstractclassmethod
    def createCard(self,acctNumber):
        raise NotImplementedError('createCArd must be implemented by sublcass')