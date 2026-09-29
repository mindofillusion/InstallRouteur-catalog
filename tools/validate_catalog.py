#!/usr/bin/env python3
import json
import re
import sys
from datetime import datetime

CONTROL = re.compile(r"[\x00-\x1f]")
RESERVED = re.compile(r'[<>:"|?*]')
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")

def fail(message):
    raise ValueError(message)

def safe_text(value, field):
    if not isinstance(value, str) or not (1 <= len(value) <= 256):
        fail(f"{field}: texte requis entre 1 et 256 caractères")
    if CONTROL.search(value) or RESERVED.search(value):
        fail(f"{field}: caractère de contrôle ou réservé interdit")

def norm(value):
    return " ".join(value.casefold().split())

def main(path):
    with open(path, encoding="utf-8") as source:
        catalog = json.load(source)
    if set(catalog) != {"format", "catalog_version", "generated_at", "entries"}:
        fail("champs racine invalides")
    if catalog["format"] != "installrouteur.catalog.v1":
        fail("format de catalogue invalide")
    if not isinstance(catalog["catalog_version"], str) or not SEMVER.fullmatch(catalog["catalog_version"]):
        fail("version de catalogue invalide")
    datetime.fromisoformat(catalog["generated_at"].replace("Z", "+00:00"))
    entries = catalog["entries"]
    if not isinstance(entries, list) or len(entries) > 50000:
        fail("nombre d'entrées invalide")
    names, aliases = set(), set()
    for index, entry in enumerate(entries):
        if set(entry) != {"canonical_name", "aliases", "category", "subcategory"}:
            fail(f"entrée {index}: champs invalides")
        for key in ("canonical_name", "category", "subcategory"):
            safe_text(entry[key], f"entrée {index}.{key}")
        name = norm(entry["canonical_name"])
        if name in names:
            fail(f"entrée {index}: nom canonique dupliqué")
        names.add(name)
        if not isinstance(entry["aliases"], list) or not (1 <= len(entry["aliases"]) <= 32):
            fail(f"entrée {index}.aliases: liste invalide")
        for alias in entry["aliases"]:
            safe_text(alias, f"entrée {index}.aliases")
            normalized = norm(alias)
            if normalized in aliases:
                fail(f"entrée {index}: alias dupliqué")
            aliases.add(normalized)
    print(f"OK: {len(entries)} entrée(s), format {catalog['format']}")

if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except (IndexError, OSError, ValueError, json.JSONDecodeError) as error:
        print(f"ERREUR: {error}", file=sys.stderr)
        sys.exit(1)
