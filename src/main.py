import sys
import time
import os

from MakeObserver import MakeObserver
from MakeObserver import MyHandler

# メイン関数（最初に呼ばれる関数）
def main():

    checkArg()
    
    configFileName = sys.argv[1]
    if os.path.isfile(configFileName) == True:
        os.chdir(os.path.abspath(os.path.dirname(configFileName)))
    else:
        print('設定ファイルが見つかりませんでした。終了します。')
        return None
    observer = MakeObserver().create(os.path.basename(configFileName))
    startWatch(observer)
    
    return None

# コマンドライン引数チェック
def checkArg():
    if len(sys.argv) != 2:
        print("Usage: python watch.py configFileName(.json)")
        sys.exit(1)

# 監視の開始 <= 監視って言ってるのにwatchを使うてどうなんや。observeじゃね
def startWatch(observer: MyHandler):
    
    print('Stop: Ctrl+C')
    try:
        while True:
            time.sleep(1)
            observer.watch()
    except KeyboardInterrupt:
        pass
    return None
# メイン関数の実行
if __name__ == "__main__":
    main()