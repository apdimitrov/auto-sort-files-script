import os
import shutil

image_formats = ["jpg", "png", "jpeg", "gif", "webp", "tiff"]
audio_formats = ["mp3", "wav"]
video_formats = ["mp4", "avi", "webm"]
docs_formats = ["txt", "ppt", "docx", "pdf", "odt"]

files = os.listdir("./")
current_directory = os.getcwd()

if not os.path.exists(current_directory + "/" + "images"):
    os.mkdir("images")
if not os.path.exists(current_directory + "/" + "audio"):
    os.mkdir("audio")
if not os.path.exists(current_directory + "/" + "video"):
    os.mkdir("video")
if not os.path.exists(current_directory + "/" + "docs"):
    os.mkdir("docs")
if not os.path.exists(current_directory + "/" + "others"):
    os.mkdir("others")


print("Auto-Sort Files Script has been started..")

while True:
    for file in files:
        if os.path.isfile(file) and file != "auto_sort_files_script.py":
            ext = (file.split(".")[-1]).lower()

            if ext in image_formats:
                shutil.move(file, "images/" + file)
            elif ext in audio_formats:
                shutil.move(file, "audio/" + file)
            elif ext in video_formats:
                shutil.move(file, "video/" + file)
            elif ext in docs_formats:
                shutil.move(file, "docs/" + file)
            else:
                shutil.move(file, "others/" + file)
