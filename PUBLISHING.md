# Publication d’une version

1. Revoir les propositions communautaires, leurs doublons et leur compatibilité avec les alias existants. Une source publique sert de contexte ; aucune validation éditeur par éditeur n’est présumée.
2. Vérifier le catalogue avec `python3 tools/validate_catalog.py catalog/approved/catalog.json`.
3. Générer un manifeste contenant la version, le SHA-256 et l’URL de l’artefact.
4. Signer le manifeste et le catalogue avec la clé ECDSA P-256 conservée hors ligne.
5. Créer une GitHub Release avec les artefacts immuables : catalogue, manifeste et signatures.
6. Vérifier les signatures avec la clé publique indépendante avant annonce de publication.

Ne jamais ajouter la clé privée au dépôt, à un secret GitHub ou à un poste de diffusion.
