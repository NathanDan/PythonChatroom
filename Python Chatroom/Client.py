#Nathan Jones - 19696498
#Advanced Programming Additional Feature
#2023

from colorama import init                                     #IMPORTING 'colorama' FEATURE THAT ALLOWS THE PROGRAM TO GIVE DIFFERENT COLOURS TO THE USERS     
from colorama import Fore, Back, Style                        #IMPORTING 'colorama' FEATURE THAT ALLOWS THE PROGRAM TO GIVE DIFFERENT COLOURS TO THE USERS

import socket                                                 #ALLOWS FOR THE PROGRAM TO GATHER IP AND MAC ADDRESSES AND CONNECTIVITY TO IP SERVERS THROUGH PORTS 
import threading                                              #ALLOWING THE PROGRAM TO RUN ON MULTIPLE THREADS 
import sys                                                    #ALLOWS ACCESS TO THE SYSTEM FROM WITHIN PYTHON
import datetime                                               #THIS ALLOWS FOR THE CURRENT TIME TO BE IMPORTED AND DISPLAYED FOR THE USER TO SEE

init()                                                        
Colour = '6'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         #ALLOWS GRAND CENTRAL TO GATHER THE CURRENT IP ADDRESS
port = 1234                                                   #DEFINING THE PORT TO BE USED TO SEND AND RECIEVE DATA/MESSAGES

print('Welcome To The CMP9133 Advanced Programming Curling Messenger Server'+'\n')
Uname = input('Enter Online Name:: ')
Colour = input('''
 Colour Selection
1. Red      5. Cyan
2. Blue     6. White
3. Green    7. Magenta
4. Yellow   

Option: 
''')
if Colour == '1':
    uname = Style.BRIGHT +Fore.RED + Uname + Style.RESET_ALL     #CREATING THE USERNAME FOR THIS ACCOUNT AND THEN ASSIGNING A COLOUR TO THE USERNAME 
elif Colour == '2':
    uname = Style.BRIGHT +Fore.BLUE + Uname + Style.RESET_ALL    #CREATING THE USERNAME FOR THIS ACCOUNT AND THEN ASSIGNING A COLOUR TO THE USERNAME 
elif Colour == '3':
    uname = Style.BRIGHT +Fore.GREEN + Uname + Style.RESET_ALL   #CREATING THE USERNAME FOR THIS ACCOUNT AND THEN ASSIGNING A COLOUR TO THE USERNAME 
elif Colour == '4':
    uname = Style.BRIGHT +Fore.YELLOW + Uname + Style.RESET_ALL  #CREATING THE USERNAME FOR THIS ACCOUNT AND THEN ASSIGNING A COLOUR TO THE USERNAME 
elif Colour == '5':
    uname = Style.BRIGHT +Fore.CYAN + Uname + Style.RESET_ALL    #CREATING THE USERNAME FOR THIS ACCOUNT AND THEN ASSIGNING A COLOUR TO THE USERNAME 
elif Colour == '6':
    uname = Style.BRIGHT +Fore.WHITE + Uname + Style.RESET_ALL   #CREATING THE USERNAME FOR THIS ACCOUNT AND THEN ASSIGNING A COLOUR TO THE USERNAME 
elif Colour == '7':
    uname = Style.BRIGHT +Fore.MAGENTA + Uname + Style.RESET_ALL #CREATING THE USERNAME FOR THIS ACCOUNT AND THEN ASSIGNING A COLOUR TO THE USERNAME 
else:
    uname = Style.BRIGHT +Fore.WHITE + Uname + Style.RESET_ALL   #CREATING THE USERNAME FOR THIS ACCOUNT AND THEN ASSIGNING A COLOUR TO THE USERNAME
    

ip = input('Enter the IP Address:: ')                         #USER ENTERS THE IP OF THE GRAND CENTRAL CHATROOM SERVER THAT WILL ALWAYS STAY THE SAME UNLESS CONNECTING TO ANOTHER SERVER

s.connect((ip, port))                                         #CONNECTING TO THE IP ADDRESS THAT WAS ENTERED ABOVE THROUGH THE PORT THAT WAS DEFINED 
s.send(uname.encode('ascii'))                                 #AFTER IT HAS CONNECTED TO THE SERVER THE USERNAME OF THIS CLIENT WILL BE SENT TO THE SERVER 

clientRunning = True                                          #SETTING THE 'clientRunning' TO TRUE SO THE PROGRAM KNOWS IT HAS ATTEMPTED TO MAKE A HANDSHAKE WITH THE SERVER 

