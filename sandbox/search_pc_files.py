import os

print("--- SEARCHING FOR GO TO PC FILES ---")
for f in os.listdir("."):
    if "pc" in f.lower() or "center" in f.lower():
        print(f)
