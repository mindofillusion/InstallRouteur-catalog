#!/usr/bin/env python3
"""Construit le catalogue candidat Windows initial.

Ce fichier est une source de travail : le résultat est candidat, non signé et
ne doit jamais être copié dans catalog/approved sans revue humaine.
"""
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

TARGETS = {
    "Bureautique": 70,
    "Création": 130,
    "Développement": 140,
    "Multimédia": 35,
    "Réseau": 70,
    "Sécurité": 50,
    "Système": 55,
    "Utilitaire": 25,
    "Jeux": 25,
}

SPECIAL_ALIASES = {
    # Une abréviation n'est admise que si elle reste suffisamment spécifique.
    # Les noms canoniques, dépourvus de numéro de version, suffisent sinon à
    # reconnaître les versions successives sans introduire de faux positifs.
    "Adobe Photoshop": "Photoshop",
    "Microsoft Flight Simulator": "Flight Simulator",
}

FORBIDDEN_ALIASES = {
    "app", "tools", "music", "drive", "cli", "nx", "dome", "vault",
    "to do", "365 apps", "remote desktop", "remote console",
    "workstation pro", "software adrenalin edition", "backupper",
}

rows = []

def add(category, subcategory, names):
    for name in names:
        rows.append((category, subcategory, name))

# Bureautique
add("Bureautique", "Suite bureautique", [
    "Microsoft 365 Apps", "LibreOffice", "Apache OpenOffice", "ONLYOFFICE Desktop Editors",
    "WPS Office", "SoftMaker Office", "FreeOffice", "OfficeSuite", "MobiOffice",
    "Hancom Office", "WordPerfect Office", "Ability Office", "SSuite Office",
    "Ashampoo Office", "Polaris Office", "Calligra Suite", "Thinkfree Office",
    "Corel WordPerfect", "Kingsoft Office", "TextMaker",
])
add("Bureautique", "PDF", [
    "Adobe Acrobat Reader", "Adobe Acrobat Pro", "Foxit PDF Reader", "Foxit PDF Editor",
    "PDF-XChange Editor", "Nitro PDF Pro", "Wondershare PDFelement", "Soda PDF",
    "PDF24 Creator", "SumatraPDF", "Okular", "STDU Viewer", "Drawboard PDF",
    "Kofax Power PDF", "Sejda PDF Desktop", "PDFsam Basic", "PDF Arranger",
    "Master PDF Editor", "MuPDF", "PDFescape Desktop",
])
add("Bureautique", "Prise de notes", [
    "Microsoft OneNote", "Obsidian", "Notion", "Evernote", "Joplin", "Standard Notes",
    "Simplenote", "Logseq", "CherryTree", "Zim Desktop Wiki", "Tomboy-ng",
    "Trilium Notes", "Anytype", "UpNote", "Boost Note", "Notezilla", "CintaNotes",
])
add("Bureautique", "Organisation", [
    "Microsoft To Do", "Todoist", "TickTick", "Trello", "Asana", "ClickUp",
    "Clockify", "Toggl Track", "RescueTime", "Freeplane", "FreeMind", "XMind",
    "MindManager", "GanttProject", "ProjectLibre", "Mindomo", "OpenProject Desktop",
])

