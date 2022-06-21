#!/usr/bin/python3
import os
from urllib.parse import parse_qs

qString = os.environ['QUERY_STRING']
qVal = parse_qs(qString)
name = qVal['name'][0]
passwd = qVal['passwd'][0]
responseBody = '<HTML><BODY><H1> Hello ' + name +\
                '<BR> Your password is ' + passwd +\
                '</H1></BODY></HTML>'
print(responseBody)
