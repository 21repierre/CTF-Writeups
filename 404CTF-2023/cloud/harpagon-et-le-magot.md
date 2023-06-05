# Harpagon et le magot

> Un homme en habits de laquais fait les cents pas, seul au fond du café. Vous vous en approchez par curiosité.
>
><p style="max-width: 60%; margin-left: auto; margin-right: auto; text-align: center;">La Flèche<br>
> Brisant le quatrième mur
> Hé quoi ! Ce coquin d'Harpagon ne se lassera donc jamais d’importuner les jeunes gens ! Voilà donc maintenant qu'il va jusqu'à louer des serveurs pour mettre ses écus à l’abri, alors même qu'il refuse à ses propres enfants la moindre dot. Son fils, mon maître, est désespéré de ne pouvoir prétendre à sa bien-aimée Mariane, que son père tente de lui ravir. Sa fille Élise n'est pas mieux traitée, la voilà promise à un ancêtre. Ha non vraiment, je ne puis me résoudre à les abandonner ! Sachez que j'ai donc mené mon enquête, et je pense avoir trouvé de quoi déstabiliser le coquin. Je ne crois pas qu'il ait jamais réussi à faire marcher sa machine comme il le souhaitait, mais elle dois néanmoins contenir toutes sortes de choses qui pourraient faire avancer notre affaire. Accepteriez-vous de m'apporter votre concours pour dévoiler les secrets du vieil avare afin que nos chers amis puissent plus aisément le raisonner ?</p>
>
> Connectez vous au VPS d'Harpagon, investiguez ce qu'il y a fait et retrouvez son secret.
> - Attention, les services peuvent mettre un peu de temps à démarrer.
> - Harpagon n'est pas très doué et n'a jamais réussi à utiliser sa cassette.
> - Mot de passe : T8h2UKEstg 

On the server, I listed files and k8s pods and found one called **cassette**: a vaultwarden instance.<br>
I tried looking around vaultwarden's files & config but found only one thing: a comment in the pod config file from Harpagon telling us that his secret wasn't there anymore.<br>
Following the hint from the challenge, I understood that the flag wasn't *in* the vault but rather in the pod config file.<br>
After searching a bit on the internet, I found that **helm** allows us to upgrade images but also restore to a prior version.<br>
`helm rollback cassette` + `helm get values cassette` give us the old `values.yml` where the flag is (reversed to avoid grep).

Flag: `404CTF{l@v4r1c3_3s7_1_fl3@u_d0n7_1l_3s7_vict1me}`