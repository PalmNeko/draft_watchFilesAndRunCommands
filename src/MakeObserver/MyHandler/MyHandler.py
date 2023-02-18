
import subprocess
from watchdog.events import FileSystemEventHandler
from watchdog.events import FileSystemEvent


class MyHandler(FileSystemEventHandler):
    def __init__(self, commands: list[str]):
        super().__init__()
        self.commands = commands
    
    def on_any_event(self, event: FileSystemEvent):
        print('イベント,event: ', event)
        for command in self.commands:
            subprocess.run(command)

        return            