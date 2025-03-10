
# Zadanie 1

file_path = input("Enter file path: ")

with open(file_path,"r") as file:
  contents = file.read()

new_file_path = "lab1zad1.txt"

with open(new_file_path, "w") as new_file:
  new_file.write(contents)

# Zadanie 2

file_path = input("Enter file path: ")

with open(file_path,"r") as file:
  contents = file.read()

new_file_path = "lab1zad2.png"

with open(new_file_path, "w") as new_file:
  new_file.write(contents)

# Zadanie 3

import re

def is_valid_ip(ip_address):
  pattern = r'^(\d{1,3}\.){3}\d{1,3}$' # \d - digits
  if not re.match(pattern, ip_address):
    return False

  parts = ip_address.split('.')
  for part in parts:
    try:
      num = int(part)
      if not 0 <= num <= 255:
        return False
    except ValueError:
      return False

  return True

ip = input("Enter an IP address: ")
if is_valid_ip(ip):
  print(f"{ip} is a valid IP address.")
else:
  print(f"{ip} is not a valid IP address.")

# Zadanie 4

import socket

def get_hostname_from_ip(ip_address):
  try:
    hostname = socket.gethostbyaddr(ip_address)[0] # zwracane: (hostname, aliaslist, ipaddrlist)
    return hostname
  except socket.herror:
    return "Hostname not found for this IP address."
  except socket.gaierror:
    return "Invalid IP address."

ip_address = input("Enter an IP address: ")
hostname = get_hostname_from_ip(ip_address)
hostname

# Zadanie 5

import socket

def get_ip_from_hostname(hostname):
  try:
    ip_address = socket.gethostbyname(hostname)
    return ip_address
  except socket.gaierror:
    return "Hostname not found or invalid."

hostname = input("Enter a hostname: ")
ip_address = get_ip_from_hostname(hostname)
print(f"The IP address for {hostname} is: {ip_address}")

# Zadanie 6

#!/usr/bin/env python

import socket

HOST = input("host:") # 216.58.215.110
PORT = int(input("port number:")) # 80

server_address = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect(server_address)
    print(f"Successfully connected to {HOST} on port {PORT}")
except ConnectionRefusedError:
    print(f"Connection to {HOST} on port {PORT} was refused.")
except OSError as e:
    print(f"An error occurred: {e}")
finally:
    sock.close()

# Zadanie 7

import socket

def check_port(host, port):
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(1)  # Set a timeout for the connection attempt
      s.connect((host, port))
      return True
  except (ConnectionRefusedError, socket.timeout, OSError):
    return False

# Example usage:
host = input("Enter the hostname or IP address: ")
min_port = 22
max_port = 65535
x = False
while x == False and port <= max_port:
  if check_port(host, port):
    print(f"Port {port} on {host} is open.")
    x = True
  else:
    print(f"Port {port} is closed.")
  port+=1