# Création
add("Création", "Retouche d'image", [
    "Adobe Photoshop", "Adobe Lightroom Classic", "GIMP", "Krita", "Paint.NET",
    "Affinity Photo", "Corel PaintShop Pro", "DxO PhotoLab", "Capture One",
    "ON1 Photo RAW", "RawTherapee", "darktable", "Luminar Neo", "Topaz Photo AI",
    "Topaz Gigapixel AI", "ACDSee Photo Studio", "XnView MP", "FastStone Image Viewer",
    "IrfanView", "digiKam", "Adobe Bridge", "Zoner Photo Studio", "Fotor",
    "CyberLink PhotoDirector", "Pinta", "Artweaver",
])
add("Création", "Dessin et illustration", [
    "Adobe Illustrator", "Affinity Designer", "CorelDRAW", "Inkscape", "Xara Designer Pro",
    "Boxy SVG", "Synfig Studio", "OpenToonz", "Pencil2D", "Moho", "Clip Studio Paint",
    "MediBang Paint Pro", "FireAlpaca", "Paint Tool SAI", "ArtRage Vitae", "Rebelle",
    "Black Ink", "Adobe Fresco",
])
add("Création", "Publication", [
    "Adobe InDesign", "Affinity Publisher", "Scribus", "QuarkXPress", "Canva Desktop",
    "VivaDesigner", "Adobe FrameMaker", "MadCap Flare", "Microsoft Visio",
    "yEd Graph Editor", "Dia", "draw.io Desktop", "EdrawMax", "SmartDraw",
    "MiKTeX", "TeXstudio", "TeXmaker", "LyX",
])
add("Création", "Modélisation 3D", [
    "Blender", "Autodesk 3ds Max", "Autodesk Maya", "Cinema 4D", "ZBrush", "Houdini",
    "SketchUp", "Rhino 3D", "Fusion 360", "Wings 3D", "Modo", "Substance 3D Painter",
    "Substance 3D Designer", "Marvelous Designer", "Clo3D", "KeyShot", "Twinmotion",
    "Daz Studio", "Poser", "MeshLab", "Meshmixer", "FreeCAD 3D",
])
add("Création", "CAO", [
    "AutoCAD", "AutoCAD LT", "BricsCAD", "DraftSight", "FreeCAD", "LibreCAD", "QCAD",
    "nanoCAD", "progeCAD", "ZWCAD", "GstarCAD", "Archicad", "Autodesk Revit",
    "Vectorworks", "Chief Architect", "Tekla Structures", "Solid Edge", "Siemens NX",
    "Bentley MicroStation", "KiCad", "Autodesk Inventor", "SolidWorks",
])
add("Création", "Audio", [
    "Audacity", "Adobe Audition", "Avid Pro Tools", "Steinberg Cubase", "Steinberg Nuendo",
    "Ableton Live", "FL Studio", "REAPER", "PreSonus Studio One", "Bitwig Studio",
    "Cakewalk by BandLab", "LMMS", "Ardour", "Reason", "Mixcraft", "Waveform",
    "Magix Music Maker", "Sound Forge", "iZotope RX", "Ocenaudio", "Wavosaur",
    "GoldWave", "WavePad", "MuseScore", "Sibelius", "Guitar Pro", "Dorico",
])
add("Création", "Vidéo", [
    "Adobe Premiere Pro", "DaVinci Resolve", "VEGAS Pro", "Avid Media Composer", "Lightworks",
    "Shotcut", "Kdenlive", "OpenShot", "VSDC Free Video Editor", "Movavi Video Editor",
    "Wondershare Filmora", "CyberLink PowerDirector", "Corel VideoStudio", "Clipchamp",
    "HitFilm", "Camtasia", "OBS Studio", "Bandicam", "HandBrake", "FFmpeg",
    "MKVToolNix", "Avidemux", "LosslessCut", "Any Video Converter", "XMedia Recode",
])

