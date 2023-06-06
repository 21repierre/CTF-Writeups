from pwn import *
from tqdm import tqdm

r = remote('challenges.404ctf.fr', 31674)

for _ in range(6):
	r.recvline()

ct = r.recvline()
ct = int(ct)
print("ct=", ct)

n = r.recvline().split(b' ')[3][3:]
n = int(n, 16)

print('n=', n)

e = 0x10001

r.recvline()

i = 62
d1 = n//e
c1 = pow(d1,e,n)

r.send(str(c1).encode('ascii'))
r.send(b"\n")

dd1 = int(r.recvline())

while d1 != dd1:
	r.recvline()
	i+=1
	d1 = n // (e**i)
	c1 = pow(d1,e,n)
	r.send(str(c1).encode('ascii'))
	r.send(b"\n")

	dd1 = int(r.recvline())

	print(i, "-"*50)
	print(d1)
	print(dd1)

print(i)

print(n//(e**i))
print(n//(e**(i-1)))

start = n//(e**i)
end = n//(e**(i-1))
tot = end-start

step = tot // 100

ti = 0
lasti = 0

for i in range(n//(e**i), n//(e**(i-1)), n//(e**(i))):
	r.recvline()
	d1 = i
	c1 = pow(d1,e,n)
	r.send(str(c1).encode('ascii'))
	r.send(b"\n")

	dd1 = int(r.recvline())

	print((i-start)/tot, "-"*100)
	print(d1)
	print(dd1)
	if d1 != dd1:
		ti = i
		break
	lasti = i

while tot > 1:
	start = lasti
	end = ti
	tot = end-start
	print(tot)

	r.recvline()
	
	d1 = start + tot // 2
	c1 = pow(d1,e,n)
	r.send(str(c1).encode('ascii'))
	r.send(b"\n")

	dd1 = int(r.recvline())

	if d1 != dd1:
		ti = d1
	else:
		lasti = d1

print("upper bound=", lasti)

p = lasti+1

print("good?", n%p)

q = n//p

# Uses CRT correctly here ;) 
d = pow(e, -1, (p-1) * (q-1))
dP = d % (p-1)
dQ = d % (q-1)
u = pow(q, -1, p)

m1 = pow(ct, dP, p)
m2 = pow(ct, dQ, q)
h = u * (m1-m2) % p
mrec = (m2 + h * q) % n

print("-"*200)
print(mrec)
from Crypto.Util.number import long_to_bytes
print(long_to_bytes(mrec))

r.interactive()




