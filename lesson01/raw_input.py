#!/usr/bin/python

import sys
thisyear = 2015
n = 'alex'
while True:
    name = raw_input("please input your name:").strip()
    if len(name) == 0:
        print 'err name,try again!'
        continue
    for i in range(1,3):
        name = raw_input("please input your name:").strip()
        if name == n:
            pass
        else:
            print "%s is not a valid user,please try again!"%name
            continue
        break
    else:
        print "gun"
        sys.exit()
    break
age = input("how old are you:")

print "hello",name,'\n'
print "you are",age,'years old!'
print thisyear - age
if age < 25:
    print "xiuxi"
elif age == 26:
    print 'as you are at the right age'
else:
    print "shangban"
