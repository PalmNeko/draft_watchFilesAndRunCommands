import json

class JsonFile:
    def load(self, filename: str):
        fp = open(filename, 'r')
        parsedJsonData = json.load(fp)
        fp.close()
        return parsedJsonData
    