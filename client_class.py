import socket

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "213.185.10.224"
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connect_to_server():
    try:
        client.connect(ADDR)
    except Exception as e:
        print(f"[ERROR]: {e}")
        exit(1)
    print(f"[SUCCESSFULLY CONNECTED TO]: {ADDR}")


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    server_msg = client.recv(2048).decode(FORMAT)
    print(f"[SERVER]: {server_msg}")


class ClientSideChatroom:
    def __init__(self, client_alias):
        self.client_alias = client_alias
        self.last_received = None
        self.last_sent = None
        self.connected = False

    def connect_to_server(self):
        try:
            client.connect(ADDR)
        except Exception as e:
            print(f"[ERROR]: {e}")
            exit(1)
        self.connected = True
        print(f"[SUCCESSFULLY CONNECTED TO]: {ADDR}")

    def send_msg(self, msg):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b" " * (HEADER - len(send_length))
        client.send(send_length)
        sent_msg = client.send(message)
        self.last_sent = sent_msg
        server_msg = client.recv(2048).decode(FORMAT)
        self.last_received = server_msg
        print(f"[SERVER]: {server_msg}")


def main():
    alias = "Theo"
    chatroom = ClientSideChatroom(alias)
    chatroom.connect_to_server()
    while True:
        raw_msg = input(f"{alias}: ")
        aliased_msg = f"{alias} {raw_msg}"
        chatroom.send_msg(aliased_msg)
        if raw_msg == DISCONNECT_MESSAGE:
            chatroom.connected = False
            print("[SUCCESSFULLY DISCONNECTED]")
            break


if __name__ == "__main__":
    main()
