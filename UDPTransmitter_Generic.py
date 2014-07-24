import socket
import threading
import time

# get IP and port for receiving UDP packets
RECEIVE_UDP_IP = raw_input("Enter your IP address: ")
RECEIVE_UDP_PORT = int(raw_input("Enter port to receive from: "))

# get IP and port for sending UDP packets
SEND_UDP_IP = raw_input("Enter IP to send to: ")
SEND_UDP_PORT = int(raw_input("Enter port to send to: "))

# configure socket for receiving UDP packets
receive_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receive_sock.bind((RECEIVE_UDP_IP, RECEIVE_UDP_PORT))

# configure socket for sending UDP packets
send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


''' begins receiving and sending threads '''
def main():
  recv_thread = threading.Thread(target=_receive)
  recv_thread.daemon = True
  recv_thread.start()

  send_thread = threading.Thread(target=_send)
  send_thread.daemon = True
  send_thread.start()

  while 1:
    time.sleep(1)


''' function to receive UDP packets in daemon thread '''
def _receive():
  while True:
    data, addr = receive_sock.recvfrom(1024) # buffer size is 1024 bytes
    print data


''' function to send UDP packets in daemon thread '''
def _send():
  while True:
    MESSAGE = raw_input()
    send_sock.sendto(MESSAGE, (SEND_UDP_IP, SEND_UDP_PORT))


if __name__ == "__main__":
    main()