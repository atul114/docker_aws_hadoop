#!/usr/bin/python2
import  cgi
import time
import commands
import os

print  "content-type:text/html"
print  ""
data=cgi.FieldStorage()
print data
yyy='''
<head>
  <title>List of services provided : </title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="/static/c1.css">
  <script src="/static/j2.js"></script>
  <script src="/static/j3.js"></script>
</head>
<body>
<div class="container">
<h2>YOUR OPTIONS ARE:-</h2>
<p>Choose the desired</p>
'''
print yyy
f=open('@ippu','r')
ip=f.read().splitlines()
print  ip

#i=user
#pi=ip[user-1]
pi=ip[0]
print"namenode"
print pi
u1=data.getvalue('1')
u2=data.getvalue('2')
print u1
print u2
print pi
print commands.getoutput(" sudo ssh -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem ec2-user@"+pi+" sudo -i hdfs dfsadmin -setQuota "+u1+' '+u2)
print '<form method="post" action="/cgi-bin/@m6.py">'
print '<label><input type="submit" value="Click to perform more"></label>'
print '</form>'





