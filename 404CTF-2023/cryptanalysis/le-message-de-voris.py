cipher = 'pvfdhtuwgbpxfhocidqcznupamzsezp'

"""
cipher = 'iyvkqplmgzdodeojjphmltyuknlakqv'
cipher_n = [ord(x)-97 for x in cipher]

base = 'a' * len(cipher)
base_n = [ord(x)-97 for x in base]

base2 = 'gvshnmijdwalablggmejiqvrhkixhns'
base2_n = [ord(x)-97 for x in base2]

print(cipher_n)
print(base_n)
n = len(cipher_n)

for i in range(n-1, -1, -1):
    base_n[n-1-i] = (cipher_n[n-1-i] - base2_n[n-1-i]) % 26
    for j in range(n-1-i, n):
        cipher_n[j] = (cipher_n[j]- base_n[n-1-i]) % 26
    print(base_n, cipher_n)

print(''.join([chr(x + 97) for x in base_n]))"""

def chiffre(m):
    n = len(m)
    b = [ord(x)-97 for x in 'gvshnmijdwalablggmejiqvrhkixhns']

    for i in range(n):
        ti = n-1-i
        
        for j in range(n):
            if j <= i:
                b[j] = (b[j] + (j+1)*m[ti]) % 26
            else:
                b[j] = (b[j] + (i+1)*m[ti]) % 26
    return b

def chiffre2(m):
    n = len(m)
    k = [ord(x)-97 for x in 'gvshnmijdwalablggmejiqvrhkixhns']
    c = [0] * n
    for i in range(n):
        s1 = 0
        s2 = 0
        for j in range(i+1):
            s1 += (j+1) * m[n-1-j]
        for j in range(i+1, n):
            s2 += (i+1) * m[n-1-j]
        c[i] = (k[i] +s1 +s2) % 26
    return c

def dechiffre(m):
    n = len(m)
    b = [0] * n
    k = [ord(x)-97 for x in 'gvshnmijdwalablggmejiqvrhkixhns']
    print("k =",k)
    s = [m[i]-k[i] for i in range(n)]
    #print((2*s[0] - s[1]) % 26)
    #print((3*s[0] - s[2] - 2*(2*s[0] - s[1]) % 26) % 26)
    #print(b,m)

    for i in range(n-1):
        #b[n-1-i] = ((i+1) * (m[i]-k[i]) - (c[i+1] - k[i+1])) % 26
        s1 = 0
        for j in range(0, i):
            s1 += (i+1-j) * b[n-1-j]
        #print(s1)
        b[n-1-i] = ((i+2) * s[0] - s[i+1] - s1) % 26
    b[0] = (s[0] - sum(b))%26
    print("b =", b)
    return b

"""
mess = "bsdfghrtfodijfoijafoijgdfiogjjd"
print(mess)
c = chiffre([ord(x)-97 for x in mess])
c2 = chiffre2([ord(x)-97 for x in mess])
print(''.join([chr(x+97) for x in c]))
print(''.join([chr(x+97) for x in c2]))
print("m =",[ord(x)-97 for x in mess])
print("c =", c)
d = dechiffre(c)
print(''.join([chr(x+97) for x in d]))"""


print(''.join([chr(x+97) for x in dechiffre([ord(x)-97 for x in 'pvfdhtuwgbpxfhocidqcznupamzsezp'])]))