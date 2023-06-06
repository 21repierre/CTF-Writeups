# Je veux la lune !

> Caligula est assis seul devant une table du café. Il y a devant lui 5 tasses vides empilées, et une 6e qu'il sirote lentement, ainsi qu'un ordinateur qu'il regarde fixement. Des cernes profonds creusent son visage. Il lève des yeux étonnamment vifs vers vous alors que vous vous approchez de lui.<br>
> Il tend sa main vers son écran d'un air désespéré et s'exclame « Je ne peux plus vivre comme ça, ce monde n'est pas supportable. J'ai besoin de quelque chose de différent. Quelque chose d'impossible, peut-être le bonheur, ou peut-être la lune... Et je sens que ma quête s'approche de sa fin. »<br>
> Vous regardez son écran, et voyez qu'il tente d'accéder sans succès à un fichier.<br>
> « Vous pensez que je suis fou, mais je n'ai jamais pensé aussi clairement ! » Un calcul rapide vous informe qu'il a probablement consommé plus d'un litre de café, et il n'est que 13h. Vous acquiescez lentement. Il reprend « Regardez, Hélicon m'a enfin rapporté la lune, mais il ne m'a pas donné l'accès... le fourbe. Je brûlerai un quart de sa fortune plus tard pour le punir. Aidez-moi ! »
>
> Entre peur et pitié, vous décidez de l'aider à obtenir le contenu du fichier secret.

Here we have a bash script asking for a name and using grep to print the corresponding line from the file `informations.txt`.<br>
We are also told to read a file `lune.txt`, probably where our flag is located.<br>
From the beggining I knew that I needed to exploit how the string I typed would be parsed/used in the script but I didn't know how.

I tried many different thing, including command execution with `$(command)` but it would always fail... because it was way simpler than I thought.

Inputting a string with space would mean spaces ine the command: `test1 test2` => `grep -wie ^test1 test2 informations.txt`.<br>
This grep lines for whole strings matching the regex `^test1` in files `test2` and `informations.txt`.<br>
From here the exploit was quiete simple, `.*` means everything so it would catch a flag un lune.txt.
Input: `.* lune.txt`

Flag: `404CTF{70n_C0EuR_v4_7e_1Ach3R_C41uS}`