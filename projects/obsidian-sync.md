# Obsidian（iCloud）→ Google Drive 自動同期

> Mac の iCloud にある Obsidian のメモのうち、Markdown だけを Google Drive に5分ごとに同期する。Google Drive 側を AI から読めるようにするのが目的。

- 同期元にファイルが無いとき（iCloud が未ダウンロードなど）は、Drive 側を消さないよう安全に止まる
- 技術：シェルスクリプト、rsync、macOS の launchd
