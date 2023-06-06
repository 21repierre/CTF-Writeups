# Dessine-moi une courbe elliptique

> Au cours d'une de vos explorations dans le café, vous surprenez la conversation suivante :
>
> Oh ! Ce jour, je m'en souviens parfaitement, comme si c'était hier. À cette époque, je passais mes journées à mon bureau chez moi, avec comme seule occupation de dessiner les illustrations qui m'étaient commandées par les journaux du coin. Je ne m'en rendais pas compte à ce moment, mais cela faisait bien 6 ans que je vivais cette vie monacale sans réelle interaction humaine. Le temps passe vite quand on n'a rien à faire de ses journées. Mais ce jour-là, c'était différent. Je m'apprêtais à commencer ma journée de travail, un peu stressé parce que j'avais des illustrations que je devais absolument finir aujourd'hui. Alors que je venais de m'installer devant ma planche à dessin, quelle ne fut pas ma surprise d'entendre une voix venir de derrière-moi :<br>
> « S'il-te plaît, dessine moi une courbe elliptique. »
Je me suis retourné immédiatement. Un petit bonhomme se tenait derrière moi, dans mon appartement, habillé de façon tout à fait incongrue. Il portait une sorte de tenue de mousquetaire céleste ? Même aujourd'hui je ne sais toujours pas comment la décrire.
> « Quoi ?<br>
> — S'il-te plaît, dessine moi une courbe elliptique. »<br>
> Devant cette situation ubuesque, mon cerveau a lâché, a abandonné. Je ne cherchais plus à comprendre et je me contentais de répondre:<br>
> « Je ne sais pas ce que c'est.<br>
> — Ce n'est pas grave, je suis sûr que tu pourras en dessiner une belle! Répondit l'enfant en rigolant. »<br>
> Machinalement, je pris mon crayon, et je dessinai à main levée une courbe, sans réfléchir. Après quelques instants, je me suis retourné, et j'ai montré le résultat à l'enfant, qui secoua immédiatement la tête.<br>
> « Non, regarde: cette courbe à un déterminant nul, je ne veux pas d'une courbe malade ! »<br>
> À ce moment, je ne cherchais plus à comprendre ce qu'il se passait. J'ai donc fait la seule chose que je pouvais faire, j'en ai redessiné une. Cette fois, l'enfant était très heureux.<br>
> « Elle est magnifique ! Je suis sûr qu'elle sera très heureuse toute seule. »<br>
> Et là, sous mes yeux ébahis, la courbe pris vie depuis mon dessin, et s'envola dans la pièce. Elle se mit à tourner partout, avant de disparaître. J'étais bouche bée, enfin encore plus qu'avant.<br>
> « Ah, elle avait envie de bouger visiblement !<br>
> — Où est-elle partie ?<br>
> — Je ne sais pas. Mais c'est toi qui l'a dessinée ! Tu ne devrais pas avoir de mal à la retrouver. En plus je crois qu'elle t'a laissé un petit souvenir, dit-il en pointant le sol, où une série de chiffres étaient effectivement dessinés sur le parquet.<br>
> — Merci encore ! Sur ce, je dois partir. Au revoir ! »<br>
> Avant que je puisse ouvrir la bouche, il disparût.<br>
> Je ne sais toujours pas ce qu'il s'est passé ce jour-là, mais je retrouverais cette courbe un jour !<br>
>
> Peut-être pourriez-vous l'aider ?

This challenge is quiete simple: given 2 random points $F,G$ from an Elliptic curve of this form $y^2 = x^3 + a * x + b$, we need to recover values of $a,b$.

We have a simple equation system:

$$
(E) \iff
\begin{equation}
\begin{cases}
G_y^2 = G_x^3 + a * G_x + b \\
F_y^2 = F_x^3 + a * F_x + b
\end{cases}\,
\end{equation}
$$

Let $s_G = G_y^2 - G_x^3$ and $s_F = F_y^2 - F_x^3$ be, we now have

$$
\begin{align}
(E) & \iff
\begin{cases}
s_G = a * G_x + b \\
s_F = a * F_x + b
\end{cases}\, \\
& \iff
\begin{cases}
s_G - s_F = a * (G_x - F_x) \\
s_F = a * F_x + b
\end{cases}\, \\
& \iff
\begin{cases}
a = \frac{s_G - s_F}{G_x - F_x}  \\
b = s_F - \frac{s_G - s_F}{G_x - F_x} * F_x
\end{cases}\, \\
\end{align} \\
$$

In Sagemath:
```python
import hashlib
from Crypto.Cipher import AES

p = 231933770389389338159753408142515592951889415487365399671635245679612352781

Gx = 93808707311515764328749048019429156823177018815962831703088729905542530725 
Gy = 144188081159786866301184058966215079553216226588404139826447829786378964579
Hx = 139273587750511132949199077353388298279458715287916158719683257616077625421 
Hy = 30737261732951428402751520492138972590770609126561688808936331585804316784
iv = bytes.fromhex('00b7822a196b00795078b69fcd91280d')
cipher = bytes.fromhex('8233d04a29befd2efb932b4dbac8d41869e13ecba7e5f13d48128ddd74ea0c7085b4ff402326870313e2f1dfbc9de3f96225ffbe58a87e687665b7d45a41ac22')

sg = (pow(Gy, 2, p) - pow(Gx, 3, p)) % p
sh = (pow(Hy, 2, p) - pow(Hx, 3, p)) % p
a = (sg - sh) / (Gx - Hx) % p
b = (sg - a * Gx) % p
print(a, b)


key = str(a) + str(b)
aes = AES.new(hashlib.sha1(key.encode()).digest()[:16], AES.MODE_CBC, iv=iv)
print(aes.decrypt(cipher))
```

Flag: `404CTF{70u735_l35_gr4nd35_p3r50nn3s_0nt_d_@b0rd_373_d35_3nf4n7s}`
