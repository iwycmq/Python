#!/usr/bin/python

import sys

logintry = 0
passwdtry = 0
trueuser = "yufei"
while True:
    if logintry < 3:
        username = raw_input("\033[34mplease input your name:\033[0m")
        if username == trueuser:
            password = raw_input("\033[34mplease input your password:\033[0m")
            passwd = '123'
            while password != passwd:
                if passwdtry < 2:
                    password =raw_input("\033[33mWrong passwd,input again:\033[0m" )
                    passwdtry += 1
                else:
                    print "\033[31mSorry your passwd frequency over 3 times\033[0m"
                    sys.exit()
            else:
                print "\033[32mWelcome yufei!\033[0m"
                c = raw_input("\033[31mInput operate \033[0m\033[32mquery/\033[0m\033[34madd/\033[0m\033[35mdel/\033[0m\033[36mmodify/\033[0m\033[37minsert/\033[0m\033[31mquit:\033[0m")
                while True:
                    if c == "query":
                        f = file('contact_list.txt')
                        c = f.readlines()
                        while True:
                            query_input = raw_input("\033[36mPlease input something to search:\033[0m")
                            if len(query_input) == 0:continue
                            if query_input == 'exit':break
                            for line in c:
                                if query_input in line:
                                    print 'Match item: \033[36;1m%s\033[0m' % line
                    elif c == "add":
                        print '''\033[31maccording to the following pattern imput:'name	department	contact \033[0m'''
                        while True:
                            add_info = raw_input("\033[32mplease add your information:\033[0m").strip()
                            if len(add_info) == 0:continue
                            items_num = len(add_info.split('\t'))
                            if add_info == "exit":break
                            if items_num == 3:
                                f = open('contact_list.txt')
                                c = f.readlines()
                                sn = len(c) +1
                                f.close()
                                f = open('contact_list.txt','a')
                                f.write('%d	%s\n' %(sn,add_info))
                                f.close()
                                print'%d	%s\n' %(sn,add_info)
                                continue
                            else:
                                print "\033[31mplease input the right pattern\033[0m"
                    elif c == "del":
                        pass
                    elif c == "modify":
                        pass
                    elif c == "insert":
                        pass
                    elif c == "quit":
                        print "Bye!"
                        sys.exit()
                    else:
                        c = raw_input("\033[31mWrong operate,input again:\033[0m\033[32mquery/\033[0m\033[34madd/\033[0m\033[35mdel/\033[0m\033[36mmodify/\033[0m\033[37minsert/\033[0m\033[31mquit\033[0m")
                        continue
        elif len(username) == 0:
            print "\033[33mSorry,your name is empty\033[0m"
            logintry += 1
            continue
        else:
            print "\033[33mSorry, user %s not found\033[0m" % username
            logintry += 1
            continue
    else:
        print "\033[31mSorry,input frequency over 3 times\033[0m"
        sys.exit()

