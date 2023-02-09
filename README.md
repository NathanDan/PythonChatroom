# PythonChatroom
The Python Chatroom is a program that was created from an idea when playing around with some of the Python networking libraries, this version orginates from a previous script I had wrote for Grand Central but has been updated and created as a standalone program. It works by having a server script that uses the host machines IP address and then multiple client scripts that use the hosts IP address to connect to the server. The clients allow for custom usernames and colour schemes from a selection of 7 different colours.

The Python modules utilised within these scripts are the following:
  - colorama     - Allows for the colours of the usernames and server messages within te chatroom
  - socket       - Allows for the Python script to access and gather the IP & MAC Addresses along with the connectivity to the server through Ports
  - threading    - Allows for the Python script to run on multiple threads at once
  - sys          - Allows for the Python script to access the internal system (not used in current version)
  - datetime     - Allows for the Python script to access the real-time internal system clock allowing for the timestamps on the messages within the chatroom

These modules work in unison to produce the chatroom, and give it the features that make up the chatroom.

To run the chatroom the first script that needs to be run is the 'Server.py' as this will create the server for the chatroom which in turn gives you the IP address that is required for the clients if they want to join the chatroom. After the 'Server.py' script is running you can then run the 'Client,py' scripts, when running they will first ask for a username along with the colour you would like to be displayed. After these have been inputted the script will ask for the server's IP address to connect to the server, a successful connection will display the welcome message on the client which states "You are ONLINE Type @help to know all the commands" along with a message on the server side that states the user has connected. Multiple clients can connect to the server at one time, now the users have connected the users can begin to send messages

Within the chatroom there are 5 main commands:
  - @help         - Displays a message that explains each of the 4 commands
  - @online       - Displays to the user what other users are online
  - @all          - Sends the message to all users on the server
  - @ + uname     - Sends the message to a specific user on the server
  - @disconnect   - Disconnects the user from the server
  
These commands are vitial for the functionalities of the chatroom, each time a message is sent within the server the username and timestamp of the message are displayed next to the message, this allows for the users to see who has sent the message and at what time they sent it. When a user discconects from the server a message is displayed within the server acknowledging the user has disconnected, this is also the same when the server goes down a message is displayed to the client scripts that state "'Server is Down. You are now Disconnected. Press enter to exit..." this allows the user to know the server is down and need to reconnect or connect to another server. 
