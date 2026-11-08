"""Telecharge les jars Modrinth cote serveur (side != client) dans ../server-mods/ et liste ceux de CurseForge a prendre a la main.
Usage: python tools/server_mods.py   (depuis le dossier pack)
"""
import hashlib, pathlib, tomllib, urllib.request

root = pathlib.Path(__file__).resolve().parent.parent
out = root / "server-mods"
out.mkdir(exist_ok=True)
manual = []
for f in sorted((root / "mods").glob("*.pw.toml")):
    d = tomllib.loads(f.read_text(encoding="utf-8"))
    if d.get("side") == "client":
        continue
    dl = d["download"]
    if "url" in dl:
        dest = out / d["filename"]
        data = urllib.request.urlopen(urllib.request.Request(dl["url"], headers={"User-Agent": "survie-deal-pack"})).read()
        algo = dl["hash-format"]
        assert hashlib.new(algo, data).hexdigest() == dl["hash"], f"hash KO: {d['filename']}"
        dest.write_bytes(data)
        print("ok  ", d["filename"])
    else:
        manual.append(d["name"] + "  ->  " + d["filename"])
print("\nA telecharger a la main (CurseForge, Aternos mod browser):")
print("\n".join(manual))
