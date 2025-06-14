### Zadanie 1
# Zakomentowałem, zeby wrzucic plik jako .py
#Telnet nie chciał działać, więc skorzystałem z openssla.

#openssl s_client -connect pop.gmail.com:995

#read R BLOCK
#+OK Gpop ready for requests from 46.205.202.246 a17mb90656255edy
#USER moj_adres_email@gmail.com
#+OK send PASS
#PASS moje_haslo
#+OK Welcome.
#STAT
#+OK 250 13563434

#Liczba wiadomosci: 250


### Zadanie 2

#Telnet nie chciał działać, więc skorzystałem z openssla.

#openssl s_client -connect pop.gmail.com:995

#read R BLOCK
#+OK Gpop ready for requests from 46.205.202.246 a17mb90656255edy
#USER moj_adres_email@gmail.com
#+OK send PASS
#PASS moje_haslo
#+OK Welcome.
#STAT
#+OK 250 13563434


#Liczba bajtów: 13563434

### Zadanie 3

#read R BLOCK
#+OK Gpop ready for requests from 46.205.200.14 p25mb93085703edq
#USER moj_email@gmail.com
#+OK send PASS
#PASS moje_haslo
#+OK Welcome.
#LIST
#+OK 250 messages (13567934 bytes)
#1 7452
#2 4912
#3 8656
#4 22214
#5 24722
#6 14724
#7 22080
#8 20469
#9 26747
#10 25462
#11 22083
#12 22080
#13 22075
#14 22086
#15 22081
#16 24729
#17 47016
#18 31746
#19 20104
#20 32067
#21 57134
#22 55778
#23 59929
#24 60722
#25 62290
#26 26080
#27 67147
#28 88358
#29 27541
#30 43242
#31 58207
#32 61708
#33 62601
#34 75217
#35 67839
#36 58045
#37 24936
#38 67730
#39 61798
#40 25495
#41 35675
#42 43435
#43 61251
#44 24770
#45 34263
#46 54286
#47 24831
#48 35149
#49 30866
#50 37849
#51 36495
#52 24878
#53 24202
#54 33882
#55 36783
#56 55653
#57 54356
#58 52380
#59 60899
#60 16751
#61 55400
#62 50770
#63 68916
#64 16741
#65 57434
#66 53574
#67 16816
#68 58149
#69 51457
#70 25580
#71 47164
#72 25138
#73 49912
#74 25288
#75 51514
#
#Numer wiadomosci rozmiar wiadomosci w bajtach

### Zadanie 4
#read R BLOCK
#+OK Gpop ready for requests from 46.205.200.14 p25mb93085703edq
#USER moj_email@gmail.com
#+OK send PASS
#PASS moje_haslo
#+OK Welcome.
#RETR 211
#moja_wiadomosc...


### Zadanie 5
#read R BLOCK
#+OK Gpop ready for requests from 46.205.200.14 p25mb93085703edq
#USER moj_email@gmail.com
#+OK send PASS
#PASS moje_haslo
#+OK Welcome.
#DELE 2
#+OK Message 2 marked for deletion
#QUIT

### Zadanie 6

import poplib
from getpass import getpass

def check_email():
    try:
        # Pobierz dane od użytkownika
        server_address = "pop.gmail.com"
        username = "moj_email@gmail.com"
        password = "haslo_do_mojego_emaila"

        print("\nŁączenie z serwerem...")
        server = poplib.POP3_SSL(server_address, port=995)
        
        print(server.getwelcome().decode())

        print("Logowanie...")
        server.user(username)
        server.pass_(password)

        print("Pobieranie statystyk skrzynki...")
        message_count, mailbox_size = server.stat()

        print(f"\nLiczba wiadomości: {message_count}")


        print("\nZamykanie połączenia...")
        server.quit()

    except poplib.error_proto as e:
        print(f"Błąd protokołu: {e}")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    check_email()


### Zadanie 7

import poplib
from getpass import getpass

