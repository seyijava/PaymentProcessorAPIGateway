'''
Created on Jan 11, 2018

@author: Admin
'''
from services.ITransactionService import ITransactionService
from dao import BankDao
from exceptions import NotFoundException
from flask.globals import session
from model import Transaction
from model import Account
from werkzeug.exceptions import NotFound
from utils import Utility
from model import CardDetails
from utils import CreditCardGenerator
import random
from distutils.log import info
from click.types import BoolParamType
import datetime
from services import MessageProducer
import asyncio
import os
from utils.TransactionEvent import TransactionEvent
import concurrent.futures
from concurrent.futures._base import Executor
from datetime import datetime,timedelta
import time

class TransactionService(ITransactionService):
    '''
    classdocs
    '''

    bankDao = None

    def __init__(self):
        '''
        Constructor
        '''
        self.bankDao = BankDao.BankDao() 
       
    def saveEntity(self,param):
         with self.bankDao.session_scope() as session:
                   entity = self.bankDao.saveEntity(session,param)
                   
         return entity, session
     
    
    def findBranchById(self,param):
         with self.bankDao.session_scope() as session:
               branch = self.bankDao.findBranchById(session, param)
               if branch is None:
                   raise NotFoundException.NotFoundException('Branch not found')
                  
         return branch
    def findAllTransction(self):
        with self.bankDao.session_scope() as session:
            transactionList = self.bankDao.findAllTransction(session);
            return transactionList
        
        

            
            
    def getBalance(self,acctNumber):
        with self.bankDao.session_scope() as session:
            account = self.bankDao.findAccountByAcctNumber(session, acctNumber)
            if account is None:
               raise  NotFoundException.NotFoundException('Account Not Found')
            return account.amount
   
    
    def createCustomer(self,param):
       customer,session =  self.saveEntity(param)
       return customer
    
    
    def createAccount(self,customerNumber):
          with self.bankDao.session_scope() as session:
              customer = self.bankDao.findCustomerByNumber(session, customerNumber)
              if customer is None:
                  raise NotFoundException.NotFoundException('Customer Not Found')
              else:
                  account = Account.Account()
                  account.acctNumber = str(Utility.generateRandmonNumber(10))
                  account.amount = 10000.00
                  account.accountType = 'SAVINGS'
                  account.customer = customer
                  session.add(account)
                 
                  return account
   
    
    
   
    def createCard(self,acctNumber):  
        with self.bankDao.session_scope() as session:
              account = self.bankDao.findAccountByAcctNumber(session, acctNumber)
              if account is None:
                  raise NotFoundException.NotFoundException('account Not Found')
              else:
                  cardList = ['VISA','MASTER','AMEX','DISCOVERY']
                  cardtype = random.choice(cardList)
                  
                  card  = CardDetails.CardDetails()
                  card.account = account
                  creditCardGenerator = CreditCardGenerator.CreditCardGenerator();
                  if cardList[0] == cardtype:
                      cardNum = creditCardGenerator.credit_card_number(creditCardGenerator.generator, creditCardGenerator.visaPrefixList, 16, 1)
                      card.cardNumber = int(float(cardNum[0]))
                      card.cardType = cardtype
                  if cardList[1] == cardtype:
                      cardNum = creditCardGenerator.credit_card_number(creditCardGenerator.generator, creditCardGenerator.mastercardPrefixList, 16, 1)
                      card.cardNumber = int(float(cardNum[0]))
                      card.cardType = cardtype
                  if cardList[2] == cardtype:
                      cardNum = creditCardGenerator.credit_card_number(creditCardGenerator.generator, creditCardGenerator.amexPrefixList, 16, 1)
                      card.cardNumber = int(float(cardNum[0]))
                      card.cardType = cardtype
                  if cardList[3] == cardtype:
                      cardNum  = creditCardGenerator.credit_card_number(creditCardGenerator.generator, creditCardGenerator.discoverPrefixList, 16, 1)
                      card.cardNumber = int(float(cardNum[0]))
                      card.cardType = cardtype
                  session.add(card)
                 
                  return card 
              
    
    def transfer(self,transferRequest):
        debitAcct = transferRequest.debitAccountNumber
        creditAcct = transferRequest.creditAccountNumber
        amt = transferRequest.amount
        narration = transferRequest.narration;
        paymentChannel = transferRequest.paymentChannel
        transType = transferRequest.transType
        latitude = transferRequest.latitude
        logitude = transferRequest.longitude
        with self.bankDao.session_scope() as session:
            debitaccount = self.bankDao.findAccountByAcctNumber(session, debitAcct)
        if debitaccount is None:
            raise NotFoundException.NotFoundException('account Not Found')
        creditAccount = self.bankDao.findAccountByAcctNumber(session, creditAcct)
       
        if creditAccount is None:
            raise NotFoundException.NotFoundException('account Not Found')
        inflowTransaction = Transaction.Transaction()
        inflowTransaction.creditAccount = creditAccount
        inflowTransaction.debitAccount = debitaccount
        inflowTransaction.transactionAmount = amt
        inflowTransaction.transactionChannel = paymentChannel
        inflowTransaction.tranactionType = transType
        latitude,logitude = Utility.generateGeoLocation();
        inflowTransaction.latitutue = latitude
        inflowTransaction.longtitute = logitude
        inflowTransaction.transactionDate = datetime.now()
        inflowTransaction.narration = narration
        inflowTransaction.transactionRef = 'FT-' + str(Utility.generateRandmonNumber(15))
        self.bankDao.saveEntity(session, inflowTransaction)
        current_timestamp = time.time()
       
        datetime_ts = datetime.fromtimestamp( current_timestamp).strftime('%Y-%m-%d %H:%M:%S')
        transactionEvent = TransactionEvent(inflowTransaction.transactionAmount,inflowTransaction.tranactionType,inflowTransaction.longtitute,inflowTransaction.latitutue,inflowTransaction.narration,datetime_ts,inflowTransaction.transactionRef,inflowTransaction.transactionChannel,inflowTransaction.debitAccount.acctNumber,inflowTransaction.creditAccount.acctNumber)
      
        self.sendMessage(transactionEvent.__dict__)
             
        return inflowTransaction.transactionRef  
     
     
     
    def sendMessage(self,message):
       
        messageProducer = MessageProducer.MessageProducer(message)
        messageProducer.start()
             
    