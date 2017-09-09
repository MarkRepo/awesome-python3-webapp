#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Default configuration.
'''

__author__ = 'Mark Wu'

configs = {
        'debug': True,
        'db': {
            'host': '127.0.0.1',
            'port':3306,
            'user':'www',
            'password':'www',
            'db':'awesome'
            },
        'session':{
            'secret':'Awesome'
            }
        
        }
