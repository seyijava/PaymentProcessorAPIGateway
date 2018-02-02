'''
Created on Jan 15, 2018

@author: Admin
'''
from flask import make_response
import json
JSON_MIME_TYPE = 'application/json'




def json_response(data='', status=200, headers=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE

    return make_response(data, status, headers)

def buildResponseMessage(_dic):
    data = json.dumps(_dic)
    return json_response(data)