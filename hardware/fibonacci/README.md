# Fibonacci

    Cette épreuve fait partie de la série qui utilise la machine virtuelle du FCSC 2023, plus d'informations sur celle-ci ici : https://www.france-cybersecurity-challenge.fr/vm

Cette fois, on vous demande de coder en assembleur la suite de Fibonacci.

La machine est initialisée avec une valeur n aléatoire (mise dans le registre R5) et devra contenir (dans R0) l'élément Fib(n) une fois le code exécuté. Pour rappel :

    Fib(0) = 0,
    Fib(1) = 1,
    Fib(n) = Fib(n - 1) + Fib(n - 2).

Le code machine (bytecode) sera envoyé sous un format hexadécimal, qu'on pourra générer à l'aide de l'assembleur fourni (fichier assembly.py).

```nc challenges.france-cybersecurity-challenge.fr 2301```

# Solution

Here, we are given the formula for the fibonnacci sequence and told to compute Fib(n) for a n in the register R5.

The hard part for me was to write the *ASM* code as I never made anything in *ASM* before.


The first thing I did was to check wether the given n was 0 or 1:
$$\forall n\in\{0,1\}, Fib(n) = n$$

```asm
MOV R0, #0 ; init Fib(0)=0 in R0
MOV R1, #1 ; init Fib(1)=1 in R1

MOV R2, #0
CMP R5, R2 ; Z = R5==R2
JNZR L1 ; Jump to L1 if n != 0

MOV R0, R5 ; return n
STP


L1:
MOV R2, #1
CMP R5, R2
JNZR loop ; Jump to loop if n != 1

MOV R0, R5 ; return n
STP
```

Then I needed to write the loop: until n is reached, compute $R_2 = R_0 + R_1$ and shift the registers to the left.

```asm
loop:
ADD R2, R0, R1 ; add R0 and R1
MOV R0, R1 ; shift registers
MOV R1, R2 ; shift registers

; Decrement R5 and check if R5=1 to stop
MOV R2, #1
SUB R5, R5, R2
CMP R5, R2
JNZR loop

MOV R0, R1
STP
```

Full code is available in ```assembly.py```