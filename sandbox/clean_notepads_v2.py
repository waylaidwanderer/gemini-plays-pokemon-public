import os

def clean():
    path = "notepads/Locations/PokemonMansion2F.md"
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Remove incorrect line under Southwest Staircase Warp Connections
    # Old line: "- **Staircase on 2F West:** The staircase at (5, 10) on 2F West leads DOWN to 1F West, landing at (5, 11) on 1F West."
    content = content.replace("- **Staircase on 2F West:** The staircase at (5, 10) on 2F West leads DOWN to 1F West, landing at (5, 11) on 1F West.", "")

    # 2. Remove speculative open gates lines under 2F State A Horizontal Connections
    content = content.replace("- **Row 11 Open Gates:** Shutter gates on Row 11 are open in State A, allowing horizontal connection between 2F East and 2F West.", "")
    content = content.replace("allowing horizontal connection between 2F East and 2F West.", "")

    # Also make sure there are no duplicate newlines
    content = content.replace("\n\n\n", "\n\n")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully cleaned Locations/PokemonMansion2F.md on disk!")

if __name__ == "__main__":
    clean()
