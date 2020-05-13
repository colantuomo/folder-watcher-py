import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
import file_manager
import settings

class CustomHandler(FileSystemEventHandler):
    
    def on_created(self, event):
        print('on created')
        file_manager.read_folder()

    # def on_modified(self, event):
    #     print('on modified')

    def on_moved(self, event):
        print('on moved')

    def on_deleted(self, event):
        print('on deleted')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    # path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = CustomHandler()
    observer = Observer()
    observer.schedule(event_handler, settings.BASE_PATH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
