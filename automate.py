import os
from os.path import join
from time import sleep

import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir = 'C:\\Users\\Ash\\Downloads'

with os.scandir(source_dir) as entries:
    for entry in entries:
        print(entry.name)

class MoverHandler(FileSystemEventHandler){
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_files(entry, name)
                self.check_compressed_files(entry, name)
                self.check_executable_files(entry, name)
}

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()