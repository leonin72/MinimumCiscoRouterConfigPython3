import getpass
import sys
import telnetlib

HOST = input("Enter the Host: ")
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("conf t\n")
tn.write("hostname US\n")
tn.write("enable secret pass\n")
tn.write("no logging console\n")
tn.write("no ip domain-lookup\n")
tn.write("no service config\n")
tn.write("service password-encryption\n")
tn.write("line console 0\n")
tn.write("password pass\n")
tn.write("login\n")
tn.write("exec-timeout 0 0\n")
tn.write("exit\n")
tn.write("line vty 0 14\n")
tn.write("password pass\n")
tn.write("login\n")
tn.write("exec-timeout 0 0\n")
tn.write("end\n")
tn.write("conf t\n")
tn.write("int fastEthernet 0/0")
tn.write("no shut\n")
tn.write("ip address 192.168.1.1 255.255.255.0\n")
tn.write("end\n")

print tn.read_all()
