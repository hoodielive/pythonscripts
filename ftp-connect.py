import socket
def retBanner(ip, port): 
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except: 
		return

def main():
	ip1 = '10.0.1.68'
	ip2 = '10.0.1.96'
	port = 21
	banner = retBanner(ip1, port)
	if banner1:
		print('[+] ' + ip1 + ': ' + banner1)
	banner = retBanner(ip2, port)
	if banner2:
		print('[+] ' + ip2 + ': ' + banner2)
if __name__ == '__main__':
	main()

