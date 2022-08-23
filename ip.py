import urllib.request
import time
import socket

def getIp():
	while True:
		hostname = socket. gethostname()
		IPAddr = socket. gethostbyname(hostname)
		print("Your Computer Name is:" + hostname)
		print("Your Computer IP Address is:" + IPAddr)
		#How to get the IP address of a client using socket.
		external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
		print("External ip: ", external_ip);
		time.sleep(2);

if __name__ == "__main__":
	getIp();
