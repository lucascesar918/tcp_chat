# tcp_irc
TCP/IP chat room client and server built using Python 3.10.5
 
This is a tool that manages connections and messages between devices by using TCP/IP protocol to communicate.
 
Feel free to complement the code and fork it.
 
## How to use?
 
### Starting server
Firstly check the host and port variables at the beginning of the file (you're welcome to add annoying inputs to prompt values for those variables). Start tcp_server.py file which is responsible for, as the name suggests, initializing the TCP server. The server will notify each connection and if something is written and sent in terminal, it will show up in chat with the nickname 'sys' (with a cool red color).
 
### Starting client
Again, check host and port variables. Each user will have to open the client located in tcp_client.py and enter their nicknames. After this, all connected users will be notified when someone is connected. Users can simply write and send messages in client (don't try typing while another user sends a message lol).
 
## Known bugs
 
* Multiple users with the same nickname
* User can't disconnect by itself
* Typing while another user sends messages interrupts the written message (message doesn't change, it is just inconvenient)
