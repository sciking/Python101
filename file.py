A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
M = 0
R = 0
temp = 0
from math import sqrt
def p101():
	dent = raw_input("")
	global A,B,C,D,E,F,M,R,temp
	try:
		float(dent)
		M=float(dent)
	except:
		temp = 343

#funzione per la stampa
	if "#" in dent:
		if "A" in dent:
			print A
		if "B" in dent:
			print B
		if "C" in dent:
			print C
		if "D" in dent:
			print D
		if "E" in dent:
			print E
		if "F" in dent:
			print F
		if "M" in dent:
			print M
		if "R" in dent:
			print R
		if "/#" in dent:
			print ""

#addizione, ossia A = A + reg selezionato. 
	if "+" in dent:
		if "A" in dent:
			M = A
			A = A*2
		if "B" in dent:
			M = B
			A = A+B
		if "C" in dent:
			M = C
			A = A+C
		if "D" in dent:
			M = D
			A = A+D
		if "E" in dent:
			M = E
			A = A+E
		if "F" in dent:
			M = F
			A = A+F
		if "M" in dent:
			A = A+M
		print A

#moltiplicazione, ossia A = A * reg selezionato. 
	if "x" in dent:
		if "A" in dent:
			M = A
			A = A*A
		if "B" in dent:
			M = B
			A = A*B
		if "C" in dent:
			M = C
			A = A*C
		if "D" in dent:
			M = D
			A = A*D
		if "E" in dent:
			M = E
			A = A*E
		if "F" in dent:
			M = F
			A = A*F
		if "M" in dent:
			A = A*M
		print A

#sottrazione, ossia A = A - reg selezionato. 
	if "-" in dent:
		if "A" in dent:
			M = A
			A = 0
		if "B" in dent:
			M = B
			A = A-B
		if "C" in dent:
			M = C
			A = A-C
		if "D" in dent:
			M = D
			A = A-D
		if "E" in dent:
			M = E
			A = A-E
		if "F" in dent:
			M = F
			A = A-F
		if "M" in dent:
			A = A-M
		print A

#divisione, ossia A = A : reg selezionato. 
	if ":" in dent:
		if "A" in dent:
			M = A
			A = 1
		if "B" in dent:
			M = B
			R = A%B
			A = A/B
		if "C" in dent:
			M = C
			R = A%C
			A = A/C
		if "D" in dent:
			M = D
			R = A%D
			A = A/D
		if "E" in dent:
			M = E
			R = A%E
			A = A/E
		if "F" in dent:
			M = F
			R = A%F
			A = A/F
		if "M" in dent:
			R = A%M
			A = A/M
		print A
#radice quadrata
	if "v" in dent:
		if "A" in dent:
			A = sqrt(A)
			M = A*2
		if "B" in dent:
			A = sqrt(B)
			M = A*2
		if "C" in dent:
			A = sqrt(C)
			M = A*2
		if "D" in dent:
			A = sqrt(D)
			M = A*2
		if "E" in dent:
			A = sqrt(E)
			M = A*2
		if "F" in dent:
			A = sqrt(F)
			M = A*2
		if "M" in dent:
			A = sqrt(M)
			M = A*2
		print A
#trasferimento da M
	if "!" in dent:
		if "A" in dent:
			A = abs(A)
		if "B" in dent:
			B = M
		if "C" in dent:
			C = M
		if "D" in dent:
			D = M
		if "E" in dent:
 			E = M
		if "F" in dent:
 			F = M
#trasferimento in A
	if "^" in dent:
		if "B" in dent:
			A = B
		if "C" in dent:
			A = C
		if "D" in dent:
			A = D
		if "E" in dent:
 			A = E
		if "F" in dent:
 			A = F
		if "M" in dent:
			A = M
#scambio con A
	if "><" in dent:
		if "B" in dent:
			temp = B
			B = A
			A = temp
		if "C" in dent:
			temp = C
			C = A
			A = temp
		if "D" in dent:
			temp = D
			D = A
			A = temp
		if "E" in dent:
			temp = E
			E = A
			A = temp
		if "F" in dent:
			temp = F
			F = A
			A = temp
		if "M" in dent:
			temp = M
			M = A
			A = temp
		if "/><" in dent: #per la parte decimale di A in M
			temp = int(A)
			M = A - int(A)

#funzione per la pulizia
	if "*" in dent:
		if "A" in dent:
			A = 0
		if "B" in dent:
			B = 0
		if "C" in dent:
			C = 0
		if "D" in dent:
			D = 0
		if "E" in dent:
			E = 0
		if "F" in dent:
			F = 0
		if "M" in dent:
			M = 0
		if "R" in dent:
			R = 0

	if "help" in dent:
		print """
SIMULATORE DI PROGRAMMA 101.
Comandi:
X viene usato come sinonimo di registro, eistono B,C,D,E,F per i dati, A per l'elaborazione,
M riceve le immissioni e R per il calcolo.
X+ -> A = A + X (addizione)
X- -> A = A - X (sottrazione)
Xx -> A = A * X (moltiplicazione)
X: -> A = A : X (divisione)
Xv -> A = radice di X, M = doppio della radice di X
X^ -> Mette il contenuto del registro X in A
X! -> Mette il conteniuto del registro M in X
X>< -> Scambia il contenuto di A e di X
X* -> Azzera il registro X
"""
	p101()
	
p101()
	
