import socket

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "YOUR IPV4 ADDRESS"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    server_msg = client.recv(2048).decode(FORMAT)
    print(f"[SERVER]: {server_msg}")


send("hello world!")
input()
send("deez nuts")
input()
send(DISCONNECT_MESSAGE)
