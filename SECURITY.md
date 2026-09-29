# Sécurité du catalogue

Le dépôt GitHub est un canal de diffusion, pas une racine de confiance. Le client doit vérifier une signature ECDSA P-256 avec une clé publique intégrée, la version, le hachage SHA-256 et les limites de taille avant toute importation.

La clé privée de signature reste hors ligne. Aucun workflow CI, secret GitHub, site web ou serveur local ne doit y avoir accès.

Les données locales des utilisateurs ne font pas partie de ce dépôt et ne doivent jamais y être ajoutées.
