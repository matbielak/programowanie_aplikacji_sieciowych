### Zadanie 1
import ntplib
from datetime import datetime

server = "ntp.task.gda.pl"
try:
    client = ntplib.NTPClient()
    response = client.request(server,version=3)
    current_time = datetime.fromtimestamp(response.tx_time)
    print(current_time)
except Exception as e:
    print(e)

### Zadanie 2
# Klient:
import socket

add = "127.0.0.1" # "212.182.24.27"
port = 2900
msg = "Hello"

try:
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((add,port))
    client_socket.sendall(msg.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Otrzymano wiadomosc od serwera: {response}")
except Exception as e:
    print(e)
finally:
    client_socket.close()
# Server:
import socket, select
from time import gmtime, strftime

HOST = '127.0.0.1'
PORT = 2900

connected_clients_sockets = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

connected_clients_sockets.append(server_socket)

print("[%s] TCP ECHO Server is waiting for incoming connections on port %s ... " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), PORT))

while True:

    read_sockets, write_sockets, error_sockets = select.select(connected_clients_sockets, [], [])

    for sock in read_sockets:

        if sock == server_socket:

            sockfd, client_address = server_socket.accept()
            connected_clients_sockets.append(sockfd)

            print("[%s] Client %s connected ... " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), client_address))

        else:
            try:
                data = sock.recv(4096)
                if data:
                    sock.send(data)
                    print ("[%s] Sending back to client %s data: [\'%s\']... " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), client_address, data))

            except:
                print("[%s] Client (%s) is offline" % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), client_address))
                sock.close()
                connected_clients_sockets.remove(sock)
                continue
server_socket.close()

### Zadanie 3
import socket

add = "127.0.0.1" # "212.182.24.27"
port = 2900
msg = "Hello"

try:
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((add,port))
    while True:
        user_input = input("Wiadomosc do serwera: (exit = wyjscie)")
        if user_input == 'exit':
            break
        client_socket.sendall(user_input.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Otrzymano wiadomosc od serwera: {response}")
except Exception as e:
    print(e)
finally:
    client_socket.close()

### Zadanie 4
# Klient:

import socket

add = "127.0.0.1" # "212.182.24.27"
port = 2901
msg = "Hello"

try:
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    client_socket.sendto(msg.encode('utf-8'),(add,port))
    response, server = client_socket.recvfrom(1024)
    print(f"Otrzymano wiadomosc od serwera: {response.decode('utf-8')}")
except Exception as e:
    print(e)
finally:
    client_socket.close()

# Server:

import socket, select, sys
from time import gmtime, strftime

HOST = '127.0.0.1'
PORT = 2901

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print("[%s] UDP ECHO Server is waiting for incoming connections ... " % strftime("%Y-%m-%d %H:%M:%S", gmtime()))

try:
    while True:

        data, address = sock.recvfrom(4096)

        print('[%s] Received %s bytes from client %s. Data: %s' % (
        strftime("%Y-%m-%d %H:%M:%S", gmtime()), len(data), address, data))

        if data:
            sent = sock.sendto(data, address)
            print('[%s] Sent %s bytes bytes back to client %s.' % (
            strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address))
finally:
    sock.close()

###Zadanie 5
import socket

add = "127.0.0.1" # "212.182.24.27"
port = 2901

try:
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True:
        user_input = input("Wiadomosc do serwera: (exit = wyjscie)")
        if user_input == 'exit':
            break
        client_socket.sendto(user_input.encode('utf-8'),(add,port))
        response, server = client_socket.recvfrom(1024)
        print(f"Otrzymano wiadomosc od serwera: {response.decode('utf-8')}")
except Exception as e:
    print(e)
finally:
    client_socket.close()

### Zadanie 6
# Klient:

import socket

def main():
    server_address = ('127.0.0.1', 2902)

   
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        while True:
            try:
                number1 = input("Podaj pierwszą liczbę (lub 'exit' aby zakończyć): ")
                if number1.lower() == 'exit':
                    print("Zamykanie klienta.")
                    break
                
                message=f"{number1}"
                client_socket.sendto(message.encode('utf-8'), server_address)

                operator = input("Podaj operator (+, -, *, /): ")
                if operator not in ['+', '-', '*', '/']:
                    print("Nieprawidłowy operator. Spróbuj ponownie.")
                    continue

                message=f"{operator}"
                client_socket.sendto(message.encode('utf-8'), server_address)

                number2 = input("Podaj drugą liczbę: ")

                message = f"{number2}"
                client_socket.sendto(message.encode('utf-8'), server_address)

                response, _ = client_socket.recvfrom(1024)
                print("Odpowiedź serwera:", response.decode('utf-8'))
            except Exception as e:
                print("Wystąpił błąd:", e)

if __name__ == "__main__":
    main()

# Serwer:

import socket
import sys
from time import gmtime, strftime

HOST = '127.0.0.1'
PORT = 2902

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.bind((HOST, PORT))
except socket.error as msg:
    print("Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]")
    sys.exit()

print ("[%s] UDP Calc Server is waiting for incoming connections ... " % strftime("%Y-%m-%d %H:%M:%S", gmtime()))

try:
    while True:

        data1, address = sock.recvfrom(4096)
        op, address = sock.recvfrom(4096)
        data2, address = sock.recvfrom(4096)

        if data1 and data2 and op:

            op = op.decode('utf-8')
            

            print("[%s] Got from client %s ... : %s %s %s" % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), str(address), data1, op, data2))

            try :

                if op == '+':
                    result = float(data1) + float(data2)
                    sent = sock.sendto(str(result).encode('utf-8'), address)
                elif op == '-':
                    result = float(data1) - float(data2)
                    sent = sock.sendto(str(result).encode('utf-8'), address)
                elif op == '*':
                    result = float(data1) * float(data2)
                    sent = sock.sendto(str(result).encode('utf-8'), address)
                elif op == '/':
                    result = float(data1) / float(data2)
                    sent = sock.sendto(str(result).encode('utf-8'), address)
                else:
                    result = "Bad operator. I support only +, -, *, / math operators"
                    sent = sock.sendto(str(result).encode('utf-8'), address)

            except ValueError :
                result = "%s"
                sent = sock.sendto(str(result).encode('utf-8'), address)

            except:
                result = "Error"
                sent = sock.sendto(str(result).encode('utf-8'), address)
