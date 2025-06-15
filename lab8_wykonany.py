### Zadanie 1
## telnet nie chcial dzialac, uzylem openssl,
## komenda: openssl s_client -connect imap.gmail.com:993
#read R BLOCK
#* OK Gimap ready for requests from 46.205.200.59 b30mb110421474edj
#a1 LOGIN "moj_email@gmail.com" "moje_haslo"
#* CAPABILITY IMAP4rev1 UNSELECT IDLE NAMESPACE QUOTA ID XLIST CHILDREN X-GM-EXT-1 UIDPLUS ENABLE MOVE CONDSTORE ESEARCH UTF8=ACCEPT #LIST-EXTENDED LIST-STATUS LITERAL- SPECIAL-USE APPENDLIMIT=35651584
#a1 OK moj_email@gmail.com authenticated (Success)
#a2 LIST "" "*"
#* LIST (\HasNoChildren) "/" "INBOX"
#* LIST (\HasChildren \Noselect) "/" "[Gmail]"
#* LIST (\All \HasNoChildren) "/" "[Gmail]/All Mail"
#* LIST (\HasNoChildren \Trash) "/" "[Gmail]/Bin"
#* LIST (\Drafts \HasNoChildren) "/" "[Gmail]/Drafts"
#* LIST (\HasNoChildren \Important) "/" "[Gmail]/Important"
#* LIST (\HasNoChildren \Sent) "/" "[Gmail]/Sent Mail"
#* LIST (\HasNoChildren \Junk) "/" "[Gmail]/Spam"
#* LIST (\Flagged \HasNoChildren) "/" "[Gmail]/Starred"
#a2 OK Success
#a3 SELECT "INBOX"
#* FLAGS (\Answered \Flagged \Draft \Deleted \Seen $NotPhishing $Phishing)
#* OK [PERMANENTFLAGS (\Answered \Flagged \Draft \Deleted \Seen $NotPhishing $Phishing \*)] Flags permitted.
#* OK [UIDVALIDITY 1] UIDs valid.
#* 9962 EXISTS
#* 0 RECENT
#* OK [UIDNEXT 15162] Predicted next UID.
#* OK [HIGHESTMODSEQ 1485909]
#a3 OK [READ-WRITE] INBOX selected. (Success)
#a4 SELECT "Sent Mail"
#a4 NO [NONEXISTENT] Unknown Mailbox: Sent Mail (now in authenticated state) (Failure)
#a4 SELECT "[Gmail]/Sent Mail"
#* FLAGS (\Answered \Flagged \Draft \Deleted \Seen $NotPhishing $Phishing)
#* OK [PERMANENTFLAGS (\Answered \Flagged \Draft \Deleted \Seen $NotPhishing $Phishing \*)] Flags permitted.
#* OK [UIDVALIDITY 5] UIDs valid.
#* 176 EXISTS
#* 0 RECENT
#* OK [UIDNEXT 182] Predicted next UID.
#* OK [HIGHESTMODSEQ 1485909]
#a4 OK [READ-WRITE] [Gmail]/Sent Mail selected. (Success)
#a5 SELECT "INBOX"
#* FLAGS (\Answered \Flagged \Draft \Deleted \Seen $NotPhishing $Phishing)
#* OK [PERMANENTFLAGS (\Answered \Flagged \Draft \Deleted \Seen $NotPhishing $Phishing \*)] Flags permitted.
#* OK [UIDVALIDITY 1] UIDs valid.
#* 9962 EXISTS
#* 0 RECENT
#* OK [UIDNEXT 15162] Predicted next UID.
#* OK [HIGHESTMODSEQ 1485909]
#a5 OK [READ-WRITE] INBOX selected. (Success)
#a6 SEARCH ALL
#* SEARCH 1 2 3 4 5 6 7 8 9 10 1 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 #55 ... 9961 9962
#a6 OK SEARCH completed (Success)
#a7 UID FETCH 9962 (FLAGS)
#* 4806 FETCH (UID 9962 FLAGS (\Seen))
#a7 OK Success
#a8 OK FETCH 9962 (FLAGS)
#a8 BAD Unknown command: OK
#a10 STORE 9961 +FLAGS \Seen
#a10 OK Success

