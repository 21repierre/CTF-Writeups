# Plongeon Rapide Super Artistique

## Challenge

- Difficulty: medium
- Value: 717 pts
- Author: @GMO_Goat
- Files: [PlongeonRapideSuperArtistique.py](PlongeonRapideSuperArtistique.py)

> Vous vous avancez sur le plongeoir, la foule est tellement en liesse que la planche en tremble. C'est le dernier saut avant d'avoir votre note finale et donc votre classement pour ce sport. Vous sautez, le monde se ralentit et, comme à l'entrainement, vous effectuez l'enchaînement de figures que vous avez travaillées. Une fois la tête sortie de l'eau, personne du jury ne montre de note ! Un flash vous frappe, c'est vrai que la note est transmise par chiffrement RSA ! Mais après vos multiples figures aériennes, vous ne vous souvenez que de votre clef publique, et de la trajectoire que vous avez empruntée...

## Writeup

We have the following:

$$
\begin{align}
P,Q &\in \mathcal{Z}[X] \\
N &= PQ \;\; \text{(which is known)} \\
p, q &= P(r), Q(r) \; \text{with} \; r \in \mathcal{Z} \\
n &= p * q
\end{align}
$$

From this, we clearly see that $n = P(r)Q(r) = N(r)$.
So we just have to find the roots of the polynomial $N-n$ to find $r$ which will then give us $p, q$.
Moreover, factoring polynomials is an "easy" task, compared to integers, so $P, Q$ are easily recovered.
Here is my solving script using sagemath:

```python
F = PolynomialRing(ZZ, "x")
x = F.gen()
N = 9621137267597279445*x^14 + 18586175928444648302*x^13 + 32676401831531099971*x^12 + 42027592883389639924*x^11 + 51798494845427766041*x^10 + 63869556820398134000*x^9 + 74077517072964271516*x^8 + 79648012933926385783*x^7 + 69354747135812903055*x^6 + 59839859116273822972*x^5 + 48120985784611588945*x^4 + 36521316280908315838*x^3 + 26262107762070282460*x^2 + 16005081865177344119*x + 5810204145325142255
n = 60130547801168751450983574194169752606596547774564695794919298973251203587128237799602582911050022571941793197314565314876508860461087209144687558341117955877761335067848122512358149929745084363835027292307961660634453113069168408298081720503728087287329906197832876696742245078666352861209105027134133927
r = (N-n).roots()[0][0]
P, Q = N.factor()
P, Q = P[0], Q[0]

p, q = P(r), Q(r)
assert p*q == n
```
