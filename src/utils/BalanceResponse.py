'''
Created on Jan 15, 2018

@author: Admin
'''

class BalanceReponse(object):
    '''
    classdocs
    '''

    responseCode = None
    responseMessage = None
    availableBalance = None
    legerBalance = None
    def __init__(self,availableBalance,legerBalance, responseCode='00',responseMessage='SUCCESSFULL'):
        '''
        Constructor
        '''
        self.responseCode = responseCode
        self.availableBalance = availableBalance
        self.legerBalance = legerBalance
        self.reponseMessage = responseMessage
        
        