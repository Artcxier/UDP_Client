import socket

target_host = "127.0.0.1"
target_port = 9997

#creation of a nest object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#sending data
client.sendto("AAABBBCCC", (target_host, target_port))

#reciving data
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()