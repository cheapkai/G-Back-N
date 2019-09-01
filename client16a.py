import numpy as np



from socket import *
serverName = 'servername'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('127.0.0.1',serverPort))

clientSocket2 = socket(AF_INET, SOCK_STREAM)
clientSocket2.connect(('127.0.0.1',12345))

#sentence = raw_input('Input lowercase sentence:')

#clientSocket.send(sentence)
#strb = "/home/mehthab/SOSC/history"


#modifiedSentence = clientSocket.recv(1024)
#print 'From Server:', modifiedSentence


Ws = 4 #window size 
Slast = 0 #last packet sent
Srecent = -100
Nframes = 50
Acksn = -1
m = 3
T = 0

pknot = 0.01

p = 0.02

#tinv = 10msec

flag = 0

perr = pknot + (1 - pknot)*(1 - ((1 - p)*(1 - p)*(1 - p)))

perr = round(perr, 2)

print 'perr :', perr

perr = 0.5000

while Acksn < 499 :

	print 'T =', T




	#print 'waiting for data'
	data = clientSocket2.recv(1024)
	if not data :
		a = 2
		#print 'no data'
	else :
		#ack has m bits plus one representing it i reached correctly or not
		#print 'yes data'
		dats = data.split(" ")

		datto = int(dats[1])

		if datto == 1 :

			
			so = int(dats[0], 2)



			if so == ((Slast + 1) % 8) :
				Acksn = Acksn + 1
				#print 'Acksn = ',Acksn

				Slast = (Slast + 1) % 8

				#print 'Slast updated :', Slast

			#if Acksn < 0 :
			#	print 'Acksn < 0', Acksn
			#	Acksn = 0\\

		if datto == 3 :

			flag = 3

			so = int(dats[0], 2)

			Slast = so



	if flag == 0 :

		if Srecent < 0 :

			Srecent = Slast

			#print 'Srecent = Slast'

			#print 'sent Slast'

			s = np.random.uniform(0,1)

			s = round(s, 5)

			k = 0 if s <= perr else 1

			#sentr = raw_input('Enter k:')

			#k = int(sentr)

			strd = str('{0:03b}'.format(Srecent)) + " " + str(k) 

			T = T + 1

			clientSocket.send(str(strd))


		else :


			if  Slast <= ((Srecent + 1) % 8) <= ((Slast + Ws - 1) % 8) :

				Srecent = (Srecent + 1) % 8

				#print 'Srecent in range'

				#print 'sent Srecent', Srecent

				s = np.random.uniform(0,1)

				s = round(s, 5)

				k = 0 if s <= perr else 1

				#	sentr = raw_input('Enter k :')

				#	k = int(sentr)

				strd = str('{0:03b}'.format(Srecent)) + " " + str(k)

				T = T + 1 

				clientSocket.send(str(strd))

			elif (Slast <= ((Srecent + 1) % 8) <= 7) and (((Slast + Ws -1) % 8) <= Slast) :

				Srecent = (Srecent + 1) % 8

				#print 'Srecent in range in circular'

				#print 'sent Srecent', Srecent

				s = np.random.uniform(0,1)

				s = round(s, 5)

				k = 0 if s <= perr else 1

				#	sentr = raw_input('Enter k :')

				#	k = int(sentr)

				strd = str('{0:03b}'.format(Srecent)) + " " + str(k)

				T = T + 1 

				clientSocket.send(str(strd))


			elif (((Slast + Ws -1) % 8) <= Slast) and (0 <= ((Srecent + 1) % 8) <= ((Slast + Ws - 1) % 8)) :

				Srecent = (Srecent + 1) % 8

				#print 'Srecent in range in circular'

				#print 'sent Srecent', Srecent

				s = np.random.uniform(0,1)

				s = round(s, 5)

				k = 0 if s <= perr else 1

				#	sentr = raw_input('Enter k :')

				#	k = int(sentr)

				strd = str('{0:03b}'.format(Srecent)) + " " + str(k)

				T = T + 1 

				clientSocket.send(str(strd))


			else :

				Srecent = Slast

				#print 'Srecent out of range - Going Back N'

				#print 'Srecent = Slast'

				#print 'sent Slast'

				s = np.random.uniform(0,1)

				s = round(s, 5)

				k = 0 if s <= perr else 1

				#	sentr = raw_input('Enter k :')

				#	k = int(sentr)

				strd = str('{0:03b}'.format(Srecent)) + " " + str(k)

				T = T + 1 

				clientSocket.send(str(strd))


	if flag == 3 :

		flag = 0

		if Srecent < 0 :

			Srecent = Slast

			#print 'Srecent = Slast'

			#print 'sent Slast'

			s = np.random.uniform(0,1)

			s = round(s, 5)

			k = 0 if s <= perr else 1

			#sentr = raw_input('Enter k:')

			#k = int(sentr)

			strd = str('{0:03b}'.format(Srecent)) + " " + str(k) 

			T = T + 1

			clientSocket.send(str(strd))


		else :

			Srecent = Slast

			#print 'Srecent out of range - Going Back N'

			#print 'Srecent = Slast'

			#print 'sent Slast'

			s = np.random.uniform(0,1)

			s = round(s, 5)

			k = 0 if s <= perr else 1

			#	sentr = raw_input('Enter k :')

			#	k = int(sentr)

			strd = str('{0:03b}'.format(Srecent)) + " " + str(k)

			T = T + 1 

			clientSocket.send(str(strd))	




				




			



fob = float(float(500)/float(T))

print 'Efficiency =',(fob)
	

clientSocket.close()
clientSocket2.close()