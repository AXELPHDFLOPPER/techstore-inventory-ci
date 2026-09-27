from pathlib import Path
import re
import sys

text = Path("Dockerfile").read_text(encoding="utf-8")
issues = []

if not re.search(r"(?mi)^USER\s+\S+", text):
    issues.append("Dockerfile no declara un usuario de ejecución")

if re.search(r"(?mi)^USER\s+root\s*$", text):
    issues.append("El usuario final del contenedor es root")

if re.search(r"(?mi)^FROM\s+[^\s]+:latest\s*$", text):
    issues.append("La imagen base usa la etiqueta latest")

if issues:
    print("CONTAINER POLICY: FAILED")
    for issue in issues:
        print(" -", issue)
    sys.exit(1)

print("CONTAINER POLICY: PASSED")