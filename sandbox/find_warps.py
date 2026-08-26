import os

def find_rom():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.gb') or file.endswith('.gbc') or file.endswith('.rom'):
                print(f"Found ROM: {os.path.join(root, file)}")

find_rom()
