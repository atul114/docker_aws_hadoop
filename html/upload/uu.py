#!/usr/bin/python2
import  cgi
import time
import commands
import os

print commands.getoutput(' ssh -i /root/Downloads/2ndjune.pem ec2-user@35.160.122.74')
print commands.getoutput(' sudo -i')
print commands.getoutput(' whoami')
