import os
from pydub import AudioSegment

from pydub import AudioSegment

def get_mp3_duration(file_path):
    print(f"Attempting to get duration for: {file_path}")

    try:
        audio = AudioSegment.from_mp3(file_path)
        duration = len(audio) / (1000 * 60)  # Convert milliseconds to minutes
        print(f"Success! Duration: {duration:.2f} minutes")
        return duration
    except Exception as e:
        print(f"Error: {e}")
        return 0


def browse_folder(folder_path):
    print(f"Entered folder path: {folder_path}")

    total_duration = 0
    files_list = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".mp3"):
                file_path = os.path.join(root, file)
                duration = get_mp3_duration(file_path)
                total_duration += duration
                files_list.append((file_path, duration))

    return files_list, total_duration


def main():
    folder_path = input("Enter the folder path: ")

    if not os.path.exists(folder_path):
        print("Folder not found.")
        return

    files_list, total_duration = browse_folder(folder_path)

    print("\nList of MP3 files with duration:")
    for file_path, duration in files_list:
        print(f"{file_path}: {duration:.2f} minutes")

    total_hours = int(total_duration // 60)
    total_minutes = total_duration % 60

    print(f"\nTotal Duration: {total_hours} hours and {total_minutes:.2f} minutes")

if __name__ == "__main__":
    main()
