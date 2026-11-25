from rich.console import Console
from rich.panel import Panel

console = Console()

def print_report(supplier: str, product: str | None, analysis: dict, signals: dict):
    nvd = [x for x in signals.get("nvd", []) if "error" not in x]
    osv = [x for x in signals.get("osv", []) if "error" not in x]

    content = f"[bold]Supplier:[/bold] {supplier}\n"
    if product:
        content += f"[bold]Product:[/bold] {product}\n"

    content += f"[bold]Overall signal:[/bold] {analysis['level']}\n\n"

    content += "[bold]Findings: [/bold]\n"
    for item in analysis["findings"]:
        content += f"• {item}\n"

    content += "\n[bold]Source breakdown:[/bold]\n"
    content += f"• NVD : {len(nvd)} match(es)\n"
    content += f"• OSV :{len(osv)} match(es)\n"

    key_signals =[]
    for item in nvd[:3]:
        key_signals.append(f"{item.get('id')} ({item.get('severity', 'UNKNOWN')})")
    for item in osv[:2]:
        key_signals.append(item.get("id"))

    if key_signals:
        content += "\n[bold]Key signals:[/bold]\n"
        for signal in key_signals:
            content += f"• {signal}\n"

    content += (
        "\n[dim]Public sources only. Intended as a 1st pass assist. for "
        "procurement / supplier risk in Japan & APAC context. "
        " /!/ not remplace formal due diligence.[/dim]"
    )

    console.print(
        Panel(
            content,
            title="SCRS (Supply Chain Risk Signal)",
            expand= False
        )
    )