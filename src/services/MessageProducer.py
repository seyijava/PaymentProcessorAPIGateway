'''
Created on Jan 16, 2018

@author: Admin
'''

from kafka import KafkaProducer
import configparser

import logging
import asyncio
import os
import threading,logging,time
import json
import datetime


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            encoded_object = list(obj.timetuple())[0:6]
        else:
            encoded_object =json.JSONEncoder.default(self, obj)
        return encoded_object

class MessageProducer(threading.Thread):
    
    
    logging.basicConfig(level=logging.DEBUG)
    '''
    classdocs
    '''
    topic = ''
    kafkaAddress = ''
    message  = ''

    def __init__(self,message):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        self.stop_event = threading.Event();
        
        config = configparser.ConfigParser()
        config.read(r"C:\\BigDataPlatform\\Projects\\bigdata\\CreditCardTransactionGenerator\\src\\app.ini")
        self.kafkaAddress =  config['kafka']['address']
        self.topic = 'IncomingTrasactionEventsTopic'
        self.message = message;
       
     
    def run(self): 
        ##try: 
            print(self.message)
            print(self.kafkaAddress)
            producer = KafkaProducer(bootstrap_servers=['192.168.0.100:9092'],api_version=(0,10),value_serializer=lambda v: json.dumps(v).encode('utf-8'))
            producer.send(self.topic, self.message) 
            producer.close()
                  
       ##### except:
            ## print("hllo")
     
    def stop(self):
         self.stop_event.set()   