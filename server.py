import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CLIENT CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            # FIX SO CLIENT ALIAS IS SHOWING
            raw_msg = conn.recv(msg_length).decode(FORMAT)
            client_alias = raw_msg.split(" ")[0]
            alias_len = len(client_alias) + 1
            msg = raw_msg[alias_len:]
            if msg == DISCONNECT_MESSAGE:
                print(f"[{client_alias}] DISCONNECTED")
                break
            print(f"[{client_alias}]: {msg}")
            server_answer = input("[SERVER]: ")
            conn.send(server_answer.encode(FORMAT))
    conn.close()
    print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 2}")


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on local server: |{SERVER}| and local port: |{PORT}|")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    pass


print("[SERVING IS STARTING]...")

start()