## zadania 2-5 wykonalem na przykladzie swojego gmaila, zeby zadania dzialaly nalezy zmienic wartosci email,password dla kazdego zadania na intniejace
### Zadanie 2
import imaplib

server_address = "imap.gmail.com"
email = "moj_email@gmail.com"
password = "moje_haslo"

try:
    mail = imaplib.IMAP4_SSL(server_address)

    mail.login(email, password)

    mail.select("INBOX")

    status, response = mail.search(None, "ALL")
    if status == "OK":
        message_ids = response[0].split()
        message_count = len(message_ids)
        print(f"Liczba wiadomości w skrzynce INBOX: {message_count}")
    else:
        print("Nie udało się pobrać wiadomości.")

    mail.logout()

except Exception as e:
    print(f"Wystąpił błąd: {e}")

### Zadanie 3

import imaplib

server_address = "imap.gmail.com" 
email = "moj_email@gmail.com"
password = "moje_haslo" 

def count_total_emails():
    try:
        mail = imaplib.IMAP4_SSL(server_address)
        mail.login(email, password)

        status, folders = mail.list()
        if status != "OK":
            print("Nie udało się pobrać listy folderów.")
            return

        total_count = 0

        for folder in folders:
            folder_info = folder.decode().split(' "/" ')
            print(f"Folder: {folder_info}")
            if len(folder_info) < 2:
                continue
            folder_name = folder_info[1].strip('"')

            status, _ = mail.select(folder_name)
            if status == "OK":
                status, response = mail.search(None, "ALL")
                if status == "OK":
                    message_ids = response[0].split()
                    total_count += len(message_ids)
                    print(f"Folder: {folder_name}, Wiadomości: {len(message_ids)}")
            else:
                print(f"Nie udało się uzyskać dostępu do folderu: {folder_name}")

        print(f"Całkowita liczba wiadomości we wszystkich skrzynkach: {total_count}")

        mail.logout()

    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        print(f"Total count: {total_count}")

count_total_emails()


### Zadanie 4

import imaplib


server_address = "imap.gmail.com" 
email = "moj_email@gmail.com"  
password = "moje_haslo"


MESSAGE_ID_TO_DELETE = 1 

def delete_email():
    try:

        mail = imaplib.IMAP4_SSL(server_address)


        mail.login(email, password)

        status, _ = mail.select("INBOX")
        if status != "OK":
            print("Nie udało się otworzyć folderu INBOX.")
            return

        status, response = mail.store(str(MESSAGE_ID_TO_DELETE), "+FLAGS", "\\Deleted")
        if status == "OK":
            print(f"Wiadomość o ID {MESSAGE_ID_TO_DELETE} oznaczona do usunięcia.")
        else:
            print(f"Nie udało się oznaczyć wiadomości o ID {MESSAGE_ID_TO_DELETE}.")

        status = mail.expunge()
        if status[0] == "OK":
            print(f"Wiadomość o ID {MESSAGE_ID_TO_DELETE} została usunięta.")
        else:
            print("Nie udało się fizycznie usunąć wiadomości.")

        mail.logout()

    except Exception as e:
        print(f"Wystąpił błąd: {e}")


delete_email()


### Zadanie 5

import imaplib
import email
from email.header import decode_header

def connect_to_imap_server(server, email_user, email_pass):
    try:
        mail = imaplib.IMAP4_SSL(server)
        mail.login(email_user, email_pass)
        return mail
    except Exception as e:
        print(f"Error connecting to IMAP server: {e}")
        return None

def fetch_unread_messages(mail):
    try:
        mail.select("inbox")
        status, messages = mail.search(None, 'UNSEEN')
        if status != "OK":
            print("Error searching inbox.")
            return []

        message_ids = messages[0].split()
        unread_messages = []

        for msg_id in message_ids:
            status, msg_data = mail.fetch(msg_id, "(RFC822)")
            if status != "OK":
                print(f"Error fetching message {msg_id}")
                continue

            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    unread_messages.append((msg_id, msg))
        return unread_messages

    except Exception as e:
        print(f"Error fetching unread messages: {e}")
        return []

def mark_as_read(mail, message_ids):
    try:
        for msg_id in message_ids:
            mail.store(msg_id, "+FLAGS", "\\Seen")
    except Exception as e:
        print(f"Error marking messages as read: {e}")

