"""Genere Survie-Deal.zip, instance Prism Launcher prete a importer.
Usage: python tools/make_instance.py <URL_pack.toml> <adresse.aternos.me>
L'instance lance packwiz-installer avant chaque demarrage: mods toujours a jour.
"""
import json, struct, sys, urllib.request, zipfile

pack_url, server_ip = sys.argv[1], sys.argv[2]
BOOT = "https://github.com/packwiz/packwiz-installer-bootstrap/releases/download/v0.0.3/packwiz-installer-bootstrap.jar"
MC, NEO = "1.21.1", "21.1.265"  # garder identique a pack.toml

cfg = f"""[General]
ConfigVersion=1.2
InstanceType=OneSix
name=Survie Deal
OverrideCommands=true
PreLaunchCommand="$INST_JAVA" -jar packwiz-installer-bootstrap.jar {pack_url}
OverrideMemory=true
MinMemAlloc=2048
MaxMemAlloc=6144
"""
mmc = {
    "components": [
        {"cachedName": "Minecraft", "cachedVersion": MC, "important": True, "uid": "net.minecraft", "version": MC},
        {"cachedName": "NeoForge", "cachedRequires": [{"equals": MC, "uid": "net.minecraft"}],
         "cachedVersion": NEO, "uid": "net.neoforged", "version": NEO},
    ],
    "formatVersion": 1,
}

def s(x):  # NBT string payload
    b = x.encode(); return struct.pack(">H", len(b)) + b

def tag(t, name, payload):  # named tag
    return bytes([t]) + s(name) + payload

entry = tag(8, "ip", s(server_ip)) + tag(8, "name", s("Survie Deal")) + b"\x00"
servers_dat = tag(10, "", tag(9, "servers", bytes([10]) + struct.pack(">i", 1) + entry) + b"\x00")

# FA Player Extension actif d'office (requis par Touch'n Motion); le pack citrouille reste a activer a la main.
options = 'resourcePacks:["vanilla","file/FA+Player-v1.1.zip"]\n'

boot = urllib.request.urlopen(urllib.request.Request(BOOT, headers={"User-Agent": "survie-deal"})).read()
with zipfile.ZipFile("Survie-Deal.zip", "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("instance.cfg", cfg)
    z.writestr("mmc-pack.json", json.dumps(mmc, indent=2))
    z.writestr("minecraft/servers.dat", servers_dat)
    z.writestr("minecraft/options.txt", options)
    z.writestr("minecraft/packwiz-installer-bootstrap.jar", boot)
print("Survie-Deal.zip cree")
