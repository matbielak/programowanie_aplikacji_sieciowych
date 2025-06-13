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