def print_message_content(msg):
    try:
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else "utf-8")
        print(f"Subject: {subject}")

        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

                if content_type == "text/plain" and "attachment" not in content_disposition:
                    body = part.get_payload(decode=True).decode()
                    print(f"Body: {body}")
                    break
        else:
            body = msg.get_payload(decode=True).decode()
            print(f"Body: {body}")

    except Exception as e:
        print(f"Error printing message content: {e}")

def main():
    server = "imap.example.com"  
    email_user = "moj_email@example.com"  
    email_pass = "moje_haslo"  

    mail = connect_to_imap_server(server, email_user, email_pass)
    if mail is None:
        return

    unread_messages = fetch_unread_messages(mail)

    if not unread_messages:
        print("No unread messages.")
    else:
        for msg_id, msg in unread_messages:
            print_message_content(msg)

        message_ids = [msg_id for msg_id, _ in unread_messages]
        mark_as_read(mail, message_ids)

    mail.logout()

if __name__ == "__main__":
    main()


### Zadanie 6

import socket
import threading

HOST = "127.0.0.1"
PORT = 14300

SIMULATED_MAILBOX = {
    "INBOX": {
        "messages": [
            "Subject: Test Email 1\nFrom: ala@example.com\nTo: bolek@example.com\n\nTest Email number 1",
            "Subject: Test Email 2\nFrom: ala@example.com\nTo: bolek@example.com\n\nTets Email number 2"
        ],
        "flags": ["", "\Seen"]
    }
}

def handle_client(conn, addr):
    print(f"Połączenie od {addr}")
    conn.sendall(b"* OK IMAP4rev1 Service Ready\r\n")

    try:
        while True:
            data = conn.recv(1024).decode("utf-8").strip()
            if not data:
                break

            print(f"Otrzymano: {data}")
            parts = data.split()
            if len(parts) < 2:
                conn.sendall(b"BAD Missing or incomplete command\r\n")
                continue

            tag = parts[0]
            command = parts[1].upper()

            if command == "LOGIN":
                conn.sendall(f"{tag} OK LOGIN completed\r\n".encode("utf-8"))

            elif command == "SELECT":
                mailbox = parts[2] if len(parts) > 2 else ""
                if mailbox.upper() in SIMULATED_MAILBOX:
                    count = len(SIMULATED_MAILBOX[mailbox.upper()]["messages"])
                    conn.sendall(f"* {count} EXISTS\r\n".encode("utf-8"))
                    conn.sendall(f"{tag} OK [READ-WRITE] SELECT completed\r\n".encode("utf-8"))
                else:
                    conn.sendall(f"{tag} NO Mailbox does not exist\r\n".encode("utf-8"))

            elif command == "FETCH":
                if len(parts) < 4:
                    conn.sendall(f"{tag} BAD FETCH syntax error\r\n".encode("utf-8"))
                    continue

                try:
                    message_id = int(parts[2]) - 1
                    if 0 <= message_id < len(SIMULATED_MAILBOX["INBOX"]["messages"]):
                        message = SIMULATED_MAILBOX["INBOX"]["messages"][message_id]
                        conn.sendall(f"* {parts[2]} FETCH (BODY[] {{{len(message)}}}\r\n{message})\r\n".encode("utf-8"))
                        conn.sendall(f"{tag} OK FETCH completed\r\n".encode("utf-8"))
                    else:
                        conn.sendall(f"{tag} NO Message not found\r\n".encode("utf-8"))
                except ValueError:
                    conn.sendall(f"{tag} BAD Invalid message ID\r\n".encode("utf-8"))

            elif command == "LOGOUT":
                conn.sendall(b"* BYE IMAP4rev1 Server logging out\r\n")
                conn.sendall(f"{tag} OK LOGOUT completed\r\n".encode("utf-8"))
                break

            else:
                conn.sendall(f"{tag} BAD Command not implemented\r\n".encode("utf-8"))

    finally:
        print(f"Zamykam połączenie z {addr}")
        conn.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f"Serwer IMAP uruchomiony na {HOST}:{PORT}")

        while True:
            conn, addr = server.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

if __name__ == "__main__":
    start_server()
