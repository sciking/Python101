A = 10
B = 20
C = 30
D = 40
E = 50
F = 60
M = 70
R = 80
from math import sqrt
def p101():
	dent = raw_input(">")
	global A,B,C,D,E,F,M,R
	try:
		int(dent)
		M=int(dent)
	except:
		print ""

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
	p101()
	
p101()
	
