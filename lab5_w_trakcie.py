### Zadanie 1
import socket

host = '127.0.0.1'
port = 2912

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client_socket:
    try:
        client_socket.connect((host,port))

        while True:
            message = input('Enter number [1-100]')
            client_socket.sendall(message.encode('utf-8'))

            resp = client_socket.recv(1024)
            print(f"Server: {resp.decode('utf-8')}")
    except Exception as e:
        print(f"Error: {e}")
### Zadanie 2
# 
import socket
import random
HOST = '127.0.0.1'
PORT = 2912

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST,PORT))
    server_socket.listen(1)
    print(f"SERVER UDP LISTENING ON PORT: {PORT}")
    random_number = random.randint(1,100)
    while True:
        client_socket, client_address = server_socket.accept()
        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            #print(f"Received: {data.decode('utf-8')} from {client_address}")
            try:
                x = int(data.decode('utf-8'))
               # client_socket.sendall(f"Received {x}.\n".encode('utf-8'))
                if x<random_number:
                    client_socket.sendall(f"Guess Higher\n".encode('utf-8'))
                if x>random_number:
                    client_socket.sendall(f"Guess Lower\n".encode('utf-8'))
                if x==random_number:
                    client_socket.sendall(f"You got it! {random_number} is the answer.\n".encode('utf-8'))
                    server_socket.close()
                    break
            except ValueError:
                client_socket.sendall("Nan".encode('utf-8'))
            
        
                

        # server_socket.sendto(data,client_address)
        # print(f"Sent: {data.decode('utf-8')} to {client_address}")

### Zadanie 3


### Zadanie 4