# Développement
add("Développement", "IDE", [
    "Microsoft Visual Studio", "Visual Studio Code", "IntelliJ IDEA", "PyCharm", "WebStorm",
    "PhpStorm", "JetBrains Rider", "CLion", "GoLand", "RubyMine", "DataSpell",
    "Android Studio", "Eclipse IDE", "Apache NetBeans", "Qt Creator", "RAD Studio",
    "Delphi", "Lazarus", "Embarcadero Dev-C++", "CodeLite", "Geany", "BlueJ", "MonoDevelop",
    "Spyder", "Thonny", "RStudio", "JupyterLab Desktop", "Unity Hub", "Godot Engine",
    "GameMaker", "Construct 3", "Qt Design Studio", "PyScripter", "Code Composer Studio",
    "NI LabVIEW", "MATLAB", "Wolfram Mathematica", "Maple", "Arduino IDE", "PlatformIO",
])
add("Développement", "Éditeur de code", [
    "Notepad++", "Sublime Text", "VSCodium", "Vim", "Neovim", "GNU Emacs", "GNU Nano",
    "Bluefish", "RJ TextEd", "PSPad", "UltraEdit", "EditPlus", "Kate", "CudaText",
    "Geany Editor", "Lite XL", "SciTE", "TextPad", "WinMerge", "Meld", "Beyond Compare",
])
add("Développement", "Gestion de versions", [
    "Git for Windows", "GitHub Desktop", "GitKraken", "Sourcetree", "TortoiseGit",
    "TortoiseSVN", "SmartGit", "Fork", "Tower", "Sublime Merge", "Git Cola",
    "Git Extensions", "Mercurial", "Bazaar", "Plastic SCM", "Perforce Helix Visual Client",
    "Fossil SCM", "CVSNT", "P4V",
])
add("Développement", "Base de données", [
    "DBeaver", "HeidiSQL", "MySQL Workbench", "pgAdmin 4", "SQL Server Management Studio",
    "Oracle SQL Developer", "Toad for Oracle", "Toad for SQL Server", "Navicat Premium",
    "TablePlus", "Beekeeper Studio", "DB Browser for SQLite", "SQLiteStudio", "Valentina Studio",
    "MongoDB Compass", "Robo 3T", "Studio 3T", "Redis Insight", "FlameRobin", "DbGate",
    "SQuirreL SQL Client", "RazorSQL", "Aqua Data Studio", "DbVisualizer", "SQLyog",
])
add("Développement", "Containers et DevOps", [
    "Docker Desktop", "Podman Desktop", "Rancher Desktop", "Minikube", "kind", "Kubernetes CLI",
    "Helm", "OpenShift Local", "Vagrant", "Packer", "Terraform", "Ansible", "Pulumi",
    "GitLab Runner", "GitHub CLI", "Azure CLI", "AWS CLI", "Google Cloud CLI", "OpenTofu",
    "Multipass", "Windows Subsystem for Linux", "Cygwin", "MSYS2",
])
add("Développement", "SDK et compilation", [
    "Node.js", "Python", "OpenJDK", "Microsoft .NET SDK", "Rust", "Go", "PHP", "Ruby",
    "Perl", "R", "Julia", "Dart SDK", "Flutter SDK", "Android SDK", "CUDA Toolkit",
    "Windows SDK", "LLVM", "MinGW-w64", "CMake", "Ninja", "Meson", "Bazel", "Gradle",
    "Apache Maven", "NuGet", "Composer", "Yarn", "pnpm", "Bun", "SWI-Prolog",
])

# Multimédia
add("Multimédia", "Lecture vidéo", [
    "VLC media player", "MPC-HC", "mpv", "PotPlayer", "KMPlayer", "SMPlayer", "GOM Player",
    "Plex", "Kodi", "MPC-BE", "Zoom Player", "5KPlayer", "DivX Player", "RealPlayer",
    "JRiver Media Center", "K-Lite Codec Pack", "Stremio", "Jellyfin Media Player",
])
add("Multimédia", "Lecture audio", [
    "foobar2000", "MusicBee", "AIMP", "Winamp", "MediaMonkey", "iTunes", "Spotify",
    "Apple Music", "TIDAL", "Deezer", "Qobuz", "Roon", "Clementine", "Strawberry",
    "Dopamine", "Quod Libet", "Audirvana", "Amazon Music", "SoundCloud",
])

