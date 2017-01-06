#!/usr/bin/python

try:
   a=int(raw_input("a= "))
   b=int(raw_input("b="))
   c=a/b
		
except ZeroDivisonError:
   print "Cannot divide by zero"
else:
   print "a\\b=", a/b
