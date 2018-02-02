'''
Created on Jan 15, 2018

@author: Admin
'''
import string
import random
from random import randint

SAVINGS = 'SAVINGS'
CURRENT = 'CURRENT'
CHECKING = 'CHECKING'

def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def generateRandmonNumber(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start,range_end)


def generateGeoLocation():
    latitude = 6.465422
    longitude = 3.406448
    dec_lat = random.random() / 100
    dec_log = random.random() / 100
    return round(latitude + dec_lat,4), round(longitude + dec_log,4)
