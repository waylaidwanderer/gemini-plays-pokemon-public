import os

path = "notepads/Scratchpad/Switch_Matrix.md"

if os.path.exists(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    old_segment = """4. Walk back to the stairs at `(7, 10)` on 2F (State A) and ascend to 3F:
   - Correct bypass route: `Down` to `(1, 13)` -> `Right` to `(4, 13)` -> `Up` to `(4, 10)` -> `Right` to `(7, 10)` stairs (Warp to 3F).
5. On 3F (State A), walk to the Mewtwo statue switch at `(12, 11)`:
   - From `(7, 11)` landing:
     - `Right` to `(8, 11)` -> `Right` to `(9, 11)` -> `Down` to `(9, 12)` -> `Right` to `(11, 12)` -> `Up` to `(11, 11)`.
     - Face `Right` (towards the statue at (12, 11)) and press `A` to toggle the switch to **State B**!
6. On 3F (State B), walk to the balcony drop at `(24, 14)` via Row 5:
   - Walk `Up` column 11 to `(11, 5)` -> Walk `Right` along row 5 to `(24, 5)` (Gate at (21, 5) is OPEN in State B!) -> Walk `Down` the balcony to `(24, 14)`.
7. Step `Left` off the balcony edge at `(24, 14)` to drop directly to 1F B1F stairs!"""

    new_segment = """4. Walk back to the stairs at `(7, 10)` on 2F (State A) and ascend to 3F:
   - Correct bypass route: `Down` to `(1, 13)` -> `Right` to `(4, 13)` -> `Up` to `(4, 10)` -> `Right` to `(7, 10)` stairs (Warp to 3F).
5. On 3F (State A), walk to the true west-side Mewtwo statue switch at `(2, 11)`:
   - From `(7, 11)` landing, walk Left to `(2, 12)` and face Up.
   - Press `A` to toggle the switch to **State B**!
6. On 3F (State B), walk to the balcony drop on the east side of 3F:
   - From `(2, 12)`, walk Right to `(7, 12)` -> Down to `(7, 13)` -> Right to `(9, 13)` -> Up to `(9, 10)` (bypassing column 8 even-row pillars) -> Right to `(11, 10)`.
   - Walk Up column 11 to `(11, 5)` -> Right along row 5 to `(21, 5)` (Gate at (21, 5) is OPEN in State B!).
   - Walk Up to `(21, 3)` -> Right to `(26, 3)` (bypassing row 4 wall at cols 22-25) -> Down to `(26, 5)` -> Left to `(24, 5)`.
   - Walk Down column 24 to `(24, 7)`.
   - Walk Right to `(26, 7)` -> Down column 26 to `(26, 12)` (bypassing row 8 raised platform) -> Left to `(25, 12)` -> Down column 25 to `(25, 14)` -> Left to `(22, 14)` (bypassing row 13 railing at col 26).
   - Enter balcony doorway at `(21, 15)` and step on the balcony at `(20, 15)`.
7. Step Left on the balcony to find the true drop edge!"""

    if old_segment in content:
        content = content.replace(old_segment, new_segment)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Successfully updated Switch_Matrix.md on disk!")
    else:
        # Try a more loose match
        print("Old segment not found exactly. Trying loose replacement...")
        lines = content.splitlines()
        replaced = False
        start_idx = -1
        end_idx = -1
        for idx, line in enumerate(lines):
            if "5. On 3F (State A), walk to the Mewtwo statue" in line:
                start_idx = idx
            if "7. Step `Left` off the balcony edge" in line:
                end_idx = idx
                break
        if start_idx != -1 and end_idx != -1:
            # Replace lines between start_idx and end_idx with new steps
            new_lines = lines[:start_idx] + [
                "5. On 3F (State A), walk to the true west-side Mewtwo statue switch at `(2, 11)`:",
                "   - From `(7, 11)` landing, walk Left to `(2, 12)` and face Up.",
                "   - Press `A` to toggle the switch to **State B**!",
                "6. On 3F (State B), walk to the balcony drop on the east side of 3F:",
                "   - From `(2, 12)`, walk Right to `(7, 12)` -> Down to `(7, 13)` -> Right to `(9, 13)` -> Up to `(9, 10)` (bypassing column 8 even-row pillars) -> Right to `(11, 10)`.",
                "   - Walk Up column 11 to `(11, 5)` -> Right along row 5 to `(21, 5)` (Gate at (21, 5) is OPEN in State B!).",
                "   - Walk Up to `(21, 3)` -> Right to `(26, 3)` (bypassing row 4 wall at cols 22-25) -> Down to `(26, 5)` -> Left to `(24, 5)`.",
                "   - Walk Down column 24 to `(24, 7)`.",
                "   - Walk Right to `(26, 7)` -> Down column 26 to `(26, 12)` (bypassing row 8 raised platform) -> Left to `(25, 12)` -> Down column 25 to `(25, 14)` -> Left to `(22, 14)` (bypassing row 13 railing at col 26).",
                "   - Enter balcony doorway at `(21, 15)` and step on the balcony at `(20, 15)`.",
                "7. Step Left on the balcony to find the true drop edge!"
            ] + lines[end_idx+1:]
            with open(path, "w", encoding="utf-8") as f:
                f.write("\n".join(new_lines))
            print("Successfully performed loose replacement on disk!")
            replaced = True
            
        if not replaced:
            print("Failed to find replacement section on disk.")
else:
    print("Switch_Matrix.md does not exist on disk.")