def receiveMsg(sock):
    Colour
    serverDown = False                                        #SETTING THE 'serverDown' VARAIBLE TO BE FALSE SO THAT THE PROGRAM KNOWS IT HAS RECIEVED A RESPONSE FROM THE SERVER 
    while clientRunning and (not serverDown):                 #THE WHILE LOOP WILL ONLY BE IN AFFECT WHILST THE 'clientRunning' VARIABLE IS SET TO TRUE
        try:
            msg = sock.recv(1024).decode('ascii')             #RECIVING THE WELCOME MESSAGE FROM THE SERVER AND DECODING IT FROM ASCII
            print(msg)                                         
        except:
            print('Server is ' + Style.BRIGHT +Fore.RED + str('Down') + Style.RESET_ALL + '. You are now Disconnected. Press enter to exit...') #NO MESSAGE FROM THE SERVER THEN THE PROGRAM WILL DISPLAY A MESSAGE SAYING SERVER DOWN
            serverDown = True                                                         #CHANGING THE 'serverDown' VARIABLE TO BE TRUE 

threading.Thread(target = receiveMsg, args = (s,)).start()                            #TELLING THE PROGRAM WHAT THREADS TO RUN AT THE SAME TIME 
while clientRunning:         
 
    time = datetime.datetime.now()                                                    #DEFINING A SHORTER NAME FOR THE FUNCTION THAT DISPALAYS THE CURRENT TIME 
    MSG = input()                                                                     #DEFINING WHAT THE USER INPUTS AS THE MESSAGE THAT WILL BE SENT
    if Colour == '1':
         msg = str(time.strftime("%H:%M ")) + '<' + Style.BRIGHT +Fore.RED + str(uname) + Style.RESET_ALL + '> ' + MSG #ADDING THE MESSAGE TO THE TIME STAMP + USERNAME SO USERS KNOW WHO SENT IT 
    elif Colour == '2':
         msg = str(time.strftime("%H:%M ")) + '<' + Style.BRIGHT +Fore.RED + str(uname) + Style.RESET_ALL + '> ' + MSG #ADDING THE MESSAGE TO THE TIME STAMP + USERNAME SO USERS KNOW WHO SENT IT
    elif Colour == '3':
         msg = str(time.strftime("%H:%M ")) + '<' + Style.BRIGHT +Fore.RED + str(uname) + Style.RESET_ALL + '> ' + MSG #ADDING THE MESSAGE TO THE TIME STAMP + USERNAME SO USERS KNOW WHO SENT IT 
    elif Colour == '4':
         msg = str(time.strftime("%H:%M ")) + '<' + Style.BRIGHT +Fore.RED + str(uname) + Style.RESET_ALL + '> ' + MSG #ADDING THE MESSAGE TO THE TIME STAMP + USERNAME SO USERS KNOW WHO SENT IT 
    elif Colour == '5':
         msg = str(time.strftime("%H:%M ")) + '<' + Style.BRIGHT +Fore.RED + str(uname) + Style.RESET_ALL + '> ' + MSG #ADDING THE MESSAGE TO THE TIME STAMP + USERNAME SO USERS KNOW WHO SENT IT 
    elif Colour == '7':
         msg = str(time.strftime("%H:%M ")) + '<' + Style.BRIGHT +Fore.RED + str(uname) + Style.RESET_ALL + '> ' + MSG #ADDING THE MESSAGE TO THE TIME STAMP + USERNAME SO USERS KNOW WHO SENT IT
    elif Colour == '8':
         msg = str(time.strftime("%H:%M ")) + '<' + Style.BRIGHT +Fore.RED + str(uname) + Style.RESET_ALL + '> ' + MSG #ADDING THE MESSAGE TO THE TIME STAMP + USERNAME SO USERS KNOW WHO SENT IT 
    else:
         msg = str(time.strftime("%H:%M ")) + '<' + Style.BRIGHT +Fore.RED + str(uname) + Style.RESET_ALL + '> ' + MSG #ADDING THE MESSAGE TO THE TIME STAMP + USERNAME SO USERS KNOW WHO SENT IT
    

    if '@quit' in msg:                     #IF THE MESSAGE CONTAINS '@quit' THEN THE FOLLOWING WOULD TAKE PLACE
        clientRunning = False              #CHANGING THE 'clientRunning' VARIABLE TO BE FALSE
        s.send('@quit'.encode('ascii'))    #SENDING THE '@quit' MESSAGE TO THE SEVER THAT WILL DISCONNECT THE USER FROM THE SERVER
    else:
        s.send(msg.encode('ascii'))        #IF IT DOES NOT CONTAIN '@quit' IT WILL SEND TEH MESSAGE TO THE SERVER THAT WILL THEN DISTRIBUTE THE MESSAGE 

#Nathan Jones - 19696498 - 2023