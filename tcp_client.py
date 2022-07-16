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


# Defining initial variables
host = "127.0.0.1"  # localhost:1024
port = 8001
nickname = input(f"{Colors.RESET}{Colors.UNDERLINE}What will be your nickname? >> ")

# Connecting to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == "nick:":
                client.send(nickname.encode())
            else:
                print(message)

        except:
            print(f"{Colors.RESET}{Colors.RED}An error occurred!")
            client.close()
            break


def write():
    while True:
        message = input(f"{Colors.RESET}")
        client.send(f"{Colors.CYAN}{nickname}{Colors.RESET}: {message}".encode())


receive_thread = threading.Thread(target=receive)
write_thread = threading.Thread(target=write)

receive_thread.start()
write_thread.start()
