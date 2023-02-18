import sys
import time

from watchdog.observers import Observer
import MakeObserver

# メイン関数（最初に呼ばれる関数）
def main():

    checkArg()
    
    folderName = sys.argv[1]
    command = sys.argv[2]
    
    observer = MakeObserver.MakeObserver().create(folderName, command)
    startWatch(observer)
    
# コマンドライン引数チェック
def checkArg():
    if len(sys.argv) != 3:
        print("Usage: python watch.py filename command")
        sys.exit(1)

# 監視の開始 <= 監視って言ってるのにwatchを使うてどうなんや。observeじゃね
def startWatch(observer: Observer):
    
    observer.start()
    print('Stop: Ctrl+C')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# メイン関数の実行
if __name__ == "__main__":
    main()