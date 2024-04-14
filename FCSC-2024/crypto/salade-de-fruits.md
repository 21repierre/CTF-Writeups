# Salade de fruits


[CF](https://math.stackexchange.com/questions/1195035/large-initial-solutions-to-x3y3-nz3?noredirect=1)

We have the following equations:

$$
\begin{align}
\begin{cases}
x^3 + y^3 &= 94 z^3  \;\;\;\;\;(E_0)\\
x &\geq 1 \\
y &\geq 1 \\
z &\geq 1 \\
x &\geq y \\
x &\geq z \\
\end{cases}
\end{align}
$$

For the first part, we use the following transformation

$$
\begin{align}
\begin{cases}
x &= \frac{36 * Z + v}{6u} \\
y &= \frac{36 * Z - v}{6u} \\
Z &= 94z^3
\end{cases}
\end{align}
$$

to get an Elliptic curve equation $u^3 - 432Z^2 = v^2 (E)$

$$
\begin{align}
& x^3 + y^3 &= 94 z^3 \\
\Leftrightarrow &\; (\frac{36 * Z + v}{6u})^3 + (\frac{36 * Z - v}{6u})^3 &= Z \\
\Leftrightarrow &\; ({36 * Z + v})^3 + ({36 * Z - v})^3 &= Z(6u)^3 \\
\Leftrightarrow &\; 93312 * Z^3 + 216 * Z * v^2 &= 216 * Z*u^3 \\
\Leftrightarrow &\; 93312 * Z^2 + 216 * v^2 &= 216 * u^3 \\
\Leftrightarrow &\; 432 * Z^2 + v^2 &= u^3 \\
\Leftrightarrow &\; u^3 - 432 * Z^2 &= v^2 \\
\end{align}
$$

So the generators of $E$ are points on the curve, so they are solutions to the equation $E_0$.
And each point on the curve is a linear combination of the generators, so each point is a solution too.
In this case, there is one generator $G$. So we just need to find $i$ such that $iG$ fills the remaining conditions.

Using `sagemath` I found $i=11$ and the flag `FCSC{2c69e5056f2a80af36c0880a2395472e51b448730a1c5c06b2b0d8e0a3b466b6}`.
