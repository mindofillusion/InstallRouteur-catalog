# InstallRouteur-catalog

Référentiel public des classifications de logiciels pour InstallRouteur.

Ce dépôt ne contient ni règle personnelle, ni journal, ni clé de signature. Les entrées dans `catalog/candidates` sont des propositions de travail. Seules les versions publiées, validées et signées hors ligne pourront être consommées par le client.

## Flux de publication

1. une proposition est soumise dans le dépôt principal ;
2. elle est revue et ajoutée au catalogue candidat ;
3. les validations de structure, de limites et de doublons sont exécutées ;
4. une version approuvée est préparée ;
5. le fichier et son manifeste sont signés hors ligne ;
6. les artefacts immuables sont publiés dans une GitHub Release.

GitHub Actions peut valider le contenu, mais ne signe rien. La clé privée ne doit jamais être stockée dans GitHub, dans un secret GitHub, ni sur un serveur de diffusion.

## État initial

`catalog/approved/catalog.json` est volontairement vide et marqué comme brouillon non signé. Il ne doit pas être référencé par un client de production.
