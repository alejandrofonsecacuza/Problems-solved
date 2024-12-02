#from math import *
def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))

def solve():
    alphabet_dict = {}
    for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
        alphabet_dict[letter] = i + 1
    for i,number in enumerate('0123456789'):
        alphabet_dict[number]= i
        
    while(True):
        try:
            name1=input()
            name2=input()
        except EOFError:
            break

        val1=0
        val2=0
        band1=True
        while(len(name1)!=1 or band1):
            band1=False
            val1=0
            for l in name1.lower():
                try:
                    val1+=int(alphabet_dict[l])
                except:
                    pass

            name1=str(val1)

        band2=True
        while(len(name2)!=1 or band2):
            band2=False
            val2=0
            for l in name2.lower():
                try:
                    val2+=int(alphabet_dict[l])
                except:
                    pass
                    
                    
            name2=str(val2)
        name1=int(name1)
        name2=int(name2)
        minimun=min(name1,name2)
        maximum=max(name1,name2)
        print("{:.2f} %".format((minimun/maximum)*100))
            

solve()
