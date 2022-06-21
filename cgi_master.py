#!/usr/bin/python3
import subprocess

qString = "name=Hong+Gildong&passwd=1234"
prog = "./cgi_post_slave.py"
try:
    proc = subprocess.Popen([prog], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
except Exception as e:
    print(e)
responseBody = proc.communicate(qString.encode())[0]
print(responseBody)
