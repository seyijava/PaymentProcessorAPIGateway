'''
Created on Jan 11, 2018

@author: Admin
'''
from flask import Flask, jsonify, abort, request, make_response, url_for,g
from services import TransactionService
import json
from payload import PayloadRequest
from utils import HttpUtil,Validator
from exceptions import NotFoundException
from utils import ResponseMessage
from utils import BalanceResponse
from model import Customer
from utils import Utility
import schedule
import time
from persistqueue import Queue;




#from model import Account
#from model import Customer
#from model import BankBranch
#from model import Transaction
#from utils import TransactionHistory


app = Flask(__name__)



 
@app.route('/bank/api/transfer', methods=['POST'])
def fundTranfer():
       
        if not request.json or  request.content_type != HttpUtil.JSON_MIME_TYPE:
            abort(400)
        payload = request.json
        result = Validator.validateTransferRequest(payload)
        if isinstance(result, str):
            print(result)
            return HttpUtil.json_response(result)
        else: 
            try:  
                payloadRequest = PayloadRequest.PayloadRequest(payload)
                transactionService = TransactionService.TransactionService()
                transfRef = transactionService.transfer(payloadRequest)
                msgReponse = 'Transaction Ref {}'.format(transfRef)
                responseMsg = ResponseMessage.ResponseMessage('00',msgReponse)
                return  HttpUtil.buildResponseMessage(responseMsg .__dict__)
            except NotFoundException.NotFoundException:
                responseMessage = ResponseMessage.ResponseMessage('99','Account Not Found')
                return  HttpUtil.buildResponseMessage(responseMessage.__dict__)
           
       ## HttpUtil.json_response(result, 400)
               ##self.transactionService.deposit(param)

@app.route('/bank/api/createacct', methods=['POST'])
def createAccount():
     if not request.json or request.content_type != HttpUtil.JSON_MIME_TYPE:
       abort(400)
     payload = request.json
     result = Validator.validateAccountRequest(payload)
     if isinstance(result,str):
        print(result)
        return HttpUtil.json_response(result)
     else:
          try:
              payloadRequest = PayloadRequest.PayloadRequest(payload)
              transactionService = TransactionService.TransactionService()
              account =  transactionService.createAccount(payloadRequest.customerNumber)
              msgReponse = 'Account Number{}'.format(account.acctNumber)
              responseMsg = ResponseMessage.ResponseMessage('00',msgReponse)
              return HttpUtil.buildResponseMessage(responseMsg.__dict__)
          except NotFoundException.NotFoundException:
             responseMessage = ResponseMessage.ResponseMessage('99','Customer Not Found')
             return  HttpUtil.buildResponseMessage(responseMessage.__dict__)
           

@app.route('/bank/api/createcustomer',methods=['POST'])
def createCustomer():
    if not request.json or request.content_type != HttpUtil.JSON_MIME_TYPE:
        abort(400)
    payload = request.json
    result = Validator.validateCustomer(payload)
    if isinstance(result,str):
        print(result)
        return HttpUtil.json_response(result)
    else:
        transactionService = TransactionService.TransactionService()
        payloadRequest = PayloadRequest.PayloadRequest(payload)
        customer = Customer.Customer()
        customer.gender = payloadRequest.gender
        customer.name = payloadRequest.name
        customer.surname = payloadRequest.surname
        customer.nationality = payloadRequest.nationality
        customer.customerNumber = Utility.random_generator(9)
        customer = transactionService.createCustomer(customer)
        msgReponse = 'Customer S/N {}'.format(customer.customerNumber)
        responseMsg = ResponseMessage.ResponseMessage('00',msgReponse)
        return HttpUtil.buildResponseMessage(responseMsg.__dict__)

@app.route('/bank/api/balance', methods=['POST'])
def checkBalance():
    if not request.json or request.content_type != HttpUtil.JSON_MIME_TYPE:
        abort(400)
    payload = request.json
    result = Validator.validateAccountNumberRequest(payload)
    if isinstance(result,str):
        print(result)
        return HttpUtil.json_response(result)
    else:
         try:
              payloadRequest = PayloadRequest.PayloadRequest(payload) 
              transactionService = TransactionService.TransactionService()
              balance = transactionService.getBalance(payloadRequest.accountNumber)
              reponseBalance = BalanceResponse.BalanceReponse(balance,balance)
              return HttpUtil.buildResponseMessage(reponseBalance.__dict__)
         except NotFoundException.NotFoundException:
             responseMessage = ResponseMessage.ResponseMessage('99','Account Not Found')
             return  HttpUtil.buildResponseMessage(responseMessage.__dict__)
               


@app.route('/bank/api/createcard',methods=['POST'])
def createCard():
    if not request.json or request.content_type != HttpUtil.JSON_MIME_TYPE:
        abort(400)
    payload = request.json
    result = Validator.validateAccountNumberRequest(payload)
    if isinstance(result,str):
        print(result)
        return HttpUtil.json_response(result)
    else:
        try:
        
            transactionService = TransactionService.TransactionService()
            payloadRequest = PayloadRequest.PayloadRequest(payload)
        
            card = transactionService.createCard(payloadRequest.accountNumber)
            msgReponse = 'CardNumber {}   {}'.format(card.cardNumber,card.cardType)
            responseMsg = ResponseMessage.ResponseMessage('00',msgReponse)
            return HttpUtil.buildResponseMessage(responseMsg.__dict__) 
        except NotFoundException.NotFoundException:
             responseMessage = ResponseMessage.ResponseMessage('99','Account Not Found')
             return  HttpUtil.buildResponseMessage(responseMessage.__dict__)  
         
         
       
       
        #messageProducer = MessageProducer.MessageProducer()
        #messageProducer.sendMessageToKafka(message)
             
    
    def sendToQueue(self,message):
        queue = Queue("C:\\BigDataPlatform\\Projects\\bigdata\\Queue")
        queue.put_nowait(message)
        
    
   
     
    
               
if __name__ == '__main__':
            app.run(debug = True)
                       