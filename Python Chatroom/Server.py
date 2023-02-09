#Nathan Jones
#2023

from colorama import init                                #IMPORTING 'colorama' FEATURE THAT ALLOWS THE PROGRAM TO GIVE DIFFERENT COLOURS TO THE USERS 
from colorama import Fore, Back, Style                   #IMPORTING 'colorama' FEATURE THAT ALLOWS THE PROGRAM TO GIVE DIFFERENT COLOURS TO THE USERS 

import socket                                            #ALLOWS FOR THE PROGRAM TO GATHER IP AND MAC ADDRESSES AND CONNECTIVITY TO IP SERVERS THROUGH PORTS    
import threading                                         #ALLOWING THE PROGRAM TO RUN ON MULTIPLE THREADS
import datetime                                          #THIS ALLOWS FOR THE CURRENT DATE/TIME TO BE IMPORTED AND DISPLAYED FOR THE USER TO SEE

init()

date = datetime.date.today()                             #DEFINING A SHORTER NAME FOR THE FUNCTION THAT DISPALAYS THE CURRENT TIME
time = datetime.datetime.now()                           #DEFINING A SHORTER NAME FOR THE FUNCTION THAT DISPALAYS THE CURRENT DATE

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #ALLOWS GRAND CENTRAL TO GATHER THE CURRENT IP ADDRESS
serverRunning = True                                     #SETTING THE 'serverRunning' TO TRUE SO THE PROGRAM KNOWS THE SERVER HAS STARTED
ip = str(socket.gethostbyname(socket.gethostname()))     #ALLOWS THE SCRIPT TO GATHER THE CURRENT IP ADDRESS OF THE SYSTEM 
port = 1234                                              #DEFINING THE PORT TO BE USED TO SEND AND RECIEVE DATA/MESSAGES
 
clients = {}                                             #CREATING THE DICTIONARY THAT WILL STORE ALL OF THE USERS CHATROOM CLIENT THAT CONNECT TO THE SERVER 

s.bind((ip, port))                                       #ASSIGNING THE PORT AND IP ADDRESS OF THE SERVER
s.listen()                                               #LISTENING FOR THE OTHER CLIENTS TO CONNECT 

print(('Python Chatroom Server')+Style.BRIGHT+Fore.GREEN+str(' ONLINE')+Style.RESET_ALL+str('...')) #SHOWING THAT THE SERVER IS ON
#THE LINE BELOW DISPLAYS WHEN THE SERVER WAS STARTED BY GIVING THE DATE AND TIME, WITH 'ONLINE' AND THE TIME AND DATE BEING DISPLAYED IN GREEN
print(('Server')+Style.BRIGHT+Fore.GREEN+str(' ONLINE')+Style.RESET_ALL+str(' since: ')+Style.BRIGHT+Fore.GREEN+str(date.strftime("%d|%m|%Y "))+Style.RESET_ALL+str('@ ')+Style.BRIGHT+Fore.GREEN+str(time.strftime("%H:%M "))+ Style.RESET_ALL)
print('Ip Address of the Server:: '+ Style.BRIGHT + Fore.BLUE + str(ip) + Style.RESET_ALL)  #DISPLAYING THE SERVER'S IP ADDRESS TO CONNECT TO AND CHANGING THE IP ADDRESS COLOUR TO BLUE

