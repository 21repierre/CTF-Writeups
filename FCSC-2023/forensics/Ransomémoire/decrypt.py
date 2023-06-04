flag_enc = open('flag.fcsc.enc', 'rb').read()

rdn_b = open('MsCmdRun14.log', 'rb').read()

tmp = list(flag_enc)
for j in range(len(tmp)):
	tmp[j] ^= rdn_b[j] ^ 14

print(bytes(tmp))