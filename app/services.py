import requests
from cache import cache

OSV_API_URL = "https://api.osv.dev/v1/query"
def fetch_vulnerabilities(package_name: str, version: str):
    cache_key = f"{package_name}@{version}"
    if cache_key in cache:
        return cache[cache_key]
    
    payload = {"package": {"name": package_name, "ecosystem": "PyPI"}, "version": version}
    response = requests.post(OSV_API_URL, json=payload)
    if response.status_code == 200:
        vulnerabilities = response.json().get("vulns", [])
        cache[cache_key] = vulnerabilities
        return vulnerabilities
    
    return []
