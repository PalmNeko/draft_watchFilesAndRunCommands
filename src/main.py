import sys
import time

from watchdog.observers import Observer
import MyHandler

# メイン関数（最初に呼ばれる関数）
def main():

    checkArg()
    
    folderName = sys.argv[1]
    command = sys.argv[2]

    startWatch(folderName, command)
    
# コマンドライン引数チェック
def checkArg():
    if len(sys.argv) != 3:
        print("Usage: python watch.py filename command")
        sys.exit(1)

# 監視の開始 <= 監視って言ってるのにwatchを使うてどうなんや。observeじゃね
def startWatch(folderName, command):
    event_handler = MyHandler.MyHandler(command)
    observer = Observer()
    observer.schedule(event_handler, path=folderName, recursive=True) # 設定
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