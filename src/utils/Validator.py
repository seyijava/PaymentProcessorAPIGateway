'''
Created on Jan 15, 2018

@author: Admin
'''
import json
from utils import HttpUtil
from _dummy_thread import error
import payload

def validateTransferRequest(payload):
    if not all([payload.get('debitAccountNumber'), payload.get('creditAccountNumber'), payload.get('narration'),payload.get('paymentChannel'),payload.get('transType'),payload.get('amount'), payload.get("latitude"),payload.get("longitude")]):
        error = json.dumps({'error': 'Missing field/s (debitAccountNumber, creditAccountNumber,narration,paymentChannel,transType,amount,latitude)'})
        return error
    else:
        return True 
    
def validateAccountRequest(payload):
    if not all([payload.get('customerNumber')]):
        error = json.dumps({'error': 'Missing Fields (customerNumber)'})
        return error
    else:
       return True   
   
def validateCustomer(payload):
    if not all([payload.get('name'),payload.get('surname'), payload.get('gender'),payload.get('nationality'),payload.get('dob')]):
        
        error = json.dumps({'error':'Missing Fields (name,surname,gender,nationality,dob)'})
        return error
    else:
       return True
   
def validateAccountNumberRequest(payload):
    if not all([payload.get('accountNumber')]):
        error = json.dumps({'error': 'Missing Fields (accountNumber'})
        return error
    else:
        return True
