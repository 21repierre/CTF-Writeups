# Oracle cassé

## Description

> Cette description fait référence à un challenge de l'édition précédente qu'il n'est absolument pas nécessaire de connaître pour faire ce challenge.
Communiqué de la direction du 404CTF
>
> Nous souhaitons prendre la parole pour vous dire que nous avons compris vos plaintes concernant les oracles de l'édition précédente. Nous comprenons que ces derniers ont été jugés injustes et trop difficiles à deviner, et c'est pourquoi nous avions décidé de les retirer. C'est pourquoi nous avons décidé de refaire un nouvel oracle, avec les toutes dernières technologies d'optimisation à notre disposition. Afin de nous excuser pour la gène occasionnée, nous offrons aux 1000 premiers arrivés un cadeau à récupérer directement dans l'oracle. Par souci de transparence, nous vous fournirons cette fois-ci le code de fonctionnement exact de cet oracle.<br>
> Nous vous prions d'agréer, Madame, Monsieur, l'expression de nos salutations distinguées.
> Colette, directrice du Matin et du 404CTF
> 
> Toutes les informations neécessaires à la résolution de ce challenge sont présentes dans l'énoncé ci-dessus.

## First look at the challenge

According to the title, we have a broken oracle and after glancing a little at the source code, I immediatly recognized RSA.<br>
Furthermore, the decryption part, implemented in the `oracle` function uses the Chinese remainder theorem for a faster decryption.<br>
However, there was an error in the implementation and it was quiete easy to verify as we are given the encrypted flag.<br>
Giving it back to the oracle gives us something looking like random bytes, at least not like a flag.

## The error

Looking around on internet for implementation of RSA-CRT (like [here](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Using_the_Chinese_remainder_algorithm)) we can observe the the code for the oracle is almost the same except for the definition of $q_{inv}$.
- Good implementation: $q_{inv}=q^{-1} \mod p$
- Bad implementation: $q_{inv}=p^{-1} \mod q$

But why is it such a big deal ?

What should be calculated is a message $m$ that respect those conditions:
$$
\begin{aligned}
m & \equiv m_2 + hq \pmod{q} \\
& \equiv m_2 \pmod{q} + hq \pmod{q} \\
& \equiv m_2 \pmod{q} \\
\end{aligned}
$$
$$
\begin{aligned}
m & \equiv m_2 + hq \pmod{p} \\
& \equiv m_2 + q_{inv} * (m_1 - m_2) * q \pmod{p} \\
& \equiv m_1 \pmod{p} \\
\end{aligned}
$$

In the second equation, $q_{inv} * q = 1$ because $q_{inv}$ is $q$'s inverse modulo $p$.<br>
However in this oracle, $q_{inv}$ is $p$'s inverse modulo $q$. This is what causes messages greter than $q$ to be incorrecly decrypted.

This way we can attack the oracle using dichotomy to find $q$: 
```
start <- 0
end <- n

While (end - start) is larger than 1 Do
	message <- (end - start) // 2
	message_c <- encrypt(message)
	message_dc <- oracle(message_c)
	If message_dc is not message Then
		start <- message
	Else
		end <- message

return end
```
Here we have $q$ and we can easily recover $p, d$ and the flag.

Flag: `404CTF{Un_0r4cl3_vr41m3n7_c4553_c3773_f015}`