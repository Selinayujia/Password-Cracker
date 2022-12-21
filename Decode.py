#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:55:12 2019

@author: selina
"""

import hashlib 
#import itertools
   
common_pwd = open("commonPwd.txt",'r',encoding = 'utf-8')
pwd_lst = common_pwd.readlines()


linkedin = open("linkedin.txt",'r',encoding = 'utf-8')
linkedin = linkedin.readlines() 


formspring = open("formspring.txt",'r',encoding = 'utf-8')
formspring = formspring.readlines() 



#eharmony = open("eharmony.txt",'r',encoding = 'utf-8')
#eharmony = eharmony.readlines() 
#
#crack_eharmony_hashed = []
#for i in range(len(pwd_lst)):
#    crack_eharmony_hashed.append((hashlib.md5((pwd_lst[i][:-1].upper()).encode('utf-8')).hexdigest()))
    
    
#crack_formspring_hashed = []    
#salt_pwd_lst = []
#for i in range(len(pwd_lst)):
#    for salt in [str(j).zfill(2) for j in range(100)]:
#        salt_pwd_lst.append (salt+pwd_lst[i])
#for i in range(len(pwd_lst)):
#    crack_formspring_hashed.append((hashlib.sha256((salt_pwd_lst[i][:-1]).encode('utf-8')).hexdigest()))
#    
#    
crack_linkedin_hashed = []
for i in range(len(pwd_lst)):
    step = (hashlib.sha1((pwd_lst[i][:-1]).encode('utf-8')).hexdigest())
    head = "00000"
    final = head + step[5:]
    crack_linkedin_hashed.append(final)

#res = []
#
#for i in range(0, 50000):
#    for j in range(len(crack_eharmony_hashed)):
#        if eharmony[i][:-1] == crack_eharmony_hashed[j]:
#            res.append(eharmony[i][:-1]+ "   "+pwd_lst[j][:-1])
#            break;
#
#print(res)




#res = []
#
#for i in range(0, 50000):
#    for j in range(len(crack_formspring_hashed)):
#        if formspring[i][:-1] == crack_formspring_hashed[j]:
#            res.append(formspring[i][:-1]+ "   "+salt_pwd_lst[j][:-1])
#            break;
#
#print(res)

res = []

for i in range(0, 10000):
    for j in range(len(crack_linkedin_hashed)):
        if linkedin[i][:-1] == crack_linkedin_hashed[j]:
            res.append(linkedin[i][:-1]+ "   "+pwd_lst[j][:-1])
            break;

print(res)





 

#lst = eharmony
#token = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','[',']','{','}','|','\',','?','.',':',';','<','>','1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
#simple_token= ['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

#
#flag = False
#while flag == False:
#    for pwd in itertools.permutations(simple_token, 10):
#        pwd = "".join(pwd)
#        if hashlib.md5(pwd.encode('utf-8')).hexdigest() == lst[0][:-1]:
#            flag = True
#            print(pwd)
#    flag = True
##            
#simple_simple_token = ['1','2','3','4','5','6','7','8','9','0']     
#            
#for i in range(40,100):
#    print(i)
#    flag = False
#    while flag == False:
#        for pwd in itertools.permutations(simple_simple_token, 10):
#            pwd = "".join(pwd)
#            pwd = hashlib.md5(pwd.encode('utf-8')).hexdigest()
#            if pwd == lst[i][:-1]:
#                flag = True
#                
#                print(pwd)
#        flag = True
            
        
#        
#simple_token= ['1','2','3','4','5','6','7','8','9','0','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'] 
#for i in range(0,101):
#    print(i)
#    flag = False
#    while flag == False:
#        for pwd_len in range(8,15):
#            for pwd in itertools.permutations(simple_token, pwd_len):
#                pwd = "".join(pwd)
#                pwd = hashlib.md5(pwd.encode('utf-8')).hexdigest()
#                if pwd == lst[i][:-1]
#                    flag = True
#                    print(pwd)
#        flag = True
#        
#        