def check_email():
    try:
  
        server_address = "pop.gmail.com"
        username = "moj_email@gmail.com"
        password = "haslo_do_mojego_emaila"

        print("\nŁączenie z serwerem...")
        server = poplib.POP3_SSL(server_address, port=995)
        
        print(server.getwelcome().decode())

        print("Logowanie...")
        server.user(username)
        server.pass_(password)

        print("Pobieranie statystyk skrzynki...")
        message_count, total_size = server.stat()

        print(f"Wiadomosci zajmuja lacznie {total_size} bajtow")

        print("\nZamykanie połączenia...")
        server.quit()

    except poplib.error_proto as e:
        print(f"Błąd protokołu: {e}")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    check_email()


### Zadanie 8

import poplib
from getpass import getpass

def check_email():
    try:
        
        server_address = "pop.gmail.com"
        username = "moj_email@gmail.com"
        password = "haslo_do_mojego_emaila"

        print("\nLaczenie z serwerem...")
        server = poplib.POP3_SSL(server_address, port=995)
        
        print(server.getwelcome().decode())

        print("Logowanie...")
        server.user(username)
        server.pass_(password)

        response, listings, octets = server.list()

        for listing in listings:
            message_number, message_size = listing.decode('utf-8').split()
            print(f"Wiadomosc nr: {message_number} = {message_size} B")

        print("\nZamykanie polaczenia...")
        server.quit()

    except poplib.error_proto as e:
        print(f"Blad protokolu: {e}")
    except Exception as e:
        print(f"Wystapil blad: {e}")

if __name__ == "__main__":
    check_email()

### Zadanie 9 

import poplib
from getpass import getpass

def check_email():
    try:
        server_address = "pop.gmail.com"
        username = "moj_email@gmail.com"
        password = "haslo_do_mojego_emaila"

        print("\nLaczenie z serwerem...")
        server = poplib.POP3_SSL(server_address, port=995)
        
        print(server.getwelcome().decode())

        print("Logowanie...")
        server.user(username)
        server.pass_(password)

        response, listings, octets = server.list()
        max_size = 0
        max_mess_number = 0

        for listing in listings:
            message_number, message_size = listing.decode('utf-8').split()
            if int(message_size) > int(max_size):
                max_size = message_size
                max_mess_number = message_number
        
        response, lines, octets = server.retr(int(max_mess_number))
        max_message_content = "\n".join(line.decode('utf-8') for line in lines)
        print(max_message_content)

        print("\nZamykanie polaczenia...")
        server.quit()

    except poplib.error_proto as e:
        print(f"Blad protokolu: {e}")
    except Exception as e:
        print(f"Wystapil blad: {e}")

if __name__ == "__main__":
    check_email()

### Zadanie 10

import poplib
import email
from email import policy
from email.parser import BytesParser
import os
import base64

server_address = "pop.gmail.com"
username = "moj_email@gmail.com"
password = "haslo_do_mojego_emaila"


def save_attachment(part):
    filename = part.get_filename()
    if not filename:
        return


    os.makedirs(".", exist_ok=True)

    payload = part.get_payload(decode=True)
    file_path = os.path.join(".", filename)

    with open(file_path, 'wb') as file:
        file.write(payload)

    print(f'Załącznik zapisany: {file_path}')

def fetch_email_with_attachments():
    try:
        server = poplib.POP3_SSL(server_address)
        server.user(username)
        server.pass_(password)

        message_count, _ = server.stat()
        print(f'Liczba wiadomości na serwerze: {message_count}')

        if message_count == 0:
            print('Brak wiadomości do pobrania.')
            return

        for i in range(1, message_count + 1):
           
            response, lines, _ = server.retr(i)
            msg_content = b'\r\n'.join(lines)

            msg = BytesParser(policy=policy.default).parsebytes(msg_content)
            print(f'Przetwarzanie wiadomości: {msg["subject"]}')
            attach = False
           
            if msg.is_multipart():
                for part in msg.iter_parts():
                    content_disposition = part.get("Content-Disposition", "")
                    if "attachment" in content_disposition:
                        save_attachment(part)
                        attach = True
            if attach == True:
                break
        server.quit()

    except Exception as e:
        print(f'Wystąpił błąd: {e}')

if __name__ == '__main__':
    fetch_email_with_attachments()


### Zadanie 11

import poplib
import email
from email import policy
from email.parser import BytesParser
import os
import base64

server_address = "pop.gmail.com"
username = "moj_email@gmail.com"
password = "haslo_do_mojego_emaila"


