#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# email registration,login and forgetpassword
def choices():
    print("Please choose what you would like to do.")
    choice = int(input("For register Type 1 : \nFor login in Type 2 :\nFor forget password type3 :\n"))
    if choice == 1:
        return register()
    elif choice == 2:
        return login()
    elif choice ==3:
        return forgetpassword()
    else:
        raise TypeError
        
import re
def register():
    f=open('datastored.txt','r')
    symbols=['!','@','#','$','%','^','&','*','(',')']
    email=input('email id: ')
    password=input('password: ')     
    valid=True
    if not (re.match('^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$',email)!= None):
        print('invalid email id,please try again')
        register()
        
      
    else:
        if len(password)<5 and len(password)>16:
            valid= False
            register()
        if not any (char.islower()for char in password):
            valid= False
            register()
        if not any (char.isupper()for char in password):
            valid= False
            register()
        if not any (char.isdigit()for char in password):
            valid= False
            register()
        if not any (char in symbols for char in password):
            valid= False
            register()
         
        if valid:
                f=open('datastored.txt','a')
                f.write(email+','+password+'\n')
                f.close()
                print('registeration is done')   
                
def login():
    e=[]
    p=[]
    f=open('datastored.txt','r')
    for i in f:
        a,b = i.split(',')
        b = b.strip()
        e.append(a)
        p.append(b)
    data = dict(zip(e,p))
        
    print('login')
    email=input('email id=')
    password=input('password=')
    
    if email in data.keys() and password in data.values():
        print('login successful')
    else:
        print('incorrect password or email')
        login()
    
def forgetpassword():
    e=[]
    p=[]
    f=open('datastored.txt','r')
    for i in f:
        a,b= i.split(',')
        b=b.strip()
        e.append(a)
        p.append(b)
    data=dict(zip(e,p))
    
    print('login')
    e=input('email id=')
    
    if e in data.keys():
        p=data[e]
        print('password = '+ p)
        
    else:
        print('invalid email id')
        login()
    
choices()    

