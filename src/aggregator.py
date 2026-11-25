from src.collectors.nvd import fetch_nvd
from src.collectors.osv import fetch_osv

def collect_all_signals(supplier: str, product: str | None = None) -> dict:
    """
    Aggregate public cyber suppliers signals from multiple sources.
    """
    nvd_results = fetch_nvd(supplier, product)
    osv_results = fetch_osv(supplier, product)

    return {
        "nvd": nvd_results,
        "osv": osv_results
    }

