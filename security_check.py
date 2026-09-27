from pathlib import Path
import re
import sys

text = Path("app.py").read_text(encoding="utf-8")
issues = []

if re.search(r'DB_PASSWORD\s*=\s*["\']', text):
    issues.append("Se detectó una credencial escrita directamente en app.py")

if re.search(r'debug\s*=\s*True', text):
    issues.append("La aplicación ejecuta debug=True")

if issues:
    print("SECURITY CHECK: FAILED")
    for issue in issues:
        print(" -", issue)
    sys.exit(1)

print("SECURITY CHECK: PASSED")