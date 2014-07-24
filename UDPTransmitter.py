import socket
import threading
import time
import base64

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
    data = _decode("vnad45hwpgn", data)
    print data


''' function to send UDP packets in daemon thread '''
def _send():
  while True:
    message = raw_input()
    message = _encode("vnad45hwpgn", message)
    send_sock.sendto(message, (SEND_UDP_IP, SEND_UDP_PORT))


''' function to encode string prior to sending '''
def _encode(key, string):
    encoded_chars = []
    for i in xrange(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return base64.urlsafe_b64encode(encoded_string)
 

''' function to decode string after receiving '''
def _decode(key, string):
    decoded_chars = []
    string = base64.urlsafe_b64decode(string)
    for i in xrange(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(abs(ord(string[i]) - ord(key_c) % 256))
        decoded_chars.append(encoded_c)
    decoded_string = "".join(decoded_chars)
    return decoded_string


if __name__ == "__main__":
    main()