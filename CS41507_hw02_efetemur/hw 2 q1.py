import client

#client.getQ1()
n = 482
t = 16
Q1_a = []
def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a
def egcd(a, b):
    
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd
for x in range (0,n):
    
    if egcd(n,x) == 1:
        Q1_a.append(x)
client.checkQ1a(len(Q1_a))

#print(len(Q1_a))
def primRoots(m):
    
    roots = []
    required_set = set(num for num in range (1, m) if gcd(num, m) == 1)

    for x in range(1, m):
        actual_set = set(pow(x, powers) % m for powers in range (1, m))
        if required_set == actual_set:
            roots.append(x)           
    return roots

a=primRoots(n)

client.checkQ1b(a[0])

for x in range(n):
    list_c = []
    for y in range(t):        
        a = (x**y) % n
        if a not in list_c and a in Q1_a:
            list_c.append(a)
        
    if len(list_c) == t and (x**t)%n in list_c:
        Q1_c = x
        break
   
#print(list_c)
#print(Q1_c)
client.checkQ1c(Q1_c)


