#!/usr/bin/env python3
"""配送統計マスター に 統計差分 を合流させる。

使い方: python3 merge_stats.py マスター.csv 差分1.csv [差分2.csv ...] -o 出力.csv

ルール（仕様書 ver.1.0 §6）
- キーは日付の枝番を除いた6桁。同一日付は枝番が最も後のものを採用
- 日付昇順で並べる
- 入力の BOM は自動で吸収。出力は UTF-8 BOMなし・LF
"""
import csv, sys, re

HEADER = ["日付","配送総件数","集荷総件数","古山配送件数","古山集荷件数",
          "特殊配送パターン","料金内訳(推定)","料金合計(推定)"]

def load(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))
    if not rows:
        raise SystemExit(f"{path}: 空ファイル")
    head = [c.strip() for c in rows[0]]
    if head != HEADER:
        raise SystemExit(f"{path}: ヘッダが仕様と違う\n  期待: {HEADER}\n  実際: {head}")
    out = []
    for r in rows[1:]:
        if not any(c.strip() for c in r):
            continue
        if len(r) != 8:
            raise SystemExit(f"{path}: 列数が8でない行 → {r}")
        out.append([c.strip() for c in r])
    return out

def key(date):
    m = re.fullmatch(r"(\d{6})([a-z]*)", date)
    if not m:
        raise SystemExit(f"日付の形式が不正: {date!r}（YYMMDD または YYMMDD+英小文字）")
    return m.group(1), m.group(2)

def main():
    args = sys.argv[1:]
    if "-o" not in args:
        raise SystemExit(__doc__)
    i = args.index("-o")
    inputs, dest = args[:i], args[i+1]
    if len(inputs) < 2:
        raise SystemExit(__doc__)

    best, origin = {}, {}
    for path in inputs:
        for row in load(path):
            base, suf = key(row[0])
            if base not in best or suf >= key(best[base][0])[1]:
                if base in best and suf == key(best[base][0])[1]:
                    print(f"  ⚠ 同一日付・同一枝番の重複: {row[0]}（{origin[base]} → {path} で上書き）")
                best[base], origin[base] = row, path

    rows = [best[b] for b in sorted(best)]
    with open(dest, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(HEADER); w.writerows(rows)

    print(f"\n統合完了: {len(rows)}日分 → {dest}")
    print(f"  期間: {rows[0][0]} 〜 {rows[-1][0]}")
    eda = [r for r in rows if key(r[0])[1]]
    if eda:
        print(f"  枝番採用: {', '.join(r[0] for r in eda)}")
    return rows

if __name__ == "__main__":
    main()
