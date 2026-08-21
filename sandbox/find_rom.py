# Let's search the ROM data for Pokemon Mansion 2F.
# The ROM image is usually named something like "pokemon_blue.gb" or "pokemon_blue.gbc" or similar.
# Let's see what files are in the parent directory or search for .gb/.gbc files.
import os
import glob

print("Current directory:", os.getcwd())
print("Files in current dir:", os.listdir("."))
print("Files in parent dir:", os.listdir(".."))
print("Files in parent parent dir:", os.listdir("../.."))