finally:

    sock.close()

### Zadanie 7
import socket

HOST = input("host: ")  # np. 216.58.215.110
PORT = int(input("port number: "))  # np. 80

server_address = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect(server_address)
    print(f"Successfully connected to {HOST} on port {PORT}")

    sock.settimeout(5)  
    response = sock.recv(1024).decode('utf-8', errors='replace')  
    print(f"Server response:\n{response}")

    if "HTTP" in response:
        print("Detected service: HTTP (Web Server)")
    elif "SSH" in response:
        print("Detected service: SSH (Secure Shell)")
    elif "SMTP" in response:
        print("Detected service: SMTP (Mail Server)")
    else:
        print("Service not recognized. It might be a custom service.")

except ConnectionRefusedError:
    print(f"Connection to {HOST} on port {PORT} was refused.")
except socket.timeout:
    print("Connection timed out. No response received.")
except OSError as e:
    print(f"An error occurred: {e}")
finally:
    sock.close()

### Zadanie 8
import socket

HOST = input("host: ")  # np. 216.58.215.110
PORT = int(input("port number: "))  # np. 80

server_address = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect(server_address)
    print(f"Successfully connected to {HOST} on port {PORT}")

    sock.settimeout(5)  
    response = sock.recv(1024).decode('utf-8', errors='replace')  
    print(f"Server response:\n{response}")

    if "HTTP" in response:
        print("Detected service: HTTP (Web Server)")
    elif "SSH" in response:
        print("Detected service: SSH (Secure Shell)")
    elif "SMTP" in response:
        print("Detected service: SMTP (Mail Server)")
    else:
        print("Service not recognized. It might be a custom service.")

except ConnectionRefusedError:
    print(f"Connection to {HOST} on port {PORT} was refused.")
except socket.timeout:
    print("Connection timed out. No response received.")
except OSError as e:
    print(f"An error occurred: {e}")
finally:
    sock.close()


### Zadanie 9
# Klient: 
import socket

def main():
    server_address = ('127.0.0.1', 2906)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        try:
            ip_address = input("Podaj adres IP: ")

            print(f"Wysyłanie adresu IP {ip_address} do serwera {server_address}")
            client_socket.sendto(ip_address.encode(), server_address)


            response, _ = client_socket.recvfrom(1024) 
            print(f"Otrzymana nazwa hosta dla adresu {ip_address}: {response.decode()}")
        
        except Exception as e:
            print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    main()
# Serwer:

import socket, select, sys
from time import gmtime, strftime

HOST = '127.0.0.1'
PORT = 2906

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print ("[%s] UDP ECHO Server is waiting for incoming connections on port %s ... " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), PORT))

try:
    while True:

        data, address = sock.recvfrom(4096)
        print('[%s] Received %s bytes from client %s. Data: %s' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), len(data), address, data))

        if data:

            try :

                hostname = socket.gethostbyaddr(str(data.decode('utf-8')))
                print(f"HOSTNAME: {hostname[0]}")
                sent = sock.sendto(hostname[0].encode('utf-8'), address)
                print ('[%s] Sent %s bytes bytes back to client %s.' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address))

            except socket.herror:
                sent = sock.sendto("Sorry, an error occurred in gethostbyaddr", address)
                print ('[%s] Sent %s bytes bytes back to client %s.' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address))
