import os

def find_files(suffix, path="."):
    results = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith(suffix):
                results.append(os.path.join(root, f))
    return results

print("Looking for ROM files (.gb, .gbc):")
roms = find_files(".gb") + find_files(".gbc")
for r in roms:
    print("Found ROM:", r)

# Look in parent directories as well
print("\nLooking in parent directory:")
roms_parent = find_files(".gb", "..") + find_files(".gbc", "..")
for r in roms_parent:
    print("Found ROM in parent:", r)

print("\nListing all files in saveDir/sandbox/notepads/ :")
for root, dirs, files in os.walk("notepads"):
    for f in files:
        print(os.path.join(root, f))
