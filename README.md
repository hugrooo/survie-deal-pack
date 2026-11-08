# Survie Deal (NeoForge 1.21.1)

Contenu du dossier
- `pack.toml`, `index.toml`, `mods/`, `resourcepacks/` : pack packwiz (a heberger sur Internet, voir etape 1).
- `server-mods/` : jars a envoyer sur Aternos (10 jars Modrinth, hash verifies). Absent du depot, a regenerer avec `python tools/server_mods.py`.
- `tools/make_instance.py` : fabrique `Survie-Deal.zip`, l'instance Prism a donner aux amis.
- `tools/server_mods.py` : retelecharge `server-mods/` apres un changement de mods.

## 1. Heberger le pack (une fois)
Mettre ce dossier (sans `server-mods/`) dans un depot GitHub public, puis l'URL du pack est
`https://raw.githubusercontent.com/<user>/<repo>/main/pack.toml`.

## 2. Serveur Aternos
1. Serveur Aternos: Software = NeoForge, version 1.21.1.
2. Onglet Mods: envoyer tous les jars de `server-mods/`.
3. Chercher dans le navigateur de mods Aternos (ou envoyer le jar depuis CurseForge): **Cinematic Interactions** (NeoForge 1.21.1) et **FAUNA Engine** (NeoForge 1.21.1).
4. Activer la whitelist Aternos (Joueurs > Whitelist) et ajouter ta copine et toi en operateurs. Les amis ne sont ajoutes qu'a leur arrivee.
5. Demarrer, lire la RAM affichee: Aternos ne permet pas d'en ajouter (environ 2,5 Go d'apres des posts de la communaute, non officiel). Si le serveur plante par manque de memoire, retirer d'abord The Sift, le plus lourd, puis Book of Dragons.

## 3. Instance pour les amis
```
python tools/make_instance.py <URL_pack.toml> <ton-serveur>.aternos.me
```
Donner `Survie-Deal.zip` + le lien de Prism Launcher (prismlauncher.org). L'ami: Prism, Ajouter une instance, Importer, choisir le zip, Jouer. A chaque lancement, packwiz met les mods a jour tout seul. Il faut un compte Minecraft Java.

Premiere ouverture: Options > Packs de ressources, activer aussi `Spectral Pumpkin Tools` (marque incompatible car fait pour 1.20.2).

## 4. Protection de la base (apres le premier demarrage)
- Claims: Open Parties and Claims. Tu crees un party pour ta copine et toi, puis tu claim des chunks depuis la carte Xaero. Les commandes exactes sont sur la page Modrinth du mod (je ne les ai pas verifiees).
- Anti-grief: GriefLogger enregistre tout, GLRA ajoute la commande et l'interface web de rollback. Voir leurs pages Modrinth pour les commandes.
- Alertes: Claim Intrusion Alert previent le proprietaire d'un claim des tentatives.
- Roles: LuckPerms. `/lp creategroup ami` puis `/lp user <pseudo> parent add ami`. Seul, il gere les droits de commandes, la hierarchie dans la base vient des rangs de party d'OPAC.

## Points non verifies
- Rien n'a ete lance: ni client, ni serveur Aternos. Premier demarrage = test.
- Le comportement exact des claims OPAC (coffres, redstone, explosions) est a regler dans sa config apres le premier demarrage.
- Mods CurseForge (Cinematic Interactions, Touch'n Motion, Weather Glass, FAUNA Engine, EMF Compat): si un auteur interdit le telechargement tiers, packwiz-installer demande un telechargement manuel au premier lancement.
- La version de NeoForge sur Aternos peut differer de 21.1.265; si le client refuse de se connecter, mettre la meme version dans `pack.toml` et `tools/make_instance.py`.
