# GitHub の料金（2026年8月時点で確認）

## 前提: プランは「個人向け」と「組織向け」で別物

| プラン | 対象 | 料金 |
|---|---|---|
| **Free** | 個人・組織 | $0 |
| **Pro** | **個人アカウント** | **$4/月** |
| Team | 組織（会社・チーム） | $4/人・月 |
| Enterprise | 法人 | $21/人・月〜 |

オーナーは個人アカウントなので、**検討対象は Free と Pro の2つだけ**。
Team / Enterprise は「組織アカウント」を作らないと選べない。

## Free と Pro の差

| | Free | Pro（$4/月） |
|---|---|---|
| リポジトリ数（Private含む） | 無制限 | 無制限 |
| Actions 実行時間 | **月2,000分** | 月3,000分 |
| Public リポジトリの Actions | 無制限 | 無制限 |
| Private リポジトリから Pages を公開 | ✗ | ✓ |
| Pages サイト自体の閲覧制限 | ✗ | **✗（Proでも不可）** |
| 必須レビュー・保護ブランチ（Privateで） | ✗ | ✓ |
| Packages 保存容量 | 500MB | 2GB |

**Pro にしても Pages で公開したサイトは全世界に見える。**
閲覧制限つきの Pages は Enterprise（$21/人・月〜、組織アカウント必須）でしか作れない。

## 結論: いまの使い方なら Free で足りる

- ひとりで使う / 公開したくない業務データがある → **Pro に上げる理由がない**
- Actions は月2,000分。1日1回3分の処理で月90分なので、同規模を20個動かせる
- 超えても止まるだけ（勝手に課金されない）。追加は Linux 2コアで **1分 $0.006**

**Pro を検討する意味が出るのは**、Actions が月2,000分を超え始めたとき。
その場合も、リポジトリを Public にできるなら Actions は無制限なので、
「公開できるものは Public にする」ほうが安上がり。

## Pages のその他の上限（プラン共通）

- サイト容量: 1GB
- 通信量: 月100GB（ソフトリミット＝超えたら警告）

## 出典
- https://github.com/pricing
- https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
- https://github.blog/changelog/2021-01-21-access-control-for-github-pages/
