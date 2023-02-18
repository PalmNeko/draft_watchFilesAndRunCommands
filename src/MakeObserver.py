

from MyHandler import MyHandler
from watchdog.observers.polling import PollingObserver
import MyHandler
from JsonFile import JsonFile

# オブザーバーの作成
class MakeObserver:

    def create(self, configJsonFileName: str):

        jsonObject = JsonFile.JsonFile().load(configJsonFileName)
        
        commands = jsonObject['on']['any']
        folderName = jsonObject['folder']
        
        event_handler = MyHandler.MyHandler(commands)

        observer = PollingObserver()
        observer.schedule(event_handler, path=folderName, recursive=True) # 設定

        return observer