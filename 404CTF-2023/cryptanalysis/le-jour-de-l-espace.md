# Le Jour de l'espace

> Rimbaud vous propose une séance initiatique au Oui-ja dans l'aile mystique du café littéraire (oui, oui, ça existe), vous avez une vision ésotérique :
> Alors que vous voyez le texte suivant ueomaspblbppadgidtfn, Rimbaud vous décrit voir un étrange cadre de 50cm de côté, avec des petits carrés de 10cm de côtés, numérotés de 0 à 24 et jetés pêle-mêle sur le sol. Rimbaud n'y comprends rien, mais vous restez obsédé par cette idée, et décidez de résoudre l'énigme.
>
> Toutes les informations nécéssaires à la résolution de ce challenge sont présentes dans l'énoncé ci-dessus.
> Format : 404CTF{cequevousalleztrouver}

After connecting to the oracle, I tried inputing a few different messages to observe the output
- `a` => `aaaaa`
- `aaa` => `aaaaa`
- `aaaaa` => `aaaaa`
- `aaaab` => `idmry`
- `aaaba` => `ubkqx`
- `aaab` => `ubkqx`
- `aaaaaa` => `aaaaaaaaaa`

From this short list we can observe a few things:
- This cipher is using block of length 5
- `a` doesn't modify the output
- any other letter changes the output
- the letter's position matters

Using the hints given in the description of the challenge, I came to the conclusion that the cipher used a matrix (25 squares of 10cm in a 50cm square => 5x5 matrix).<br>
Another interesting thing is that the oracle can't use `z`. This confirms that each letter is associated with a number from 0 to 24.

At that point, I remembered an old challenge that used matrix to encrypt message, the **Hill cipher**.<br>
Each letter is assigned a number (commonly its position in the alphabet, starting at 0), we construct an inversible matrix $C$ using those 25 values and use it to encrypt messages $M$:

$$
C=
\begin{pmatrix}
c_{11} & c_{21} & c_{31} & c_{41} & c_{51} \\
c_{12} & c_{22} & c_{32} & c_{42} & c_{52} \\
c_{13} & c_{23} & c_{33} & c_{43} & c_{53} \\
c_{14} & c_{24} & c_{34} & c_{44} & c_{54} \\
c_{15} & c_{25} & c_{35} & c_{45} & c_{55} \\
\end{pmatrix}
$$
$$
M=
\begin{pmatrix}
m_1 \\
m_2 \\
m_3 \\
m_4 \\
m_5 \\
\end{pmatrix}
$$
$$
\begin{aligned}
M_c & = C\times M \\ 
M_d & = M = C^{-1} \times M_c
\end{aligned}
$$

Knowing this, it is pretty easy to recover $C$.<br>
I already obserbed that `a` doesn't change change anything: `a` is $0$.
And probably `b` is $1$, etc.
What happens when we send `aaaab` ? or `aaaba` ?

$$
M_1=
\begin{pmatrix}
0 \\
0 \\
0 \\
0 \\
1 \\
\end{pmatrix}
M_2=
\begin{pmatrix}
0 \\
0 \\
0 \\
1 \\
0 \\
\end{pmatrix}
$$

$$
M_{c,1}=
\begin{pmatrix}
1 * c_{51} \\
1 * c_{52} \\
1 * c_{53} \\
1 * c_{54} \\
1 * c_{55} \\
\end{pmatrix}
M_{c,2}=
\begin{pmatrix}
1 * c_{41} \\
1 * c_{42} \\
1 * c_{43} \\
1 * c_{44} \\
1 * c_{45} \\
\end{pmatrix}
$$

This way we recover each value of the $C$ matrix, invert it and get the flag!

Here we get:

$$
C=
\begin{pmatrix}
9 & 4 & 18 & 20 & 8 \\
11 & 0 & 2 & 1 & 3 \\
5 & 6 & 7 & 10 & 12 \\
13 & 14 & 15 & 16 & 17 \\
19 & 21 & 22 & 23 & 24 \\
\end{pmatrix}
$$

Here is a sagemath script for decrypting the flag:
```python
R = IntegerModRing(25)
C = Matrix(R, [[9,4,18,20,8],[11,0,2,1,3],[5,6,7,10,12], [13,14,15,16,17],[19,21,22,23,24]])
C_1 = C ^ (-1)
m_c = [ord(x)-ord('a') for x in 'ueomaspblbppadgidtfn']

m = ""

for i in range(0, len(m_c), 5):
	M_c = Matrix(R, m_c[i:i+5]).transpose()
	M = C_1 * M_c
	m += ''.join([chr(Integer(x[0]) + ord('a')) for x in M])

print(m)
```
which gives us `barjavelmaassassinea`.<br>
Reading it in French shows us that the `a` at the end isn't part of the flag (it's due to the x5 padding).

Flag: `404CTF{barjavelmaassassine}`
