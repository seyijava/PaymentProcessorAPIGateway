'''
Created on Jan 16, 2018

@author: Admin
'''

from setuptools import setup



setup(name='BankPython',
      version='0.1',
      description='Bank Python is bank simulator that has an API Gateway. It has the following transaction type 1. Balance Enquiry, Deposit, Create Customer, Create Account, Withdrawer etc',
      author = 'Otun Oluwaseyi',
      author_email='seyijava@mgmail.com',
      license='MIT',
      packages=['controller','dao','exceptions','main','model','payload','services','utils'],
      install_requires=['sqlalchemy','flask'],
      zip_safe=False
      
      )
