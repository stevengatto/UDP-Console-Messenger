import socket
import threading

# get IP and port for receiving UDP packets
RECEIVE_UDP_IP = raw_input("Enter your IP address")
RECEIVE_UDP_PORT = raw_input("Enter port to receive from")

# get IP and port for sending UDP packets
SEND_UDP_IP = raw_input("Enter IP to send to")
SEND_UDP_PORT = raw_input("Enter port to send to")

# configure socket for receiving UDP packets
receive_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

# configure socket for sending UDP packets
send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


''' begins receiving and sending threads '''
def main:
  self.recv_thread = threading.Thread(target=self._receive)
  self.recv_thread.daemon = True
  self.recv_thread.start()

  self.send_thread = threading.Thread(target=self._send)
  self.send_thread.daemon = True
  self.send_thread.start()


''' function to receive UDP packets in daemon thread '''
def _receive(self):
  while True:
    data, addr = receive_sock.recvfrom(1024) # buffer size is 1024 bytes
    print data


''' function to send UDP packets in daemon thread '''
def _send(self):
  MESSAGE = raw_input(">")
  sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))


if __name__ == "__main__":
    main()