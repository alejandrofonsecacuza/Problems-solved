#int 32bits 4byte (-2^31 <-> 2**31-1 || 10^9)

from math import *
"""
1. Representación de Bits en Python

Python permite representar números en varios sistemas numéricos:

    Binario: Usa el prefijo 0b. Ejemplo: 0b1010 (10 en decimal).
"""
num = 10
print(bin(num))  # Output: 0b1010
"""
2. Operaciones a Nivel de Bits

Aquí están las operaciones bit a bit más comunes:

    AND bit a bit (&): Devuelve 1 solo si ambos bits son 1.
    OR bit a bit (|): Devuelve 1 si al menos uno de los bits es 1.
    XOR bit a bit (^): Devuelve 1 si los bits son diferentes.
    NOT bit a bit (~): Invierte todos los bits.
    Desplazamiento a la izquierda (<<): Desplaza los bits hacia la izquierda un número especificado de posiciones, llenando con ceros.
    Desplazamiento a la derecha (>>): Desplaza los bits hacia la derecha un número especificado de posiciones, llenando con el bit de signo para números negativos.
"""
def op():
	print(22 & 26)#and 
	print(22 | 26)#or
	print(22^26)#xor
	print(~50)#not

#Operaciones de corrimiento
print(22 << 4)#Corrimiento a la isquierda
print(22 >> 4)#Corrimiento a la derecha

#Mascara de bits
"""
Bit Masks A bit mask of the form 1 << k has a one bit in position k, and all other
bits are zero, so we can use such masks to access single bits of numbers. In particular,
the kth bit of a number is one exactly when x & (1 << k) is not zero. The following
code prints the bit representation of an int number x:
"""
def binary(x,n):
	s=""
	for i in range(n-1,-1,-1):
		s+=str((1 if (x & (1<<i)) else 0))
	return s


# x | (1 << k) Enciende el k-esimo bit de x
# x & ~ (1 << k) Apaga el k-esimo bit de x
# x ˆ (1 << k) Invierte el k-esimo bit de x
# Un numero positivo x es potencia de dos si x & (x − 1) = 0. 


#Representacion de conjuntos
"""
Every subset of a set {0, 1, 2, . . . , n − 1} can be represented as an n bit integer
whose one bits indicate which elements belong to the subset. This is an efficient way
to represent sets, because every element requires only one bit of memory, and set
operations can be implemented as bit operations.
"""
#For example, since int is a 32-bit type, an int number can represent any subset
#of the set {0, 1, 2, . . . , 31}. The bit representation of the set {1, 3, 4, 8} is
#00000000000000000000000100011010 //282
x = 0;
x |= (1<<1);
x |= (1<<3);
x |= (1<<4);
x |= (1<<8);
print(x)
"""
Set Operations Table 2.1 shows how set operations can be implemented as bit
operations. For example, the following code first constructs the sets x = {1, 3, 4, 8}
and y = {3, 6, 8, 9} and then constructs the set z = x ∪ y = {1, 3, 4, 6, 8, 9}:


Operation Set syntaxBit syntax
Intersection a∩b a&b
Union a∪b a|b
Complement ā ~a
Difference a\b  a&(~ b)
"""
x = (1<<1)|(1<<3)|(1<<4)|(1<<8);
y = (1<<3)|(1<<6)|(1<<8)|(1<<9);
z = x|y;#xuy
z = x&y;#x∩y



#############
def back(l,index):
	if(index==len(N9)):
		print(l)
		return
	for i in (1,0):
		back(l+[i],index+1)
		
#back([],0)
n=5
#for i in range(0,(1<<n)):
#	print(binary(i,4))



def prueba(a,n):
	print(a)
	k=0
	for i in a:
		print(binary(i,n))
print("prueba1")
n=5
a=[2 ,1 ,3 ,4, 5]
prueba(a,n)
print("prueba2")
n=9
a=[2, 4, 5, 6, 7, 1, 3, 8, 9]
prueba(a,n)
	

