### Zadanie 1
# Serwer:
import socket
from datetime import datetime

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST,PORT))
    server_socket.listen(1)
    print(f"SERVER TCP LISTENING ON PORT: {PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        with client_socket:
            print(f"Connected {client_address}")

            data = client_socket.recv(1024)
            #if len(data)>0:
              #  print(f"Received: {data.decode('utf-8')}")

            current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

            client_socket.sendall(current_time.encode('utf-8'))
            print(f"Sent current time: {current_time}")
# Klient do sprawdzenia:
import socket

add = "127.0.0.1" # "212.182.24.27"
port = 65432
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


### Zadanie 2
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST,PORT))
    server_socket.listen(1)
    print(f"SERVER TCP LISTENING ON PORT: {PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        with client_socket:
            print(f"Connected {client_address}")
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"Received: {data.decode('utf-8')}")

            

                client_socket.sendall(data)
                print(f"Echo: {data.decode('utf-8')}")

### Zadanie 3
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST,PORT))
    print(f"SERVER UDP LISTENING ON PORT: {PORT}")

    while True:
       data,client_address = server_socket.recvfrom(1024)
       print(f"Received: {data.decode('utf-8')} from {client_address}")

       server_socket.sendto(data,client_address)
       print(f"Sent: {data.decode('utf-8')} to {client_address}")


### Zadanie 4
import socket

HOST = '127.0.0.1'
PORT = 65432

def solve(n1,op,n2):
    if op=='+':
        return n1 + n2
    if op=='-':
        return n1 - n2
    if op=='*':
        return n1 * n2
    if op=='/':
        return n1 / n2


with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST,PORT))
    print(f"SERVER UDP LISTENING ON PORT: {PORT}")
    n1 = []
    while True:
        data,client_address = server_socket.recvfrom(1024)
        print(f"Received: {data.decode('utf-8')} from {client_address}")
        ops = ['+','-','*','/']
        if data.decode('utf-8') in ops:
           print("oper")
           op = data.decode('utf-8')
        else:
            try:
                x = int(data.decode('utf-8'))
                n1.append(x)
                print("number")
            except ValueError:
                print("what?")
        if len(n1) == 2:
            server_socket.sendto(str(solve(n1[0],op,n1[1])).encode('utf-8'),client_address)
            n1 = []

       # server_socket.sendto(data,client_address)
       # print(f"Sent: {data.decode('utf-8')} to {client_address}")

### Zadanie 5
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST,PORT))
    print(f"SERVER UDP LISTENING ON PORT: {PORT}")

    while True:
        data,client_address = server_socket.recvfrom(1024)
        x = data.decode('utf-8')
        print(f"Received: {x} from {client_address}")
        try:
            hostname,_,_ = socket.gethostbyaddr(x)
            server_socket.sendto(hostname.encode('utf-8'),client_address)
        except socket.herror as e:
            server_socket.sendto("Error".encode('utf-8'),client_address)

       #server_socket.sendto(data,client_address)
       #print(f"Sent: {data.decode('utf-8')} to {client_address}")


# Zadanie 6
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST,PORT))
    print(f"SERVER UDP LISTENING ON PORT: {PORT}")

    while True:
        data,client_address = server_socket.recvfrom(1024)
        x = data.decode('utf-8')
        print(f"Received: {x} from {client_address}")
        try:
            ip_address = socket.gethostbyname(x)
            server_socket.sendto(ip_address.encode('utf-8'),client_address)
        except socket.herror as e:
            server_socket.sendto("Error".encode('utf-8'),client_address)

       #server_socket.sendto(data,client_address)
       #print(f"Sent: {data.decode('utf-8')} to {client_address}")

### Zadanie 7

import socket

add = "127.0.0.1"  
port = 2900  
msg = "Hello" 

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((add, port))
    
    if len(msg) > 20:
        print("Wiadomość jest zbyt długa, zostanie przycięta.")
    msg = msg[:20]
    
    client_socket.sendall(msg.encode('utf-8'))
    print(f"Wysłano do serwera: {msg}")
    
    response = client_socket.recv(20).decode('utf-8')
    print(f"Otrzymano wiadomość od serwera: {response}")

except Exception as e:
    print(f"Błąd: {e}")
finally:
    client_socket.close()

### Zadanie 8

import socket

add = "127.0.0.1"  
port = 2900  
msg = "Hello"

def send_exact(sock, message, length):
    if len(message) > length:
        message = message[:length]
    else:
        message = message.ljust(length) 
    sock.sendall(message.encode('utf-8'))

def receive_exact(sock, length):
    data = b""
    while len(data) < length:
        chunk = sock.recv(length - len(data))
        if not chunk:
            raise ConnectionError("Połączenie zakończone przed odebraniem pełnej wiadomości")
        data += chunk
    return data.decode('utf-8')

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((add, port))
    
    send_exact(client_socket, msg, 20)
    print(f"Wysłano do serwera: {msg[:20]}")

    response = receive_exact(client_socket, 20)
    print(f"Otrzymano wiadomość od serwera: {response}")

except Exception as e:
    print(f"Błąd: {e}")
finally:
    client_socket.close()

### Zadanie 9
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

### Zadanie 10
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


### Zadanie 11
import socket, select, sys
from time import gmtime, strftime


def check_msgA_syntax(txt):
    s = len(txt.split(";"))
    if s != 9:
        return "BAD_SYNTAX"
    else:
        tmp = txt.split(";")
        if tmp[0] == "zad15odpA" and tmp[1] == "ver" and tmp[3] == "srcip" and tmp[5] == "dstip" and tmp[7] == "type":
            try:
                ver = int(tmp[2])
                srcip = tmp[4]
                dstip = tmp[6]
                type = int(tmp[8])
                if ver == 4 and type == 6 and srcip == "212.182.24.27" and dstip == "192.168.0.2":
                    return "TAK"
                else:
                    return "NIE"
            except:
                return "NIE"
        else:
            return "BAD_SYNTAX"


def check_msgB_syntax(txt):
    s = len(txt.split(";"))
    if s != 7:
        return "BAD_SYNTAX"
    else:
        tmp = txt.split(";")
        if tmp[0] == "zad15odpB" and tmp[1] == "srcport" and tmp[3] == "dstport" and tmp[5] == "data":

            try:
                srcport = int(tmp[2])
                dstport = int(tmp[4])
                data = tmp[6]

                if srcport == 2900 and dstport == 47526 and data == "network programming is fun":
                    return "TAK"
                else:
                    return "NIE"
            except:
                return "NIE"
        else:
            return "BAD_SYNTAX"


HOST = '127.0.0.1'
PORT = 2911

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
        print('[%s] Received %s bytes from client %s. Data: %s' % (
        strftime("%Y-%m-%d %H:%M:%S", gmtime()), len(data), address, data))

        if data:

            tmp = data.decode('utf-8').split(";")
            print("DATA: %s" % data)

            if tmp[0] == "zad15odpA":
                answer = check_msgA_syntax(data.decode('utf-8'))
                sent = sock.sendto(answer.encode('utf-8'), address)
                print('[%s] Sent %s bytes bytes back to client %s.' % (
                strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address))

            elif tmp[0] == "zad15odpB":
                answer = check_msgB_syntax(data.decode('utf-8'))
                sent = sock.sendto(answer.encode('utf-8'), address)
                print('[%s] Sent %s bytes bytes back to client %s.' % (
                strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address))

            else:
                sent = sock.sendto("BAD_SYNTAX", address)
                print('[%s] Sent %s bytes bytes back to client %s.' % (
                strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address))
finally:
    sock.close()