# Réseau
add("Réseau", "Navigateur web", [
    "Google Chrome", "Mozilla Firefox", "Microsoft Edge", "Brave", "Vivaldi", "Opera",
    "Opera GX", "Tor Browser", "Waterfox", "Pale Moon", "LibreWolf", "Chromium",
    "Ungoogled Chromium", "Maxthon", "Slimjet", "Falkon", "Floorp", "Arc Browser",
    "Sidekick", "Yandex Browser", "Avast Secure Browser", "DuckDuckGo Browser",
    "Epic Privacy Browser", "K-Meleon", "SeaMonkey",
])
add("Réseau", "Transfert et cloud", [
    "FileZilla", "WinSCP", "Cyberduck", "Core FTP", "CuteFTP", "Total Commander",
    "FreeCommander", "Double Commander", "OneCommander", "Mountain Duck", "Rclone",
    "Dropbox", "Google Drive", "Microsoft OneDrive", "pCloud Drive", "MEGAsync",
    "Sync.com", "Nextcloud Desktop", "Syncthing", "Resilio Sync", "GoodSync",
    "Air Explorer", "NetDrive", "RaiDrive", "WebDrive", "CloudMounter",
])
add("Réseau", "Accès distant", [
    "Remote Desktop Manager", "mRemoteNG", "Royal TS", "AnyDesk", "TeamViewer", "RustDesk",
    "VNC Viewer", "TightVNC", "UltraVNC", "RealVNC Server", "MobaXterm", "Termius",
    "SecureCRT", "PuTTY", "KiTTY", "DWService",
])
add("Réseau", "VPN", [
    "OpenVPN Connect", "WireGuard", "Tailscale", "ZeroTier", "NordVPN", "ExpressVPN",
    "Proton VPN", "Mullvad VPN", "Surfshark", "Private Internet Access", "CyberGhost VPN",
    "LogMeIn Hamachi", "SoftEther VPN", "FortiClient", "Cisco Secure Client",
    "GlobalProtect", "SonicWall NetExtender",
])

# Sécurité
add("Sécurité", "Antivirus", [
    "Bitdefender Total Security", "Kaspersky Standard", "ESET NOD32 Antivirus", "Norton 360",
    "McAfee Total Protection", "Avast One", "AVG Internet Security", "Avira Prime",
    "Malwarebytes", "F-Secure Internet Security", "Trend Micro Maximum Security", "Panda Dome",
    "G Data Total Security", "Webroot SecureAnywhere", "ClamWin", "HitmanPro", "AdwCleaner",
    "Spybot Search and Destroy", "RogueKiller", "Emsisoft Anti-Malware", "Dr.Web Security Space",
    "VIPRE Advanced Security", "ZoneAlarm Extreme Security", "Comodo Internet Security",
])
add("Sécurité", "Gestionnaire de mots de passe", [
    "1Password", "Bitwarden", "KeePass", "KeePassXC", "LastPass", "Dashlane", "NordPass",
    "Proton Pass", "Enpass", "RoboForm", "Sticky Password", "Password Safe", "Buttercup",
    "Password Boss", "Zoho Vault", "KeeWeb", "WinAuth", "YubiKey Manager",
])
add("Sécurité", "Confidentialité", [
    "VeraCrypt", "Cryptomator", "AxCrypt", "Gpg4win", "Kleopatra", "OpenPGP Studio",
    "BleachBit", "PrivaZer", "Eraser", "Secure Eraser", "Sandboxie Plus", "GlassWire",
    "simplewall", "Portmaster", "NetLimiter", "Wireshark", "Fiddler Classic", "Burp Suite Community",
    "OWASP ZAP",
])

# Système
add("Système", "Virtualisation", [
    "Oracle VM VirtualBox", "VMware Workstation Pro", "QEMU", "Hyper-V Manager", "Windows Sandbox",
    "Genymotion", "BlueStacks", "NoxPlayer", "LDPlayer", "MEmu", "Android Emulator",
    "MuMu Player", "VMware Horizon Client", "Microsoft Remote Desktop", "Parallels RAS Client",
    "VMware Remote Console", "VMware Tools",
])
add("Système", "Diagnostic", [
    "Sysinternals Suite", "Process Explorer", "Process Monitor", "Autoruns", "TCPView", "RAMMap",
    "GPU-Z", "CPU-Z", "HWiNFO", "Speccy", "AIDA64", "HWMonitor", "CrystalDiskInfo",
    "CrystalDiskMark", "GSmartControl", "Hard Disk Sentinel", "WinDirStat", "TreeSize",
    "WizTree", "Everything", "Microsoft PowerToys", "EarTrumpet", "DisplayFusion",
])
add("Système", "Pilotes et matériel", [
    "MSI Afterburner", "RivaTuner Statistics Server", "FanControl", "OpenRGB", "SignalRGB",
    "Corsair iCUE", "Logitech G HUB", "Razer Synapse", "SteelSeries GG", "Armoury Crate",
    "AMD Software Adrenalin Edition", "NVIDIA App", "GeForce Experience", "Intel Driver and Support Assistant",
    "Samsung Magician", "Western Digital Dashboard", "Seagate Toolkit", "Canon PRINT", "HP Smart",
    "Brother iPrint and Scan", "Epson Scan 2", "Elgato Stream Deck",
])
add("Système", "Terminal", [
    "Windows Terminal", "PowerShell 7", "ConEmu", "Cmder", "Alacritty", "WezTerm", "Tabby",
    "Windows Package Manager", "Chocolatey", "Scoop", "Ninite",
])

