import os

files_to_delete = [
    'notepads/Locations/RocketHideout',
    'notepads/Locations/CeladonCity',
    'notepads/Scratchpad/B2F_Spinner_Testing',
    'notepads/Scratchpad/B3F_Stairs_Testing'
]

for file_path in files_to_delete:
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"Successfully deleted {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
    else:
        print(f"File {file_path} does not exist.")
