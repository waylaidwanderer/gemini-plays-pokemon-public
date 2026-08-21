# Let's search the system for the ROM file!
# Since we are on Windows (based on C:\Users\joel\AppData\Roaming\uv\python...), we can search for .gb or .gbc files starting from C:\Users\joel or C:\
import os

print("Searching for ROM...")
found = []
# Let's search C:\Users\joel\desktop
search_paths = ["C:\\Users\\joel\\desktop", "C:\\Users\\joel\\Desktop", "C:\\Users\\joel"]
for sp in search_paths:
    if os.path.exists(sp):
        print(f"Searching in {sp}...")
        for root, dirs, files in os.walk(sp):
            # To avoid scanning everything and timing out, let's limit the depth
            if root.count(os.sep) - sp.count(os.sep) > 3:
                continue
            for f in files:
                if f.endswith(".gb") or f.endswith(".gbc") or "blue" in f.lower() or "red" in f.lower():
                    fp = os.path.join(root, f)
                    print("Found candidate file:", fp)
                    found.append(fp)
            if len(found) > 10:
                break
    if len(found) > 10:
        break

print("Search finished!")
