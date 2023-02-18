import sys
import time

from watchdog.observers import Observer
import MakeObserver.MakeObserver as MakeObserver

# メイン関数（最初に呼ばれる関数）
def main():

    checkArg()
    
    configFileName = sys.argv[1]
    
    observer = MakeObserver.MakeObserver().create(configFileName)
    startWatch(observer)
    

# コマンドライン引数チェック
def checkArg():
    if len(sys.argv) != 2:
        print("Usage: python watch.py configFileName(.json)")
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