def save_attachment(part):
    filename = part.get_filename()
    if not filename:
        return


    os.makedirs(".", exist_ok=True)

    payload = part.get_payload(decode=True)
    file_path = os.path.join(".", filename)

    with open(file_path, 'wb') as file:
        file.write(payload)

    print(f'Załącznik zapisany: {file_path}')

def fetch_email_with_attachments():
    try:
        server = poplib.POP3_SSL(server_address)
        server.user(username)
        server.pass_(password)

        message_count, _ = server.stat()
        print(f'Liczba wiadomości na serwerze: {message_count}')

        if message_count == 0:
            print('Brak wiadomości do pobrania.')
            return

        for i in range(1, message_count + 1):
           
            response, lines, _ = server.retr(i)
            msg_content = b'\r\n'.join(lines)

            msg = BytesParser(policy=policy.default).parsebytes(msg_content)
            print(f'Przetwarzanie wiadomości: {msg["subject"]}')
            attach = False
           
            if msg.is_multipart():
                for part in msg.iter_parts():
                    content_disposition = part.get("Content-Disposition", "")
                    if "attachment" in content_disposition:
                        save_attachment(part)
                        attach = True
            if attach == True:
                break
        server.quit()

    except Exception as e:
        print(f'Wystąpił błąd: {e}')

if __name__ == '__main__':
    fetch_email_with_attachments()


### Zadnie 12

import socket


EMAILS = [
    "Subject: Hello\nFrom: moj_email@gmail.com\n\nHello.",
    "Subject: Hi\nFrom: twoj_email@gmail.com\n\nHi.",
]

class POP3Server:
    def __init__(self, host='127.0.0.1', port=110):
        self.host = host
        self.port = port
        self.server_socket = None

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Serwer POP3 działa na {self.host}:{self.port}")
        
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Połączenie od {client_address}")
            self.handle_client(client_socket)

    def handle_client(self, client_socket):
        try:
            client_socket.send(b"+OK POP3 server ready\r\n")
            authenticated = False
            
            while True:
                data = client_socket.recv(1024).decode('utf-8').strip()
                print(f"Otrzymano: {data}")
                if not data:
                    break

                command, *args = data.split()
                command = command.upper()

                if command == "USER":
                    client_socket.send(b"+OK User accepted\r\n")

                elif command == "PASS":
                    authenticated = True
                    client_socket.send(b"+OK Password accepted\r\n")

                elif command == "STAT":
                    if authenticated:
                        message_count = len(EMAILS)
                        total_size = sum(len(email) for email in EMAILS)
                        client_socket.send(f"+OK {message_count} {total_size}\r\n".encode('utf-8'))
                    else:
                        client_socket.send(b"-ERR Authenticate first\r\n")

                elif command == "LIST":
                    if authenticated:
                        client_socket.send(f"+OK {len(EMAILS)} messages:\r\n".encode('utf-8'))
                        for i, email in enumerate(EMAILS, start=1):
                            client_socket.send(f"{i} {len(email)}\r\n".encode('utf-8'))
                        client_socket.send(b".\r\n")
                    else:
                        client_socket.send(b"-ERR Authenticate first\r\n")

                elif command == "RETR":
                    if authenticated:
                        if args and args[0].isdigit():
                            message_index = int(args[0]) - 1
                            if 0 <= message_index < len(EMAILS):
                                client_socket.send(b"+OK Message follows:\r\n")
                                client_socket.send(EMAILS[message_index].encode('utf-8') + b"\r\n.\r\n")
                            else:
                                client_socket.send(b"-ERR No such message\r\n")
                        else:
                            client_socket.send(b"-ERR Invalid message number\r\n")
                    else:
                        client_socket.send(b"-ERR Authenticate first\r\n")

                elif command == "DELE":
                    client_socket.send(b"+OK Message deleted\r\n")

                elif command == "QUIT":
                    client_socket.send(b"+OK Goodbye\r\n")
                    break

                else:
                    client_socket.send(b"-ERR Command not recognized\r\n")

        except Exception as e:
            print(f"Błąd: {e}")
        finally:
            client_socket.close()

if __name__ == "__main__":
    server = POP3Server()
    try:
        server.start()
    except KeyboardInterrupt:
        print("\nSerwer zatrzymany.")
