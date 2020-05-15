from watchdog.events import FileSystemEventHandler
import file_manager

class CustomHandler(FileSystemEventHandler):

    # def __init__(self):
    #     pass

    def on_created(self, event):
        print('on created')
        # file_manager.read_folder()

    # def on_modified(self, event):
    #     print('on modified')

    def on_moved(self, event):
        # print('Folder has changed')
        file_manager.read_folder()

    def on_deleted(self, event):
        print('on deleted')
