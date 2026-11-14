import json, pathlib
m = json.loads(pathlib.Path("research_package/MANIFEST.json").read_text(encoding="utf-8"))
for e in m["files"]:
    print(f"{e['bytes']:>8}  {e['path']}")
