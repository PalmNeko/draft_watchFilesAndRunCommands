
import subprocess

from .FileWatcher import FileWatcher

class MyHandler(FileWatcher):
    def __init__(self, configs: dict):
        super().__init__(configs['folder'])
        self.configs = configs
    
    def on_any(self, changeFiles: list[str]):
        print('いずれかの変更がありました。: ', changeFiles)
        if not (
                'on' in self.configs and
                'any' in self.configs['on']
            ):
            return
        for command in self.configs['on']['any']:
            subprocess.run(command)
        return

    def on_created(self, changeFiles: list[str]):
        print('ファイルが作成されました。: ', changeFiles)
        if not (
                'on' in self.configs and
                'created' in self.configs['on']
            ):
            return
        for command in self.configs['on']['created']:
            subprocess.run(command)
        return