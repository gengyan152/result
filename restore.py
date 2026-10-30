import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
manifest = json.loads((root / "archive-manifest.json").read_text())
target = root / manifest["filename"]
if target.exists():
    raise SystemExit(f"Output already exists: {target}")
for part in manifest["parts"]:
    path = root / part["name"]
    if not path.is_file() or path.stat().st_size != part["size"]:
        raise SystemExit(f"Missing part or wrong size: {path.name}")
whole = hashlib.sha256()
with target.open("xb") as output:
    for part in manifest["parts"]:
        digest = hashlib.sha256()
        with (root / part["name"]).open("rb") as source:
            while block := source.read(8 * 1024**2):
                digest.update(block)
                whole.update(block)
                output.write(block)
        if digest.hexdigest() != part["sha256"]:
            raise SystemExit(f"Checksum mismatch: {part['name']}; output is incomplete")
        print("Verified", part["name"])
if whole.hexdigest() != manifest["sha256"]:
    raise SystemExit("Final ZIP checksum mismatch")
print("Restored and verified:", target)
