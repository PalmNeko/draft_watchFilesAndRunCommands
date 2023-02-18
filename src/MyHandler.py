
import subprocess
from watchdog.events import FileSystemEventHandler
from watchdog.events import FileSystemEvent


class MyHandler(FileSystemEventHandler):
    def __init__(self, command):
        super().__init__()
        self.command = command
    
    def on_any_event(self, event: FileSystemEvent):
        print('変更有,event: ', event)
        subprocess.run(self.command)