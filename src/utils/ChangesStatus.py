'''
Created on Jan 13, 2018

@author: Admin
'''

class ChangesStatus(object):
    '''
    classdocs
    '''
    status =None
    message=None

    def __init__(self, status,message):
        '''
        Constructor
        '''
        self.message =message
        self.status = status
        