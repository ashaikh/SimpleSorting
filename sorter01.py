import os
import shutil
import mimetypes

# Add support for .txt files
mimetypes.add_type("text/plain", ".txt")

# Define the source directory
src_dir = "/home/T/Downloads"

# Define the destination directories
video_dir = "/home/T/Downloads/video"
picture_dir = "/home/T/Downloads/pictures"
screen_capture_dir = "/home/T/Downloads/screencapture"
software_dir = "/home/T/Downloads/software"
txt_dir = "/home/T/Downloads/txt"
csv_dir = "/home/T/Downloads/csv"
xls_dir = "/home/T/Downloads/xls"
docs_dir = "/home/T/Downloads/docs"
pdf_dir = "/home/T/Downloads/pdf"

# Define the copy function
def move_with_overwrite(src, dst):
    shutil.copy2(src, dst)
    os.remove(src)


# Iterate over the files in the source directory
for entry in os.scandir(src_dir):
    if entry.is_file():
        # Get the full path of the file
        filepath = entry.path
        
        # Get the MIME type of the file
        mimetype, _ = mimetypes.guess_type(filepath)
        
        if mimetype:
            # Get the file type from the MIME type
            file_type, _ = mimetype.split("/")
            
            # Get the filename and extension
            filename, extension = os.path.splitext(entry.name)
            
            # Move the file to the appropriate destination directory
            if file_type == "video":
                move_with_overwrite(filepath, os.path.join(video_dir, entry.name))
            elif file_type == "image":
                if filename.startswith("screencapture"):
                    move_with_overwrite(filepath, os.path.join(screen_capture_dir, entry.name))
                else:
                    move_with_overwrite(filepath, os.path.join(picture_dir, entry.name))
            elif file_type == "application":
                if extension in (".zip", ".iso", ".exe", ".msi", ".dmg", ".deb", ".gz", ".7z", ".7zip", ".jar"):
                    move_with_overwrite(filepath, os.path.join(software_dir, entry.name))
            elif file_type == "text" and extension == ".txt":
                move_with_overwrite(filepath, os.path.join(txt_dir, entry.name))
            elif file_type == "application/pdf" and extension == ".pdf":
                move_with_overwrite(filepath, os.path.join(pdf_dir, entry.name))
            elif file_type == "text/csv" and extension == "csv":
                move_with_overwrite(filepath, os.path.join(csv_dir, entry.name))
            elif file_type == "application/vnd.ms-excel":
                if extension in (".xls", ".xlsx"):
                    move_with_overwrite(filepath, os.path.join(xls_dir, entry.name))         
            elif mimetype == "application/msword" or mimetype == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                if extension in (".doc", ".docx"):
                    move_with_overwrite(filepath, os.path.join(docs_dir, entry.name))
            else:
                print("Ignoring file:", entry.name)
            
