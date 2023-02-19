# draft_watchFilesAndRunCommands
# 概要
設定内容に基づいてフォルダおよびファイルの監視し、変更があれば設定したコマンドを実行する。

# 背景・目的
ビルドなどにwatch機能があるが、うまく動かないことがあった。ファイルを監視して、コマンドを実行をしてくれるプログラムがあれば楽だと思った。

# 機能
* ファイル・フォルダの監視
* ファイルの削除、作成、変更時にコマンドを実行する。

# 使い始める
1. リポジトリのクローン
1. pyinstallerライブラリのインストール。`pip install pyinstaller`
1. exe化 `pyinstaller --onefile src/main.py`
1. 設定ファイルの作成 jsonSchemas参照
1. [作成したexeファイル] [作成した設定ファイル]

# 想定する使い方
##### ディレクトリ構成 (ディレクトリの中身は表示していない)
> /
>> setting-watch.json <br>
>> scripts/ <br>
>> src/

##### 設定ファイル

`setting-watch.json`
```json
{
    "folder": "./src",
    "on": {
        "modified": [
            "echo start: modified Process",
            "bash ./scripts/exaple_build.sh",
            "bash ./scripts/exaple_test.sh",
            "bash ./scripts/exaple_build.sh --prod",
            "bash ./scripts/example_deploy.sh",
            "echo end"
        ]
    }
}
```
##### 動作
`src/`内のファイルもしくはフォルダが保存されたときに、コマンドを複数実行します。ただし、エラーがあっても後続のコマンドを中止などはしません。
