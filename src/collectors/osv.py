import requests

def fetch_osv(supplier: str, product: str | None = None) -> list:
    """
    Fetch public vuln. advisories from OSV.
    Especially relevant for open source dependancies used by vendors/products.
    """
    # v1 strategy
    # try product 1st if provided, otherwise supplier ID
    package_name= product if product else supplier

    url = "https://api.osv.dev/v1/query"
    payload = {
        "package": {
            "name": package_name,
            "ecosystem": "PyPI"  # v1 default; can be expanded later
        }
    }

    try:
        response = requests.post(url, json=payload, timeout=25)
        if response.status_code != 200:
            return[]
        data = response.json()
    except Exception:
        return []

    results = []
    for vuln in data.get("vulns", []):
        results.append({
            "id": vuln.get("id", "UNKNOWN"),
            "summary": (vuln.get("summary") or "No summary")[220]
        })

    return results

