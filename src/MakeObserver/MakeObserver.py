

from .MyHandler import *
from JsonFile import JsonFile

# オブザーバーの作成
class MakeObserver:

    def create(self, configJsonFileName: str):
        jsonObject = JsonFile().load(configJsonFileName)
        
        observer = MyHandler(jsonObject)

        return observer