def handleClient(client, uname):
    clientConnected = True               #CREATING A VARIABLE THAT WILL BE TRUE IF OTHER USERS HAVE CONNECTED 
    keys = clients.keys()                #CREATING A VARIABLE THAT WILL STORE THE USERS CHATROOM CLIENTS AS KEYS, SO THEY CAN BE IDENTIFED
    help = ('''

There Are 4 Commands In Messenger:

@online     = Shows All The People Currently Online
@disconnect = Ends Your session And Disconnects
@all        = Sends The Message To Everyone On The Server
@'Username' = Sends The Message To Particular User

''')                                    #CREATING THE HELP MENU THAT WILL BE DISPLAYED WITHIN THE CLIENTS OF THE USERS THAT HAVE CONNECTED AND WILL TELL THEM THE BASIC COMMANDS 

    while clientConnected:              #WHILST THE USERS CHATROOM CLIENTS ARE CONNECTED THEN THE FOLLOWING WILL TAKE PLACE 
        time = datetime.datetime.now()  #DEFINING A SHORTER NAME FOR THE DATE TIME MODULE SO IT CAN BE CALLED LATER ON 
        try:
            msg = client.recv(1024).decode('ascii') #DECODING THE MESSAGES THAT THE SERVER RECIEVES FROM THE CHATRROM CLIENTS  
            response = (('Number of People')+Style.BRIGHT +Fore.GREEN + str(' ONLINE') + Style.RESET_ALL+'\n') #DISPLAYING THE TITLE FOR THE NUMBER OF CHATROOM CLIENTS THAT HAVE CONNECTED
            found = False
            if '@online' in msg:   #IF A CHATROOM CLIENT MESSAGE CONTAINS '@online' THEN THE FOLLOWING WILL TAKE PLACE
                clientNo = 0       #DEFINING HOW MANY CHATROOM CLIENTS ARE ONLINE
                for name in keys:  #IF THERE ARE CHATROOM CLIENTS THAT HAVE CONNECTED AND ARE STORE IN THE KEYS THE FOLLOWING WILL TAKE PLACE
                    clientNo += 1  #ADDING TO THE NUMBER OF USERS CONNECTED TO KEEP A COUNT OF PEOPLE 
                    response = response + str(clientNo) +'::' + name+'\n' #CREATING A RESPONSE TO DISPLAY HOW MANY USERS ARE CONNECTED FOLLOWED THE NAMES OF THE USERS 
                client.send(response.encode('ascii'))                     #SENDING THE RESPONSE TO THE USERS CLIENT AND ENCODING TEH MESSAGE BEFORE IT IS SENT 
            elif '@help' in msg:                     #IF A CHATROOM CLIENT MESSAGE CONTAINS '@help' THEN THE FOLLOWING WILL TAKE PLACE 
                client.send(help.encode('ascii'))    #SENDS THE USERS CLIENT THE HELP MESSAGE THAT DISPLAYS ALL OF THE COMMANDS FOR THE CHATROOM  
            elif '@all' in msg:                      #IF A CHATROOM CLIENT MESSAGE CONTAINS '@all' THEN THE FOLLOWING WILL TAKE PLACE
                msg = msg.replace('@all','')         #THE MESSAGE THAT HAS BEEN SENT WILL REPLACE THE '@all' WITH NOTHING  
                for k,v in clients.items():         
                    v.send(msg.encode('ascii'))      #SENDING THE MESSAGE TO ALL USERS IN THE CHATROOM AT THAT TIME AND IN THE PROCESS WILL ENCODE THE MESSAGE 
            elif '@disconnect' in msg:               #IF A CHATROOM CLIENT MESSAGE CONTAINS '@disconnect' THEN THE FOLLOWING WILL TAKE PLACE  
                response = Style.BRIGHT +Fore.RED + str('ENDING') + Style.RESET_ALL + ' Session and exiting...' #CREATING A RESPONSE TO DISPLAY THATV THEIR SESSION IS ENDING/DISCONNECTING 
                client.send(response.encode('ascii'))#SENDING THAT RESPONSE TO THE SPECIFIC USERS CLIENT AND ENCODING IT BEFORE SENDING 
                clients.pop(uname)                   #PHYSICALLY REMOVING THE USERS CLIENT FROM THE SERVER
                response1 = uname + Style.BRIGHT +Fore.RED + str('LOGGED OUT') + Style.RESET_ALL
                client.send(response.encode('ascii'))#SENDING THAT RESPONSE TO THE SPECIFIC USERS CLIENT AND ENCODING IT BEFORE SENDING
                print(uname + ' has logged out')     #DISPLAYING IN THE SERVER WINDOW THAT THE USER HAS LOGGED OUT 
                clientConnected = False              #CHANGING THE VARIABLE THAT STATES IF A USER IS STILL CONNECTED 
            else:
                for uname in keys:       
                    if('@'+uname) in msg:   #IF A MESSAGE WITHIN THE CHATROOM CONTAINS A NAME OF ONE OF THE USERS IT WILL SEND IT TO THAT USER
                        msg = msg.replace('@'+uname, ''+str(time.strftime("%H:%M "))) #ADDING THE TIME TO THE MESSAGE AND ADDING THE USER THE MESSAGE IS GOING TO 
                        clients.get(uname).send(msg.encode('ascii'))                  #ENCODING THE MESSAGE AND GATHER THE INFORMATION WHERE TO SEND THE MESSAGE 
                        found = True                                                 #IF THE USER THAT THE MESSAGE IS BEING SENT TO HAS BEEN FOUND THEN THE VARIABLE IS SET TO 'True'
                if(not found):
                    client.send('Trying to send message to invalid person.'.encode('ascii')) #IF THE USER CANNOT BE FOUND THEN THIS MESSAGE WILL BE SENT TO THE USER WHO SENT THE MESSAGE
        except:
            clients.pop(uname)                 #SEEING IF THE USER TEHY ARE TRYING TO SEND THE MESSAGE TO HAS LOGGED OUT 
            print(uname + ' has Disconnected') #DISPLAYING A MESSAGE SAYING THAT THE USER THEY TRIED TO SEND THE MESSAGE TO HAS LOGGED OUT 
            clientConnected = False            #CHANGING THE VARIABLE TO 'False' THAT STATES WHETHER THE USER'S CLIENT HAS CONNECTED

while serverRunning:                               #THIS LOOP ONLY RUNS WHILST THE 'serverRunning' VARIABLE IS TRUE
    client, address = s.accept()                   #ACCEPTING THE REQUESTS FROM THE USER'S CLIENTS THAT ARE TRYING TO CONNECT WITH THE SERVER
    uname = client.recv(1024).decode('ascii')      #RECIEVING THE USER'S CHATROOM CLIENTS USERNAME SO IT CAN BE DISPLAYED 
    print('%s connected to the server'%str(uname)) #DISPLAYING WITHIN THE SERVER WINDOW THAT A NEW USER HAS CONNECED ALONG WITH THEIR USERNAME 
    client.send('You are ONLINE Type @help to know all the commands'.encode('ascii')) #SENING THE WELCOME MESSAGE TO THE USER'S CLIENT
    
    if(client not in clients):    #IF THE CLIENTS USERNAME IS NOT IN THE SYSTEM THE FOLLOWING WILLN TAKE PLACE
        clients[uname] = client   #ADDING THE CLIENTS CHATROOM USERNAME TO THE DICTIONARY 
        threading.Thread(target = handleClient, args = (client, uname, )).start() #STARTING ANOTHER THREAD FOR THAT USER SO THEY CAN HAVE ACCESS TO THE SERVER AND SEND MESSAGES  

#Nathan Jones -2023
