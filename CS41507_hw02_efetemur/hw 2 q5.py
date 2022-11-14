import random
from lfsr import *
#p1(x) = x6 + x5 + x4 + x + 1
#p2(x) = x6 + x2 + 1
#p3(x) = x5 + x3 + 1

length = 256 

L1 = 6
L2= 6
L3 = 5

C1 = [0]*(L1+1)
C2 = [0]*(L2+1)
C3 = [0]*(L3+1)

S1 = [0]*L1
S2 = [0]*L2
S3 = [0]*L3
    
C1[0] = C1[1] = C1[4] = C1[5]= C1[6] = 1
C2[0] = C2[2] = C2[6] = 1
C3[0] = C3[3] = C3[5] = 1

def func(L,C,S):
    for i in range(0,L):            # for random initial state
        S[i] = random.randint(0, 1)
    print ("Initial state: ", S) 

    keystream = [0]*length
    for i in range(0,length):
         keystream[i] = LFSR(C, S)
        
    print ("First period: ", FindPeriod(keystream))
    print("maximum period = ", (2**L)-1)
    if (2**L)-1 > FindPeriod(keystream):
        print("not maximum period")
    else:
        print("maximum period")
    print()    
    
func(L1,C1,S1)
func(L2,C2,S2)
func(L3,C3,S3)