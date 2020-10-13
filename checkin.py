#!/usr/bin/env python3
import amino
import os
import getpass
os.system('clear')
print( '\033[1;31m           /$$                           /$$      ')
print( '\033[1;31m          | $$                          | $$      ')
print( '\033[1;31m  /$$$$$$$| $$$$$$$   /$$$$$$   /$$$$$$$| $$   /$$')
print( '\033[1;31m /$$_____/| $$__  $$ /$$__  $$ /$$_____/| $$  /$$/')
print( '\033[1;31m| $$      | $$  \ $$| $$$$$$$$| $$      | $$$$$$/ ')
print( '\033[1;31m| $$      | $$  | $$| $$_____/| $$      | $$_  $$ ')
print( '\033[1;31m|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$')
print( '\033[1;31m \_______/|__/  |__/ \_______/ \_______/|__/  \__/')
print( '\033[1;31m         /$$          ')
print( '\033[1;31m        |__/          ')
print( '\033[92m         /$$ /$$$$$$$ ')
print( '\033[92m /$$$$$$| $$| $$__  $$')
print( '\033[92m|______/| $$| $$  \ $$')
print( '\033[92m        | $$| $$  | $$')
print( '\033[92m        | $$| $$  | $$')
print( '\033[92m        |__/|__/  |__/      \033[1;36mscript By \033[1;92mkira_xc')
print('\n\033[0m')              
client=amino.Client()
ss=0
sz=25
nuum=0
tst=False
while tst==False:
    try:
        email=input("\033[1;93m# your email : \033[0m")
        password=getpass.getpass("\033[1;93m# your password : \033[0m")
        client.login(email=email,password=password)
        tst=True
    except:
        tst=False
        print("\033[1;93m# verify email or password\033[0m")
        exx=input("\033[1;93m# to be continue ?\033[1;92m y/n \033[0m: \033[0m")
        if exx=='n' or exx=='N' or exx=='no':
            os._exit(1)
listcom=client.sub_clients(start=ss,size=sz)
print("\033[1;93m# comminuty lengh : ",len(listcom.comId))
while len(listcom.comId)!=0:
    
    for comId in listcom.comId:
        sub_client=amino.SubClient(comId=comId,profile=client.profile)
        try:
          sub_client.check_in('0')
          info=sub_client.get_community_info(comId=comId)
          nuum=nuum+1
          print(nuum,"\033[1;93m)\033[1;92mcheck in : ok \ncomminuty name :",info.name,"\ncomnunity id : ",comId,"\033[0m")
        except:
            ttff=True
    ss=ss+25
    listcom=client.sub_clients(start=ss,size=sz)
print ("\033[1;92mall comminuty is done !\n\033[0m")
os._exit(1)
