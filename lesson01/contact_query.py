#!/usr/bin/env python
import sys
a = 0
while True:
    if a < 3:
        input = raw_input("Please input your username:")
        if input == 'Alex':
            password = raw_input("please input your pass:")
            p = '123'
            while password != p:
                password =raw_input("Wrong passwd,input again:" )
            else:
                print 'Welcome login to TriAquae!\n'
                while True:
                    match_yes = 0
                    input = raw_input("\033[32mPlease input the name whom you want to search:\033[0m")
                    contact_file = file('contact_list.txt')
                    while True:
                        line = contact_file.readline()
                        if len(line) == 0:break
                        if input in line:
                            print 'Match item: \033[36;1m%s\033[0m' % line
                            match_yes = 1
                        if input == 'quit':
                            print "\033[31mis logout\033[0m"
                            sys.exit()
                    else:
                        pass

                    if match_yes == 0 :print 'No match item found.'
        else:
            print "Sorry, user %s not found" % input
            a += 1
            continue
        break
    else:
        sys.exit()
