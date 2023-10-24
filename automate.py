from time import sleep
import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir = "D:\\Downloads"
dest_dir_sfx = "D:\\Downloads\\SFX"
dest_dir_music = "D:\\Downloads\\Music"
dest_dir_video = "D:\\Downloads\\Video"
dest_dir_image = "D:\\Downloads\\Image"
dest_dir_documents = "D:\\Downloads\\Documents"
dest_text_dir_documents = "D:\\Downloads\\Text_Documents"
dest_dir_html_docs = "D:\\Downloads\\HTML_Documents"
dest_dir_database = "D:\\Downloads\\Databases"
dest_dir_ipynb = "D:\\Downloads\\Jupyter_Notebooks"
dest_dir_compressed = "D:\\Downloads\\Compressed"
dest_dir_executable = "D:\\Downloads\\Executable"

audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]

video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",".mp4", ".mp4v", ".m4v", ".avi", 
                    ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]

image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff",
                    ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic",
                    ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg",
                    ".svgz", ".ai", ".eps", ".ico", ".avif"]
                
document_extensions = [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

text_document_extensions = [".txt", ".log", ".json", ".md", ".csv", ".xml"]

html_document_extensions = [".html", ".htm"]

database_extensions = [".sql"]

ipynb_extensions = [".ipynb"]

compressed_extensions = [".7z", ".arj", ".deb", ".pkg", ".rar", ".rpm", ".tar.gz", ".z", ".zip", ".bz2", ".xz", ".tar", ".tgz"]

executable_extensions = [".apk", ".bat", ".bin", ".cgi", ".pl", ".com", ".exe", ".gadget", ".jar", ".msi", ".py", ".wsf"]

def make_unique(dest, name):
    filename, extension = os.path.splitext(name)
    counter = 1
    while os.path.exists(os.path.join(dest, name)):
        name = f"{filename} ({counter}){extension}"
        counter += 1
    return name

def move_file(dest, entry, name):
    try:
        if not os.path.exists(dest):
            os.makedirs(dest)

        if not os.path.exists(os.path.join(dest, name)):
            shutil.move(entry.path, os.path.join(dest, name))

        else:
            unique_name = make_unique(dest, name)
            shutil.move(entry.path, os.path.join(dest, unique_name))
    except Exception as e:
        logging.error(f'move() -> destination {dest}; entry {entry}; name {name}')
        logging.error(f'Exception throwed: {e}')

class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_files(entry, name)
                self.check_text_document_files(entry, name)
                self.check_html_document_files(entry, name)
                self.check_database_files(entry, name)
                self.check_ipynb_files(entry, name)
                self.check_compressed_files(entry, name)
                self.check_executable_files(entry, name)

    def check_audio_files(self, entry, name):  
        for audio_extension in audio_extensions:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                if entry.stat().st_size < 10_000_000 or "SFX" in name:  
                    dest = dest_dir_sfx
                else:
                    dest = dest_dir_music
                move_file(dest, entry, name)
                logging.info(f"Moved audio file: {name}")

    def check_video_files(self, entry, name):  
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move_file(dest_dir_video, entry, name)
                logging.info(f"Moved video file: {name}")

    def check_image_files(self, entry, name): 
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move_file(dest_dir_image, entry, name)
                logging.info(f"Moved image file: {name}")

    def check_document_files(self, entry, name):
        for documents_extension in document_extensions:
            if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
                move_file(dest_dir_documents, entry, name)
                logging.info(f"Moved document file: {name}")

    def check_text_document_files(self, entry, name):
        for text_documents_extension in text_document_extensions:
            if name.endswith(text_documents_extension) or name.endswith(text_documents_extension.upper()):
                move_file(dest_text_dir_documents, entry, name)
                logging.info(f"Moved text document file: {name}")

    def check_html_document_files(self, entry, name):
        for html_document_extension in html_document_extensions:
            if name.endswith(html_document_extension) or name.endswith(html_document_extension.upper()):
                move_file(dest_dir_html_docs, entry, name)
                logging.info(f"Moved html document file: {name}")
    
    def check_database_files(self, entry, name):
        for database_extension in database_extensions:
            if name.endswith(database_extension) or name.endswith(database_extension.upper()):
                move_file(dest_dir_database, entry, name)
                logging.info(f"Moved database file: {name}")
    
    def check_ipynb_files(self, entry, name):
        for ipynb_extension in ipynb_extensions:
            if name.endswith(ipynb_extension) or name.endswith(ipynb_extension.upper()):
                move_file(dest_dir_ipynb, entry, name)
                logging.info(f"Moved ipynb file: {name}")
    
    def check_compressed_files(self, entry, name):
        for compressed_extension in compressed_extensions:
            if name.endswith(compressed_extension) or name.endswith(compressed_extension.upper()):
                move_file(dest_dir_compressed, entry, name)
                logging.info(f"Moved compressed file: {name}")

    def check_executable_files(self, entry, name):
        for executable_extension in executable_extensions:
            if name.endswith(executable_extension) or name.endswith(executable_extension.upper()):
                move_file(dest_dir_executable, entry, name)
                logging.info(f"Moved executable file: {name}")


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