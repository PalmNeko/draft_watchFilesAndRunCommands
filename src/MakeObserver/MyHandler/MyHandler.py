
import subprocess

from .FileWatcher import FileWatcher

class MyHandler(FileWatcher):
    def __init__(self, configs: dict):
        super().__init__(configs['folder'])
        self.configs = configs
    
    def on_any(self, changeFiles: list[str]):
        print('イベント,event: ', changeFiles)
        for command in self.configs['on']['any']:
            subprocess.run(command)
        return