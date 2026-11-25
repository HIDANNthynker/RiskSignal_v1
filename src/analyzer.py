def analyze(signals: dict) -> dict:
    """
    Simple first-pass scoring for procurement / supplier risk usage.
    """
    nvd = [x for x in signals.get("nvd", []) if "error" not in x]
    osv = [x for x in signals.get("osv", []) if "error" not in x]

    findings = []
    score = 0

    if nvd:
        score += min(len(nvd), 5)
        findings.append(f"{len(nvd)} public CVE signals found in NVD")

        high_or_critical = [
            x for x in nvd
            if str(x.get("severity", "")).upper() in ["HIGH", "CRITICAL"]
        ]
        if high_or_critical:
            score += 2
            findings.append(
                f"{len(high_or_critical)} high/critical severity CVE signals"
            )

    if osv:
        score += min(len(osv), 3)
        findings.append(f"{len(osv)} public advisory signals found in OSV")

    if not nvd and not osv:
        findings.append("No significant public cyber signals found in current sources")

    if score >= 7:
        level = "HIGH"
    elif score >= 3:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "level": level,
        "score": score,
        "findings": findings
    }