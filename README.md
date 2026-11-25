# keepuniq

## 概要

keepuniqは、標準入力から受け取った文章の中から重複している行を取り除き、標準出力に表示するコマンドです。

## 主な機能

- 重複した行を1つにまとめる
- 最初に出てきた行の順番を維持する
- 標準入力と標準出力を使用する

## インストール

以下のコマンドでGitHubから取得します。

```bash
git clone https://github.com/s21c1097xt-lgtm/keepuniq.git
cd keepuniq
```

## 使用方法

以下のように実行します。

```bash
printf "apple\nbanana\napple\norange\n" | ./keepuniq
```

実行結果：

```text
apple
banana
orange
```

## 動作環境

- Python 3
- UbuntuなどのLinux環境

## テスト方法

以下のコマンドでテストを実行できます。

```bash
python3 -m unittest discover -s tests -v
```

## 仕組み

入力された行を順番に確認し、すでに出現した行かどうかをsetで判定します。まだ出現していない行だけを標準出力に表示します。

## 作者

作者：原田健太郎

## ライセンス

MIT License
