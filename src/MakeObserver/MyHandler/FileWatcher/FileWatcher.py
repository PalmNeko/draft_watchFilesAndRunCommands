import os
import glob

class FileWatcher():

    def __init__(self, globPaths: list[str]):
        self.globPaths = globPaths
        # 監視するフォルダ内のファイルとフォルダの辞書を作成
        self.before = dict([(f, None) for f in self.targetPaths()])
        print ('target file count on start:', len(self.before))
        for f in self.before:
            self.before[f] = os.stat(f).st_mtime
    
    # 対象のファイル・フォルダのパスを返す。
    def targetPaths(self):
        returnPaths = []
        for globPath in self.globPaths:
            for path in glob.glob(globPath, recursive=True):
                if os.path.isfile(path):
                    returnPaths.append(path)
                for dirpath, dirs, files in os.walk(path):
                    for dir in dirs:
                        returnPaths.append(os.path.join(dirpath, dir))
                    for file in files:
                        returnPaths.append(os.path.join(dirpath, file))
        return returnPaths
    
    # watch
    def watch(self):
        after = dict([(f, None) for f in self.targetPaths()])
        for f in after:
            if os.path.exists(f):
                after[f] = os.stat(f).st_mtime

        added = [f for f in after if f not in self.before]
        removed = [f for f in self.before if f not in after]
        modified = []
        for f in self.before:
            if f in after and after[f] != self.before[f]:
                modified.append(f)
        
        if added or removed or modified:
            self.on_any(added + removed + modified)
            if added:
                self.on_created(added)
            if removed:
                self.on_deleted(removed)
            if modified:
                self.on_modified(modified)
        
        for f in after:
            after[f] = os.stat(f).st_mtime
        self.before = after
        return

    # 変更
    def on_any(self, changeFiles: list[str]):
        print("変更がありました", ", ".join(changeFiles))
        return None
    
    # 作成時
    def on_created(self, addFiles: list[str]):
        print("新しいファイルが追加されました:", ", ".join(addFiles))
        return None
    
    # 削除時
    def on_deleted(self, removedFiles: list[str]):
        print("ファイルが削除されました:", ", ".join(removedFiles))
        return None

    # ファイル変更時
    def on_modified(self, modifiedFiles: list[str]):
        print("ファイルが変更されました:", ", ".join(modifiedFiles))
        return None
    