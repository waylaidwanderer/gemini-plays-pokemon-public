import os

filepath = "notepads/Main.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

print("Original Content length:", len(content))
# Let's normalize newlines to make sure it matches
normalized_content = content.replace("\r\n", "\n")

target = """## Global Badges & Progression Status
- **Gym Badges Possessed:** 7 (Boulder, Cascade, Thunder, Rainbow, Soul, Marsh, Volcano).
- **Outstanding Gyms:**
  - Viridian Gym (Giovanni) - Earth Badge (target #8) - Open and active! (Unlocked since we possess 7 Badges)."""

if target in normalized_content:
    print("Found exact match in normalized content!")
    replacement = """## Global Badges & Progression Status
- **Gym Badges Possessed:** 6 (Boulder, Cascade, Thunder, Rainbow, Soul, Marsh).
- **Outstanding Gyms:**
  - Cinnabar Gym (Blaine) - Volcano Badge (target #7) - Locked (needs Secret Key from Pokémon Mansion).
  - Viridian Gym (Giovanni) - Earth Badge (target #8) - Locked (requires 7 Badges to enter)."""
    new_content = normalized_content.replace(target, replacement)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Replaced successfully!")
else:
    print("Exact match not found.")
    lines = content.splitlines()
    for idx, line in enumerate(lines[:20]):
        print(f"{idx}: {repr(line)}")
