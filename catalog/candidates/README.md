# Catalogue candidat

Les fichiers de ce répertoire servent à la revue éditoriale. Ils ne doivent jamais être distribués directement au client.

## Jeu initial Windows

`windows-600.json` contient exactement 600 logiciels Windows répartis entre neuf catégories et 32 sous-catégories. Les noms sont sans numéro de version ; l’alias de chaque entrée est stable afin de permettre une reconnaissance indépendante de la version quand le titre de l’installateur contient ce nom.

Le fichier est généré par `tools/build_windows_600_candidate.py`, puis contrôlé par `tools/validate_catalog.py`. Il respecte aussi les limites actuelles de nom, d’alias et de taxonomie du client Win32.

## Revue communautaire

Ce projet ne demande pas de validation directe auprès de chaque éditeur. Les contributions proviennent des utilisateurs et restent des données non fiables jusqu’à leur revue. Une entrée proposée doit pouvoir être discutée publiquement, passer le contrôle de format et de doublons, puis être acceptée par un mainteneur avant d’être reprise dans une version de travail.

Une URL publique est demandée comme contexte de revue, mais une signature de release atteste uniquement de l’intégrité d’une version publiée ; elle ne prétend pas certifier l’exactitude éditoriale de chaque classification.

## Limite importante

Le client InstallRouteur 0.4.13 n’importe pas encore de catalogue distant et sa capacité locale est limitée à 384 produits. Ce jeu de 600 entrées est donc une base éditoriale de travail, pas une mise à jour installable. La future fonction de synchronisation devra lever cette limite, vérifier la signature ECDSA P-256 et n’accepter qu’une release signée hors ligne.
