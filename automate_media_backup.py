import os
import shutil
import gzip

def create_directory(dir_path):
    """Create directory if it doesn't exist."""
    os.makedirs(dir_path, exist_ok=True)

def is_image_file(filename):
    """Check if a file is an image based on extension."""
    image_exts = ['.jpg', '.png', '.jpeg']
    return any(filename.lower().endswith(ext) for ext in image_exts)

def is_video_file(filename):
    """Check if a file is a video based on extension."""
    video_exts = ['.mp4']
    return any(filename.lower().endswith(ext) for ext in video_exts)

def find_media_files(src_dir):
    """Find all media files in source directory, ignoring hidden folders."""
    image_files = []
    video_files = []
    
    for root, dirs, files in os.walk(src_dir):
        # Ignore hidden directories (those starting with a dot)
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if is_image_file(file):
                image_files.append(os.path.join(root, file))
            elif is_video_file(file):
                video_files.append(os.path.join(root, file))
    
    return image_files, video_files

def copy_media_files(src_dir, backup_dir, backed_up_file):
    """Copy media files from source to backup directory."""
    create_directory(backup_dir)
    image_subfolder = os.path.join(backup_dir, "images")
    video_subfolder = os.path.join(backup_dir, "videos")

    image_files, video_files = find_media_files(src_dir)

    copied_files = set()
    
    for src_file in image_files:
        dest_file = os.path.join(image_subfolder, os.path.basename(src_file))
        create_directory(os.path.dirname(dest_file))
        if not os.path.exists(dest_file):
            shutil.copy(src_file, dest_file)
            copied_files.add(src_file)
            print(f"Copied: {src_file}")

    for src_file in video_files:
        dest_file = os.path.join(video_subfolder, os.path.basename(src_file))
        create_directory(os.path.dirname(dest_file))
        if not os.path.exists(dest_file):
            shutil.copy(src_file, dest_file)
            copied_files.add(src_file)
            print(f"Copied: {src_file}")

    if copied_files:
        with open(backed_up_file, "a") as f:
            f.write("\n".join(copied_files))
            print(f"{len(copied_files)} new files backed up to {backup_dir}")
    else:
        print("No new files to copy. Everything is backed up.")

def gzip_directory(directory_path, output_gzip_file):
    """Gzip a directory and create a .gz file inside the directory."""
    with open(output_gzip_file, 'wb') as f_out, gzip.open(output_gzip_file, 'wb') as f_in:
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as file_in:
                    shutil.copyfileobj(file_in, f_out)
    
    print(f'Directory "{directory_path}" gzipped to "{output_gzip_file}"')

def main():
    src_dir = os.getcwd()  # Get the current working directory as the source directory
    backup_dir = os.path.join(src_dir, "Media Backup")  # Change the backup folder name and use os.path.join
    backed_up_file = os.path.join(backup_dir, "backedup_media.txt")
    
    copy_media_files(src_dir, backup_dir, backed_up_file)
    
    # Ask the user if they want to gzip both folders into a single 'mediabackup.gz' file or individually
    gzip_choice = input("Do you want to gzip both folders into a single 'mediabackup.gz' file? (yes/no): ").strip().lower()
    
    if gzip_choice == 'yes':
        media_backup_folder = backup_dir
        gzip_directory(media_backup_folder, os.path.join(media_backup_folder, "mediabackup.gz"))
    else:
        gzip_images = input("Do you want to gzip the 'images' folder? (yes/no): ").strip().lower()
        gzip_videos = input("Do you want to gzip the 'videos' folder? (yes/no): ").strip().lower()
        
        if gzip_images == 'yes':
            images_folder = os.path.join(backup_dir, "images")
            gzip_directory(images_folder, os.path.join(images_folder, "MediaBackup_images.gz"))
        
        if gzip_videos == 'yes':
            videos_folder = os.path.join(backup_dir, "videos")
            gzip_directory(videos_folder, os.path.join(videos_folder, "MediaBackup_videos.gz"))

if __name__ == "__main__":
    main()
