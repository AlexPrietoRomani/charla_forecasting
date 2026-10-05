import httpx
import re

url = "https://app.powerbi.com/view?r=eyJrIjoiYjYwYTk5MDgtM2M0MS00NDMyLTgzNDEtMjNhNjEzYWQyOTNlIiwidCI6IjdmMDg0NjI3LTdmNDAtNDg3OS04OTE3LTk0Yjg2ZmQzNWYzZiJ9"
r = httpx.get(url, timeout=15)
print("PowerBI status:", r.status_code)
# Search for config
scripts = re.findall(r'<script[^>]*>(.*?)</script>', r.text, re.DOTALL)
for s in scripts:
    if "resolvedClusterUri" in s or "reportId" in s or "telemetry" in s:
        print("Found config script snippet:")
        print(s[:600])
