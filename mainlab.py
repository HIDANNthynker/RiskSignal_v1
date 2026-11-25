import argparse
from src.aggregator import collect_all_signals
from src.analyzer import analyze
from src.reporter import print_report

def main():
    parser = argparse.ArgumentParser(
        description="Public cyber supplies risk signals for procurement / supplier risk (Japan & APAC focus)"
    )

    parser.add_argument("--supplier", required=True, help="Supplier or vendor ID")
    parser.add_argument("--product", required=False, help="Optional product / component occur")
    args = parser.parse_args()

    print(f"\n[*] Collecting public signals for: {args.supplier}")
    if args.product:
        print(f"[*] Product focus: {args.product}")
    print("[*] Scope: public sources only --> Intended use: procurement / supplier risk 1st-pass\n")

    signals = collect_all_signals(args.supplier, args.product)
    analysis = analyze(signals)

    #print("DEBUG signals =", signals)
   # print("DEBUG analysis =", analysis)

    print_report(args.supplier, args.product, analysis, signals)

if __name__ == "__main__":
    main()