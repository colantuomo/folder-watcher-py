import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import file_manager
import settings
from CustomHandler import CustomHandler

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    # path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = CustomHandler()
    observer = Observer()
    observer.schedule(event_handler, settings.get_base_path(), recursive=True)
    observer.start()
    print('watch started.')
    file_manager.read_folder()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
