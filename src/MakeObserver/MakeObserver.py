

from .MyHandler import *
from JsonFile import JsonFile

# オブザーバーの作成
class MakeObserver:

    def create(self, configJsonFileName: str):

        jsonObject = JsonFile().load(configJsonFileName)
        
        commands = jsonObject['on']['any']
        folderName = jsonObject['folder']
        
        observer = MyHandler(commands, [folderName])

        return observer