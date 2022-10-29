from watchdog.events import FileSystemEventHandler
from datetime import datetime
import os

class FileShedule(FileSystemEventHandler):
    
    def __init__(self, file_path : str):
        self.file_path = file_path
    
    def on_any_event(self, event):
        pass
    
    def on_created(self, event):
        pass
    
    def on_deleted(self, event):
        pass
    
    def on_modified(self, event):
        last_line = str()
        mod_list = []
        with open(self.file_path, 'rb') as file:
            try:
                file.seek(-2, os.SEEK_END)
                while file.read(1) != b'\n':
                    file.seek(-2, os.SEEK_CUR)
            except OSError:
                file.seek(0)
            last_line = file.readline().decode().split(' ')
        print(f"{datetime.now()} {last_line[0]}")