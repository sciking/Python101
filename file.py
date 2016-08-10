#Variabili per il debug
A = 10
B = 20
C = 30
D = 40
E = 50
F = 60
M = 70
R = 80
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
	p101()
	
p101()
	
