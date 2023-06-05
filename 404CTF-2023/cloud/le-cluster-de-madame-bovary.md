# Le Cluster de Madame Bovary

> Un individu dans un coin vous interpelle et vous invite à sa table. Une fois assis, il vous explique qu'il veut que vous infiltriez le cluster Kubernetes de Madame Bovary. Madame Bovary est une femme riche et influente qui a investi dans la technologie Kubernetes pour gérer les applications de son entreprise de production de médicaments. Vous vous doutez qu'il s'agit sans doute d'un concurrent industriel mais il vous offre une belle récompense si vous réalisez sa demande.
>
> Votre mission consiste à prendre le contrôle du cluster Kubernetes de Madame Bovary et à accéder à ses applications critiques. Vous devrez exploiter toutes les vulnérabilités possibles pour atteindre votre objectif.
>
> Le fichier fourni est une machine virtuelle à charger dans Virtualbox. Cette machine virtuelle contient le cluster Kubernetes du challenge.
> - Utilisateur : ctf
> - Mot de passe : 404ctf2023

It's clear that we need to find something in a kubernetes cluster, so after getting a shell, I listed the available pods:
- pod/agent
I got a shell into it: `get shell to pod/agent`<br>
After looking around, I found this binary: `/opt/agent`.<br>
Running it, the binary tells us be in to start `pod/the-container`<br>
After getting into it, in the same folder we find a new binary `/opt/the-container` but this one tells us the container needs to be in namespace **404CTF**.

- Export the container config file: `kubectl get pod the-container -o yaml > the-container.yml`
- Replace **default** by **404ctf** in namespace
- Change current namespace for **404ctf**: `kubectl config set-context ctf --user=default --namespace=404ctf --cluster=default`
- Restart `the-container` with its new configuration: `kubectl apply -f the-container.yml`

Running the binary now gives us a partial flag ```404CTF{A_la_decouv``` and tells us the last part is in `404ctf/web-server`.<br>
I copied `the-container.yml` as `web-server.yml` and changed **the-container** to **web-server** inside.<br>
I started the new container and got a shell into it: `kubectl apply -f web-server.yml`<br>
Using `ps aux`, I found the new binary: `/app/web-server`.<br>
The source code was in the same folder: `cat /app/web-server.go`, and I got the end of flag: `erte_de_k8s}`

Flag: `404CTF{A_la_decouverte_de_k8s}`