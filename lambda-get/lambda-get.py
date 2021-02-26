#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 15:55:25 2021

@author: axel

Return the number of the person using the name provided as argument
"""

import json

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    # myFile = open('contacts.txt','r')
    # for ligne in myFile:
    #     if name in ligne:
    #         number = ligne
    #         print(ligne)
    #         break
    # myFile.close()
    # return number
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello, CDK! You have hit {}\n'.format(event['path'])
    }