finally:
    sock.close()

### Zadanie 10
# Klient:
import socket

def main():
    server_address = ('127.0.0.1', 2907)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        try:

            hostname = input("Podaj nazwę hosta: ")

            print(f"Wysyłanie nazwy hosta {hostname} do serwera {server_address}")
            client_socket.sendto(hostname.encode(), server_address)

            response, _ = client_socket.recvfrom(1024)
            print(f"Otrzymany adres IP dla hosta {hostname}: {response.decode()}")
        
        except Exception as e:
            print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    main()

# Serwer:
# !/usr/bin/env python

import socket, select, sys
from time import gmtime, strftime

HOST = '127.0.0.1'
PORT = 2907

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print ("[%s] UDP ECHO Server is waiting for incoming connections on port %s ... " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), PORT))

try:
    while True:

        data, address = sock.recvfrom(4096)
        print ('[%s] Received %s bytes from client %s. Data: %s' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), len(data), address, data))

        if data:

            try:

                hostname = socket.gethostbyname(str(data.decode('utf-8')))
                #sent = sock.sendto(str(hostname), address)
                sent = sock.sendto(hostname.encode('utf-8'), address)
                print ('[%s] Sent %s bytes bytes back to client %s.' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address))

            except socket.gaierror:
                sent = sock.sendto("Sorry, an error occurred in gethostbyaddr".encode('utf-8'), address)
                print ('[%s] Sent %s bytes bytes back to client %s.' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address))
finally:
    sock.close()


### Zadanie 11
# Klient:

import socket

def prepare_message(message, length=20):
    if len(message) < length:
        return message.ljust(length)
    elif len(message) > length:
        return message[:length]
    return message

def main():

    server_address = ("127.0.0.1", 2908)

    msg = input("Podaj wiadomość do wysłania (max 20 znaków): ")
    prepared_msg = prepare_message(msg)

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            print(f"Łączenie z serwerem {server_address}...")
            client_socket.connect(server_address)
            
            print(f"Wysyłanie wiadomości: '{prepared_msg}'")
            client_socket.sendall(prepared_msg.encode('utf-8'))

            response = client_socket.recv(1024).decode('utf-8')
            print(f"Otrzymano wiadomość od serwera: '{response}'")
    
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    main()


# Serwer:


import socket
import sys
from time import gmtime, strftime

HOST = '127.0.0.1'
PORT = 2908
MAX_PACKET_LENGTH = 20

def recvall(sock, msgLen):
    msg = ""
    bytesRcvd = 0

    while bytesRcvd < msgLen:

        chunk = sock.recv(msgLen - bytesRcvd)

        if not chunk:
            break

        bytesRcvd += len(chunk)
        msg += str(chunk)

    return msg

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

s.listen(1000)

print("[%s] TCP ECHO (fixed-length messages) Server is waiting for incoming connections ... " % strftime("%Y-%m-%d %H:%M:%S", gmtime()))

while True:

    connection, client_address = s.accept()

    try:
        print("[%s] Client %s connected ... " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), client_address))

        while True:
            try :
                data = recvall(connection, MAX_PACKET_LENGTH)
                print("[%s] Client %s sent \'%s\' " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), client_address, data))

                if data:

                        print("[%s] Sending back to client %s ... " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), data))
                        connection.sendall(data.encode('utf-8'))
                else:
                    print("[%s] Client %s disconnected ... " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), client_address))
                    break
            except socket.error:
                    print("[%s] Something happened, but I do not want to bother you ... " % (strftime("%Y-%m-%d %H:%M:%S", gmtime())))

    finally:
        connection.close()


### Zadanie 12
# Serwer ten sam co do zadania 11
# Klient:

import socket

def prepare_message(message, length=20):
    if len(message) < length:
        return message.ljust(length) 
    elif len(message) > length:
        return message[:length]
    return message

def send_all(sock, data):
    total_sent = 0
    while total_sent < len(data):
        sent = sock.send(data[total_sent:])
        if sent == 0:
            raise RuntimeError("Socket connection broken")
        total_sent += sent

def recv_all(sock, length):
    data = b''
    while len(data) < length:
        chunk = sock.recv(length - len(data))
        if chunk == b'':
            raise RuntimeError("Socket connection broken")
        data += chunk
    return data

