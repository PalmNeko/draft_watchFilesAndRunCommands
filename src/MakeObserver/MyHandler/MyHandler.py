
import subprocess

from .FileWatcher import FileWatcher

class MyHandler(FileWatcher):
    def __init__(self, commands: list[str], globPaths: list[str]):
        super().__init__(globPaths)
        self.commands = commands
    
    def on_any(self, changeFiles: list[str]):
        print('イベント,event: ', changeFiles)
        for command in self.commands:
            subprocess.run(command)
        return