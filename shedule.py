from shedle_class import FileShedule
from watchdog.observers import Observer
import time

path_to_file = "result.txt"
event_handler = FileShedule(path_to_file)
observer = Observer()
observer.schedule(event_handler, path=path_to_file, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()