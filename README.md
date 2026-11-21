# ポートフォリオ

生活や研究の「面倒」を、小さな自動化とデータ分析で解決してきた記録です。
各プロジェクトの「何を解決したか」「どう作ったか」「結果」をまとめています。

## プロジェクト

| プロジェクト | 一言で | 使った技術 |
|---|---|---|
| [Gmail 自動振り分け](projects/gmail-sorter.md) | 受信箱を「既読・残す・迷惑メール」に自動で片付け、使うほど送信元を覚える | Google Apps Script、判断特化 AI（Jev）、ナイーブベイズ、GitHub Actions |
| [CSV 初期分析の自動化](projects/csv-analysis.md) | CSV と課題を渡すと、前処理からベースラインモデルまで日本語レポートにまとめる | Python、pandas、LightGBM、Claude Code のスキル |
| [PubMed 論文探索ノートブック](projects/pubmed-notebook.md) | 検索式の一覧から論文を一括収集し、ヒット数と重複を整理する | Python、Google Colab、NCBI E-utilities |
| [Yahoo!メール 自動振り分け](projects/yahoo-mail.md) | 件名と差出人でフォルダに振り分ける | Python、IMAP |
| [Obsidian → Google Drive 自動同期](projects/obsidian-sync.md) | iCloud のメモを Google Drive に5分ごとに同期し、AI から読めるようにする | シェル、rsync、launchd |
| [Windows 自動ロックタイマー](projects/pc-auto-locker.md) | 指定時刻に画面をロックして作業の区切りを作る | HTA、JavaScript |

## コードも公開しているもの

| フォルダ | 内容 |
|---|---|
| [projects/kaggle-signate](projects/kaggle-signate/README.md) | Kaggle・SIGNATE のコンペの解法と実験記録（例: Jリーグ観客動員数予測） |
| [projects/atcoder](projects/atcoder/README.md) | AtCoder の解答（Python） |

## 作り方の共通点

- **費用を抑える**：ルールで決まるものはルールで決め、AI は迷ったものだけに使う
- **自分のデータを外に出さない**：できるだけ自分の Google アカウントや PC の中で動かす
- **使う人が迷わない**：設定はスプレッドシートやメニューから変えられるようにし、コードを触らなくてよい形にする

## 著作権

このリポジトリの文章・図の著作権は作者にあります。無断での転載・再配布はご遠慮ください。
