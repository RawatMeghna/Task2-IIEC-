#! /usr/bin/python3

print("Content-type: text/html")
print()

import os
import sys
import subprocess
import cgi 

cmd = cgi.FieldStorage()
value = cmd.getvalue('cmd')

flag = True

choice = value
if ('date' in choice.lower()) or ('month' in choice.lower()) or ('year' in choice.lower()):
	result = subprocess.getoutput('date')
	print(f"Today's date is: {result}")
	
elif ('calender' in choice.lower()) or ('cal' in choice.lower()):
	result = subprocess.getoutput('cal')
	print(f"This Month Calender: {result}")
	
elif ('ifconfig' in choice.lower()) or ('what is my ip address' in choice.lower()):
	result = subprocess.getoutput('ifconfig')
	print(f"Your ip address is: {result}")

elif ('view system profile' in choice.lower()) or ('show profile' in choice.lower()):
	result = subprocess.getoutput('sosreport')
	print(result)

elif ('configure system language' in choice.lower()) or ('language' in choice.lower()):
	result = subprocess.getoutput('localectl')
	print(result)

elif ('configure network' in choice.lower()) or ('network' in choice.lower()):
	result = subprocess.getoutput('nmcli')
	print(result)

elif ('configure hostname' in choice.lower()) or ('hostname' in choice.lower() or ('what is server hostname' in choice.lower()):
	result = subprocess.getoutput('hostnamectl')
	print(result)

else:
	print("we can't understand what you are asking")