import socket

target_host = "127.0.0.1"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("AABBCC".encode('utf-8'), (target_host, target_port))
data, addr = client.recvfrom(4096)

print(data)

""" 
ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host                
"""