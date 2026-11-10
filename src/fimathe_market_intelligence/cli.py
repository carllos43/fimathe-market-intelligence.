import argparse, json
from pathlib import Path
from .analyzer import analyze_market

def main():
    parser = argparse.ArgumentParser(description="Fimathe Market Intelligence OHLC analyzer")
    parser.add_argument("csv", help="CSV com colunas open,high,low,close e timestamp opcional")
    parser.add_argument("--instrument")
    parser.add_argument("--timeframe")
    args = parser.parse_args()
    import csv
    with Path(args.csv).open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    candles = [{k:(r.get(k) if k == "timestamp" else float(r[k])) for k in ("timestamp","open","high","low","close")} for r in rows]
    print(json.dumps(analyze_market(candles, args.instrument, args.timeframe), ensure_ascii=False, indent=2))

if __name__ == "__main__": main()