def main():

    server_address = ("127.0.0.1", 2908)

    msg = input("Podaj wiadomość do wysłania (max 20 znaków): ")
    prepared_msg = prepare_message(msg)

    try:
       
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            print(f"Łączenie z serwerem {server_address}...")
            client_socket.connect(server_address)
            
            print(f"Wysyłanie wiadomości: '{prepared_msg}'")
            send_all(client_socket, prepared_msg.encode('utf-8'))


            response = recv_all(client_socket, 20).decode('utf-8') 
            print(f"Otrzymano wiadomość od serwera: '{response}'")
    
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    main()

### Zadanie 13
# Klient:
import socket
udp_datagram = "ed740b550024effd70726f6772616d6d696e6720696e20707974686f6e2069732066756e"
udp_datagram = "0b54898b1f9a18ecbbb164f2801800e3677100000101080a02c1a4ee001a4cee68656c6c6f203a29"
source_port = int(udp_datagram[0:4],base=16)
destination_port = int(udp_datagram[4:8],base=16)

data = bytes.fromhex(udp_datagram[64:]).decode('utf-8')

msg = f"zad13odp;src;{source_port};dst;{destination_port};data;{data}"
add = '127.0.0.1' # 212.182.24.27
try:
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    client_socket.sendto(msg.encode(),(add,2909))
    response, server = client_socket.recvfrom(1024)
    print(f"Otrzymano wiadomosc od serwera: {response.decode('utf-8')}")
except Exception as e:
    print(e)
finally:
    client_socket.close()

# Serwer:
import socket, select, sys
from time import gmtime, strftime


def check_msg_syntax(txt):
    s = len(txt.decode().split(";"))
    if s != 7:
        return "BAD_SYNTAX"
    else:
        tmp = txt.decode().split(";")
        if tmp[0] == "zad13odp" and tmp[1] == "src" and tmp[3] == "dst" and tmp[5] == "data":
            try:
                src_port = int(tmp[2])
                dst_port = int(tmp[4])
                data = str(tmp[6])
            except :
                return "BAD_SYNTAX:"
            if src_port == 2900 and dst_port == 35211 and data == "hello :)":
                return "TAK"
            else:
                return "NIE"
        else:
            return "BAD_SYNTAX"


HOST = '127.0.0.1'
PORT = 2909

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print("[%s] UDP ECHO Server is waiting for incoming connections ... " % strftime("%Y-%m-%d %H:%M:%S", gmtime()))


try:
    while True:

        data, address = sock.recvfrom(1024)
        print('[%s] Received %s bytes from client %s. Data: %s' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), len(data), address, data))

        if data:

            answer = check_msg_syntax(data)
            sent = sock.sendto(answer.encode('utf-8'), address)
            print('[%s] Sent %s bytes bytes back to client %s.' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address))
finally:
    sock.close()

### Zadanie 14
# Klient:
import socket
udp_datagram = "ed740b550024effd70726f6772616d6d696e6720696e20707974686f6e2069732066756e"
source_port = int(udp_datagram[0:4],base=16)
destination_port = int(udp_datagram[4:8],base=16)
data = bytes.fromhex(udp_datagram[16:]).decode('utf-8')
message = f"zad14odp;src;{source_port};dst;{destination_port};data;{data}"
add = '127.0.0.1' # 212.182.24.27
try:
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    client_socket.sendto(message.encode(),(add,2910))
    response, server = client_socket.recvfrom(1024)
    print(f"Otrzymano wiadomosc od serwera: {response.decode('utf-8')}")
except Exception as e:
    print(e)
finally:
    client_socket.close()


# Serwer:
import socket, select, sys
from time import gmtime, strftime


def check_msg_syntax(txt):
    s = len(txt.split(";"))
    if s != 7:
        return "BAD_SYNTAX"
    else:
        tmp = txt.split(";")
        if tmp[0] == "zad14odp" and tmp[1] == "src" and tmp[3] == "dst" and tmp[5] == "data":
            try :
                src_port = int(tmp[2])
                dst_port = int(tmp[4])
                data = tmp[6]
            except :
                return "BAD_SYNTAX"
            if src_port == 60788 and dst_port == 2901 and data == "programming in python is fun":
                return "TAK"
            else:
                return "NIE"
        else:
            return "BAD_SYNTAX"


HOST = '127.0.0.1'
PORT = 2910

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print("[%s] UDP ECHO Server is waiting for incoming connections ... " % strftime("%Y-%m-%d %H:%M:%S", gmtime()))


try:
    while True:

        data, address = sock.recvfrom(1024)
        print('[%s] Received %s bytes from client %s. Data: %s' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), len(data), address, data))

        if data:

            answer = check_msg_syntax(data.decode('utf-8'))
            sent = sock.sendto(answer.encode('utf-8'), address)
            print('[%s] Sent %s bytes bytes back to client %s.' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address))
finally:
    sock.close()