# Utilitaire
add("Utilitaire", "Compression", [
    "7-Zip", "WinRAR", "WinZip", "PeaZip", "Bandizip", "NanaZip", "PowerArchiver", "IZArc",
    "B1 Free Archiver", "Zipware", "ExtractNow", "Universal Extractor", "ALZip", "Ashampoo ZIP",
    "WinArchiver", "Hamstersoft ZIP Archiver", "KGB Archiver", "Easy 7-Zip",
])
add("Utilitaire", "Sauvegarde", [
    "Macrium Reflect", "AOMEI Backupper", "EaseUS Todo Backup", "Veeam Agent for Microsoft Windows",
    "Clonezilla", "Rufus", "Ventoy", "balenaEtcher", "Acronis True Image", "Paragon Backup and Recovery",
    "O and O DiskImage", "Duplicati", "Kopia", "Restic", "Uranium Backup",
])

# Jeux
add("Jeux", "Plateforme et launcher", [
    "Steam", "Epic Games Launcher", "GOG Galaxy", "EA app", "Ubisoft Connect", "Battle.net",
    "Riot Client", "Xbox app", "Playnite", "Heroic Games Launcher", "itch.io", "Amazon Games",
    "Rockstar Games Launcher", "Game Jolt Client", "GeForce NOW", "Humble App",
])
add("Jeux", "Simulation", [
    "Microsoft Flight Simulator", "X-Plane 12", "DCS World", "iRacing", "Assetto Corsa Competizione",
    "Euro Truck Simulator 2", "American Truck Simulator", "Train Sim World", "Farming Simulator",
    "Microsoft Flight Simulator 2024", "IL-2 Sturmovik", "rFactor 2", "BeamNG.drive",
])
add("Jeux", "Réalité virtuelle et émulation", [
    "Meta Quest Link", "SteamVR", "OpenXR Tools for Windows Mixed Reality", "Dolphin Emulator",
    "PCSX2", "RetroArch", "PPSSPP", "Cemu", "RPCS3", "yuzu", "Ryujinx", "Xenia",
])

def alias_for(name):
    alias = SPECIAL_ALIASES.get(name, name)
    if alias.casefold() in FORBIDDEN_ALIASES:
        raise ValueError(f"alias trop générique refusé : {name!r} -> {alias!r}")
    return alias

def main():
    by_category = defaultdict(list)
    for category, subcategory, name in rows:
        by_category[category].append({
            "canonical_name": name,
            "aliases": [alias_for(name)],
            "category": category,
            "subcategory": subcategory,
        })
    entries = []
    for category, target in TARGETS.items():
        available = by_category[category]
        if len(available) < target:
            raise SystemExit(f"{category}: {len(available)} entrées, {target} requises")
        entries.extend(available[:target])
    if len(entries) != 600:
        raise SystemExit(f"compte incorrect: {len(entries)}")
    catalog = {
        "format": "installrouteur.catalog.v1",
        "catalog_version": "0.1.0",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "entries": entries,
    }
    output = Path(__file__).parents[1] / "catalog" / "candidates" / "windows-600.json"
    output.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{output}: {len(entries)} entrées")

if __name__ == "__main__":
    main()
