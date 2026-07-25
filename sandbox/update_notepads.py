import os

def update_progression():
    path = "notepads/Progression_And_Party_Stats.md"
    if not os.path.exists(path):
        print(f"Path {path} does not exist!")
        return
        
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Let's add the Bug Catcher defeat
    old_target_list = "  - **Defeated Bug Catcher Kenton:** Defeated Bug Catcher Kenton at (7, 22) on Turn 2031, earning ¥110.\n  - **Obtained Item (Potion):** Found and retrieved Potion at (2, 20) on Mt. Moon 1F on Turn 2068."
    new_target_list = "  - **Defeated Bug Catcher Kenton:** Defeated Bug Catcher Kenton at (7, 22) on Turn 2031, earning ¥110.\n  - **Obtained Item (Potion):** Found and retrieved Potion at (2, 20) on Mt. Moon 1F on Turn 2068.\n  - **Defeated Bug Catcher (South-East):** Defeated Bug Catcher at (30, 27) on Mt. Moon 1F on Turn 2697, earning ¥100."
    
    if old_target_list in content:
        content = content.replace(old_target_list, new_target_list)
        print("Updated progression list successfully.")
    else:
        print("Progression target list not found!")
        # Let's try matching a smaller part
        smaller_old = "  - **Obtained Item (Potion):** Found and retrieved Potion at (2, 20) on Mt. Moon 1F on Turn 2068."
        smaller_new = "  - **Obtained Item (Potion):** Found and retrieved Potion at (2, 20) on Mt. Moon 1F on Turn 2068.\n  - **Defeated Bug Catcher (South-East):** Defeated Bug Catcher at (30, 27) on Mt. Moon 1F on Turn 2697, earning ¥100."
        if smaller_old in content:
            content = content.replace(smaller_old, smaller_new)
            print("Updated progression list using smaller match.")
            
    # Now let's update Pikachu's stats
    old_tesla = """- **TESLA (Pikachu):**
  - **Level:** 8
  - **Moveset:** ThunderShock (28/30 PP), Growl (40/40 PP)
  - **Stats:** Attack 12, Defense 10, Speed 19, Special 12
  - **HP:** 22 / 24
  - **Status:** Healthy"""

    new_tesla = """- **TESLA (Pikachu):**
  - **Level:** 10
  - **Moveset:** ThunderShock (18/30 PP), Growl (40/40 PP), Thunder Wave (30/30 PP)
  - **Stats:** Attack 14, Defense 11, Speed 22, Special 14
  - **HP:** 15 / 26
  - **Status:** Healthy"""

    if old_tesla in content:
        content = content.replace(old_tesla, new_tesla)
        print("Updated Tesla's stats successfully.")
    else:
        # Let's try replacing with a simpler substring
        print("Tesla's old stats block not matched exactly on newlines. Trying line by line.")
        lines = content.split('\n')
        new_lines = []
        skip = False
        for line in lines:
            if "- **TESLA (Pikachu):**" in line:
                new_lines.append(new_tesla)
                skip = True
                continue
            if skip:
                if "- **GUSTY (Pidgey):**" in line or "##" in line or "- **NIBBLES" in line:
                    skip = False
                else:
                    continue
            new_lines.append(line)
        content = '\n'.join(new_lines)
        print("Updated Tesla's stats using line parsing.")
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def update_b2f():
    path = "notepads/Locations/MtMoon_B2F.md"
    if not os.path.exists(path):
        print(f"Path {path} does not exist!")
        return
        
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    old_block = "- **Wall Blockage (Burden of Proof Updated):** Columns 18-19 form a rock wall on rows 14 to 21, but are completely **OPEN** on row 12 and rows 22-27, allowing direct horizontal transit between the starting area and the main cavern!"
    new_block = "- **Wall Blockage:** Columns 18-19 form a rock wall on rows 14 to 21."
    
    if old_block in content:
        content = content.replace(old_block, new_block)
        print("Updated B2F wall blockage successfully.")
    else:
        print("B2F old block not matched exactly.")
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    update_progression()
    update_b2f()
