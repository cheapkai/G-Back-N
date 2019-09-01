from datetime import datetime
import numpy as np
import sys


from socket import *

abl = [] #all packets - 500
avl = [None]*500 #the window - buffer for packets

time_stamp = [] #window for timestamps

anchor = -1 #the last packet sent


itb = 0
itv = 0

for i in range(500):
	abl.append(i)

print len(abl)

print abl[3]


#sys.exit()

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


#abl = []
#avl = []

#for i in range(500):
#	abl.append(i)

#print len(abl)

#sys.exit() 

nfr = 499
Ws = 4 #window size 
Slast = 0 #last packet sent
Srecent = -100
Nframes = 50
Acksn = -1
m = 3
T = 0
Tfirst = 0 #head of abl
Tlast = -1 #tail of abl
Slast = Tfirst % 8
Srecent = Tlast
b1 = 0
b2 = Ws - 1
it = -1
ab = -1
pknot = 0.01

p = 0.02

#tinv = 10msec

flag = 0

perr = pknot + (1 - pknot)*(1 - ((1 - p)*(1 - p)*(1 - p)))

perr = round(perr, 2)

print 'perr :', perr

perr = 0.00100

while Acksn < 499 :

	print 'T =', T




	print 'waiting for data'
	data = clientSocket2.recv(1024)
	if not data :
		a = 2
		print 'no data'
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
				



				Tfirst = Tfirst + 1
				Slast = Tfirst % 8

				#print 'Slast updated :', Slast

			#if Acksn < 0 :
			#	print 'Acksn < 0', Acksn
			#	Acksn = 0\\

		if datto == 3 :

			flag = 3

			so = int(dats[0], 2)

			#Tlast = Tfirst


			#Slast = Tfirst % 8



	if flag == 0 :

		if (Tlast - Tfirst + 1) < Ws :

			if (Tlast + 1) <= 499:
				Tlast = Tlast + 1

				Srecent =  Tlast % 8


				if Tlast < 0 :

					Tlast = Tfirst
					Slast = Tfirst % 8

					Srecent = Slast

					#print 'Srecent = Slast'

					#print 'sent Slast'

					s = np.random.uniform(0,1)

					s = round(s, 5)

					k = 0 if s <= perr else 1

					cap = str(datetime.now().time())

					caps = cap.split(':')

					hr = int(caps[0])*60*60

					mi = int(caps[1])*60

					sec = int(round(float(caps[2])))

					tim = hr + mi + sec

					avl[Tlast] = tim






					#sentr = raw_input('Enter k:')

					#k = int(sentr)

					strd = str('{0:03b}'.format(Srecent)) + " " + str(k) 

					T = T + 1

					clientSocket.send(str(strd))


				else :

					if  Slast <= ((Srecent ) % 8) <= ((Slast + Ws - 1) % 8) :

						#Srecent = (Srecent + 1) % 8

						#print 'Srecent in range'

						#print 'sent Srecent', Srecent

						s = np.random.uniform(0,1)

						s = round(s, 5)

						k = 0 if s <= perr else 1

						cap = str(datetime.now().time())

						caps = cap.split(':')

						hr = int(caps[0])*60*60

						mi = int(caps[1])*60

						sec = int(round(float(caps[2])))

						tim = hr + mi + sec

						avl[Tlast] = tim

						#	sentr = raw_input('Enter k :')

						#	k = int(sentr)

						strd = str('{0:03b}'.format(Srecent)) + " " + str(k)
						T = T + 1 

						clientSocket.send(str(strd))

					elif (Slast <= ((Srecent ) % 8) <= 7) and (((Slast + Ws -1) % 8) <= Slast) :

						#Srecent = (Srecent + 1) % 8

						#print 'Srecent in range in circular'

						#print 'sent Srecent', Srecent

						s = np.random.uniform(0,1)

						s = round(s, 5)

						k = 0 if s <= perr else 1

						cap = str(datetime.now().time())

						caps = cap.split(':')

						hr = int(caps[0])*60*60

						mi = int(caps[1])*60

						sec = int(round(float(caps[2])))

						tim = hr + mi + sec

						avl[Tlast] = tim


						#	sentr = raw_input('Enter k :')

						#	k = int(sentr)

						strd = str('{0:03b}'.format(Srecent)) + " " + str(k)

						T = T + 1 

						clientSocket.send(str(strd))


					elif (((Slast + Ws -1) % 8) <= Slast) and (0 <= ((Srecent ) % 8) <= ((Slast + Ws - 1) % 8)) :

						#Srecent = (Srecent + 1) % 8

						#print 'Srecent in range in circular'

						#print 'sent Srecent', Srecent

						s = np.random.uniform(0,1)

						s = round(s, 5)

						k = 0 if s <= perr else 1

						#	sentr = raw_input('Enter k :')

						#	k = int(sentr)


						cap = str(datetime.now().time())

						caps = cap.split(':')

						hr = int(caps[0])*60*60

						mi = int(caps[1])*60

						sec = int(round(float(caps[2])))

						tim = hr + mi + sec

						avl[Tlast] = tim

				

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

						cap = str(datetime.now().time())

						caps = cap.split(':')

						hr = int(caps[0])*60*60

						mi = int(caps[1])*60

						sec = int(round(float(caps[2])))

						tim = hr + mi + sec

						avl[Tlast] = tim


						#	sentr = raw_input('Enter k :')

						#	k = int(sentr)

						strd = str('{0:03b}'.format(Srecent)) + " " + str(k)

						T = T + 1 

						clientSocket.send(str(strd))

			elif avl[Tlast] != None :

				cap = str(datetime.now().time())

				caps = cap.split(':')

				hr = int(caps[0])*60*60
				mi = int(caps[1])*60
				sec = int(round(float(caps[2])))

				tim = hr + mi + sec

				if (tim - int(avl[Tlast])) >= 5 :

					Tlast = Tfirst

					Slast = Tfirst % 8

					Srecent = Slast

					s = np.random.uniform(0,1)

					s = round(s, 5)

					k = 0 if s <= perr else 1

					cap = str(datetime.now().time())

					caps = cap.split(':')

					hr = int(caps[0])*60*60

					mi = int(caps[1])*60

					sec = int(round(float(caps[2])))

					tim = hr + mi + sec

					avl[Tlast] = tim




					strd = str('{0:03b}'.format(Srecent)) + " " + str(k)

					T = T + 1 

					clientSocket.send(str(strd))

				else :

					strd = str('{0:03b}'.format(Srecent)) + " " + str(0)

					clientSocket.send(str(strd))
					

			else :

				print 'avl[Tlast] is none'
		
		elif avl[Tfirst] != None :

			cap = str(datetime.now().time())
			caps = cap.split(':')

			hr = int(caps[0])*60*60

			mi = int(caps[1])*60

			sec = int(round(float(caps[2])))

			tim = hr + mi + sec

			if (tim - int(avl[Tfirst])) >= 5 :

				Tlast = Tfirst

				Slast = Tfirst % 8

				Srecent = Slast

				s = np.random.uniform(0,1)

				s = round(s, 5)

				k = 0 if s <= perr else 1

				cap = str(datetime.now().time())
				caps = cap.split(':')

				hr = int(caps[0])*60*60

				mi = int(caps[1])*60

				sec = int(round(float(caps[2])))

				tim = hr + mi + sec

				avl[Tlast] = tim

			


				













				strd = str('{0:03b}'.format(Srecent)) + " " + str(k)

				T = T + 1

				clientSocket.send(str(strd))

			else :

				strd = str('{0:03b}'.format(Srecent)) + " " + str(k)

				clientSocket.send(str(strd))



			


		else :

			print 'avl[Tfirst] is None'
				 




	if flag == 3 :

		flag = 0

		if Tlast < 0 :

			Tlast = Tfirst

			Slast = Tfirst % 8

			Srecent = Slast

			s = np.random.uniform(0,1)
			s = round(s, 5)
			k = 0 if s <= perr else 1

			cap = str(datetime.now().time())
			caps = cap.split(':')

			hr = int(caps[0])*60*60

			mi = int(caps[1])*60

			sec = int(round(float(caps[2])))

			tim = hr + mi + sec

			avl[Tlast] = tim



			strd = str('{0:03b}'.format(Srecent)) + " " + str(k)

			T = T + 1

			clientSocket.send(str(strd))









			#Srecent = Slast

			#print 'Srecent = Slast'

			#print 'sent Slast'

			#s = np.random.uniform(0,1)

			#s = round(s, 5)

			#k = 0 if s <= perr else 1

			#sentr = raw_input('Enter k:')

			#k = int(sentr)

			#strd = str('{0:03b}'.format(Srecent)) + " " + str(k) 

			#T = T + 1

			#clientSocket.send(str(strd))


		else :

			Tlast = Tfirst

			Slast = Tfirst % 8


			Srecent = Slast

			#print 'Srecent out of range - Going Back N'

			#print 'Srecent = Slast'

			#print 'sent Slast'

			s = np.random.uniform(0,1)

			s = round(s, 5)

			k = 0 if s <= perr else 1

			cap = str(datetime.now().time())
			caps = cap.split(':')

			hr = int(caps[0])*60*60

			mi = int(caps[1])*60

			sec = int(round(float(caps[2])))

			tim = hr + mi + sec



			avl[Tlast] = tim

			#	sentr = raw_input('Enter k :')

			#	k = int(sentr)



			strd = str('{0:03b}'.format(Srecent)) + " " + str(k)

			T = T + 1 

			clientSocket.send(str(strd))	




				




			



fob = float(float(500)/float(T))

print 'Efficiency =',(fob)
	

clientSocket.close()
clientSocket2.close()