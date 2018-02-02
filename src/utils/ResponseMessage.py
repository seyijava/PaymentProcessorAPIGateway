'''
Created on Jan 15, 2018

@author: Admin
'''
import code

class ResponseMessage(object):
    '''
    classdocs
    '''
    respoonseCode = None
    reponseMessage = None

    def __init__(self, code,msg):
        '''
        Constructor
        '''
        self.respoonseCode = code
        self.reponseMessage = msg
        