""" File Organizer Script Author: Akshit Description: Automatically sorts files in a folder into subfolders based on file type. Built as a freelance automation tool. """
import os
import shutil

# ---- CONFIGURATION ----
# Map of extensions to folder names
EXTENSION_MAP = {
    # Documents
    '.pdf': 'Documents',
    '.docx': 'Documents',
    '.doc': 'Documents',
    '.txt': 'Documents',
    '.xlsx': 'Documents',
    '.pptx': 'Documents',
    # Images
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.svg': 'Images',
    '.webp': 'Images',
    # Music
    '.mp3': 'Music',
    '.wav': 'Music',
    '.flac': 'Music',
    # Videos
    '.mp4': 'Videos',
    '.mov': 'Videos',
    '.avi': 'Videos',
    '.mkv': 'Videos',
    # Archives
    '.zip': 'Archives',
    '.rar': 'Archives',
    '.7z': 'Archives',
    # Code
    '.py': 'Code',
    '.js': 'Code',
    '.html': 'Code',
    '.css': 'Code',
    '.c': 'Code',
    '.cpp': 'Code',
}

def organize_folder(folder_path):
    """Main function — takes a folder path and organizes it."""

    # Check if the folder actually exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    print(f"\nOrganizing: {folder_path}")
    print("-" * 40)

    moved_count = 0
    skipped_count = 0

    # Loop through every item in the folder
    for filename in os.listdir(folder_path):

        # Build the full file path
        file_path = os.path.join(folder_path, filename)

        # Skip if it's a folder (we only move files)
        if os.path.isdir(file_path):
            skipped_count += 1
            continue

        # Get the file extension in lowercase (.PDF → .pdf)
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # Decide which subfolder it goes into
        subfolder = EXTENSION_MAP.get(ext, 'Others')

        # Create that subfolder if it doesn't exist
        dest_folder = os.path.join(folder_path, subfolder)
        os.makedirs(dest_folder, exist_ok=True)

        # Move the file
        dest_path = os.path.join(dest_folder, filename)
        shutil.move(file_path, dest_path)

        print(f" Moved: {filename} → {subfolder}/")
        moved_count += 1

    print(f"\nDone! Moved {moved_count} files. Skipped {skipped_count} folders.")

# ---- RUN THE SCRIPT ----
if __name__ == "__main__":
    print("=== File Organizer v1.0 ===")
    folder = input("Enter folder path to organize: ")
    organize_folder(folder.strip())