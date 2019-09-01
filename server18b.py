import numpy as np


from socket import *
serverName = 'servername'
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

serverSocket2 = socket(AF_INET,SOCK_STREAM)
serverSocket2.bind(('',12345))
serverSocket2.listen(1)

#serverSocket3 = socket(AF_INET, SOCK_DGRAM)
#serverSocket3.bind(('', 12344))
N = 4
m = 3

pknot = 0.01

p = 0.02

#tinv = 10msec

perr = pknot + (1 - pknot)*(1 - ((1 - p)*(1 - p)*(1 - p)))

perr = round(perr, 5)

perr = 0.00100
print 'perr :', perr



print 'The server is ready to receive haha'
while 1:
	print 'starting'
	connectionSocket, addr = serverSocket.accept()
	#sentence = connectionSocket.recv(1024)
	#commands = sentence.split(' ')
	#num = len(commands)
	#command = commands[0]
	#test = 0
	conn, Addr = serverSocket2.accept()

	#say, first the server receives the number of frames to receive

	Rnext = 0
	Qnext = 0

	strd = str(Rnext) + " " + str(1)
	conn.send(str(strd))

	while Qnext < 500 :

		#print 'inside while Rnext < 50 :'

		data  = connectionSocket.recv(1024)

		#print 'data received '

		#print(repr(data))

		if not data :
			a = 2

		else :

			dats = data.split(" ")
			dat = int(dats[0], 2)

			dalt = int(dats[1])

			print 'dat', dat

			if dat == Rnext  and dalt == 1:

				print 'Updating Rnext :'

				Rnext = Rnext + 1

				Rnext = Rnext % 8

				print 'Rnext :',Rnext

				Qnext = Qnext + 1

				s = np.random.uniform(0,1)

				s = round(s, 5)

				k = 0 if s <= perr else 1






				strd = str('{0:03b}'.format(Rnext)) + " " + str(k)
				conn.send(str(strd))

			


			elif dat != Rnext and dalt == 1 :

				print 'dalt == 1 but dat != Rnext'

				strd = str('{0:03b}'.format(Rnext)) + " " + str(2)

				conn.send(str(strd))






			elif dalt == 0 :

				print 'dalt == 0'

				strd = str('{0:03b}'.format(Rnext)) + " " + str(2)

				conn.send(str(strd))

















			else :
				if dat == (Rnext % N)  and dalt == 1:
					Qnext = Qnext - N

					print 'Updating Rnext in retrans :'
					Rnext = dat

					  #modulo 2^m

					Rnext = Rnext + 1
					Rnext = Rnext % 8


					print 'Rnext :',Rnext

					Qnext = Qnext + 1

					s = np.random.uniform(0,1)

					s = round(s, 5)

					k = 0 if s <= perr else 1

					
					strd = str('{0:03b}'.format(Rnext)) + " " + str(k)
					conn.send(str(strd))


				






	

