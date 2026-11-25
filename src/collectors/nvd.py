import requests

def fetch_nvd(supplier: str, product: str | None = None) -> list:
    """
    Fetch public CVE signals from NVD.
    Useful even in Japan/APAC contexts because of many vendor and product vulnerabilities are globally disclosed through CVE/NVD.
    """
    query = supplier if not product else f"{supplier} {product}"

    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params = {
        "keywordSearch": query,
        "resultsPerPage": 10
    }

    try:
        response = requests.get(url, params=params, timeout=25)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        return [{"error": f"NVD request failed: {e}"}]

    results = []
    for item in data.get("vulnerabilities", []):
        cve = item.get("cve", {})
        cve_id = cve.get("id", "UNKNOWN")

        descriptions = cve.get("descriptions", [])
        summary = descriptions[0].get("value", "No description") if descriptions else "No description"

        Severity = "UNKNOWN"
        metrics = cve.get("metrics", {})

        if "cvssMetricV31" in metrics and metrics["cvssMetricV31"]:severity = metrics["cvssMetricV31"][0]["cvssData"].get("baseSeverity", "UNKNOWN")
        elif "cvssMetricV30" in metrics and metrics["cvssMetricV30"]:severity = metrics["cvssMetricV30"][0]["cvssData"].get("baseSeverity", "UNKNOWN")
        elif "cvssMetricV2" in metrics and metrics["cvssMetricV2"]:severity = metrics["cvssMetricV2"][0].get("baseSeverity", "UNKNOWN")

        results.append({
            "id": cve_id,
            "severity": severity,
            "summary": summary[:220]
        })

    return results
