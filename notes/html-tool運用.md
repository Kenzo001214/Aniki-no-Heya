# 自作HTMLツールの置き場所（tiiny.host からの移行）

対象: 「当日張り込みカルテ」のような、**CSV → Python → HTML1ファイル** で作るツール。

## まず整理: ホスティングは「配布」しかしていない

生成されたHTMLは**完全に自己完結**（外部通信ゼロ・データ埋め込み済み）。
つまりファイルさえ iPhone にあれば動く。
tiiny.host が解決していたのは「**どうやって iPhone にファイルを届けるか**」だけ。
→ 月額を払う価値があるかは、この一点だけで判断してよい。

## 重要な前提: GitHub は HTML を「表示」してくれない

`raw.githubusercontent.com` は HTML を **text/plain（ただの文字）** として返す。
Private / Public を問わず、ブラウザで開いてもソースが見えるだけで動かない。
**HTMLを動く形で配信する機能は GitHub Pages だけ**で、それは常に全世界公開。
→ 業務データ入りのこのツールは Pages に置けない（`git-github.md` 参照）。

## 推奨: Private リポジトリ + Actions + ダウンロードして開く

1. Private リポジトリに **Python スクリプトと CSV** を置く
2. GitHub Actions で生成（`workflow_dispatch` = ボタン手動実行でよい）
3. 生成された HTML を**リポジトリにコミットさせる**
4. iPhone の Safari で GitHub を開き、そのファイルの
   **「Download raw file」**（ダウンロードアイコン）をタップ
5. Safari の**ダウンロード一覧（↓）からタップして開く**と JavaScript ごと動く

- 費用ゼロ / データは Private のまま外に出ない
- 過去バージョンが全部コミット履歴に残る（tiiny.host にはない利点）
- 注意: ファイルアプリのプレビューだと動かないことがある。Safari のダウンロード一覧か
  **Documents（Readdle社・無料）**アプリから開く

## 代替: Pyto でその場生成

Python が iPhone 内（Pyto）で完結するなら、**転送すら不要**。
生成 → ファイルアプリに保存 → 開く、で終わり。ネットも要らない。
CSV を手で書き集めている運用なら、こちらのほうが手数が少ないこともある。

## Actions のアーティファクトは使わない

Actions の「artifact」機能でも受け取れるが、**zip で降ってくる**ので
iPhone で解凍する手間が増える（ファイルアプリで長押し→展開）。
リポジトリに直接コミットさせるほうが早い。
