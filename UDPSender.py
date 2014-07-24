import socket
 
UDP_IP = "localhost"
UDP_PORT = 5005

while True:
  MESSAGE = raw_input(">")

  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))