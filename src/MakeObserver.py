

from MyHandler import MyHandler
from watchdog.observers.polling import PollingObserver
import MyHandler

# オブザーバーの作成
class MakeObserver:

    def create(self, folderName, command):
        event_handler = MyHandler.MyHandler(command)
        observer = PollingObserver()
        observer.schedule(event_handler, path=folderName, recursive=True) # 設定

        return observer