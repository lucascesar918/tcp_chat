import socket
import threading


# Color class
class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


# Connection information
host = "127.0.0.1"  # localhost
port = 8001

# Starting server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists for clients and nicknames
clients = []
nicknames = []


# Broadcasting messages to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)


# Handling messages
def handle(client):
    while True:
        try:
            # Broadcasting received message
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing and closing clients
            nickname = nicknames[clients.index(client)]
            nicknames.remove(nickname)
            client.close()
            broadcast(f"{Colors.RESET}{Colors.YELLOW + nickname} has been disconnected.".encode())
            print(f"{Colors.RESET}{Colors.YELLOW}[{client}]@{nickname} has disconnected.")
            break


def write():
    while True:
        message = input(f"{Colors.RESET}")
        broadcast(f"{Colors.RED}sys{Colors.RESET}: {message}".encode())


# Receiving client connections and handling them
def receive():
    while True:
        # Accept connection
        client, address = server.accept()

        # Request and store nickname
        client.send("nick:".encode())
        nickname = client.recv(1024).decode()
        clients.append(client)
        nicknames.append(nickname)

        # Print and broadcast connection
        client.send(f"{Colors.RESET}{Colors.BLUE}Connected!{Colors.RESET}\n".encode())
        broadcast(f"{Colors.RESET}{Colors.BLUE}{nickname} joined.{Colors.RESET}".encode())
        print(f"{Colors.RESET}{Colors.BLUE}{str(address)}{Colors.RESET}@{Colors.CYAN}{nickname}{Colors.RESET} has been connected.")

        # Start handling and receiving for client
        handle_thread = threading.Thread(target=handle, args=(client,))
        write_thread = threading.Thread(target=write)
        handle_thread.start()
        write_thread.start()


print(f"{Colors.RESET}{Colors.GREEN}Server is online...")
receive()
