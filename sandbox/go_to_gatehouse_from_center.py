import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos[0], pos[1]
        time.sleep(0.1)
    return None

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return None
        
    bridge.press_buttons([direction])
    
    # Wait for position to change
    for _ in range(5):
        time.sleep(0.15)
        new_pos = get_pos()
        if new_pos is not None and new_pos != pos:
            return new_pos
            
    print(f"Bumping/stuck at {pos} walking {direction}!")
    return pos

def run_path(path, check_warp=False):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            if check_warp:
                print("Transition occurred (pos is None)!")
                return True
            time.sleep(0.5)
            continue
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            time.sleep(0.5)
            new_pos = get_pos()
            if new_pos is None:
                if check_warp:
                    print("Transition occurred (pos is None after retry)!")
                    return True
                continue
                
        if new_pos == pos:
            stuck_count += 1
            if stuck_count > 3:
                print(f"Blocked at {pos}! Exiting path.")
                return False
        else:
            stuck_count = 0
            if check_warp:
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"Transition occurred! New pos: {new_pos}")
                    break
            idx += 1
    return True

def main():
    print("=== NAVIGATING FROM CENTER TO SAFARI ZONE GATEHOUSE ===")
    
    pos = get_pos()
    print("Initial position outside Center:", pos)
    if pos is None:
        print("Failed to get starting position!")
        return
        
    # We are at (19, 28)
    # Walk Down 4 steps to (19, 32)
    # Walk Left 18 steps to (1, 32)
    # Walk Up 18 steps to (1, 14)
    # Walk Right 25 steps to (26, 14)
    # Walk Up 5 steps to (26, 9) -- Wait! There is a cut-able bush at (26, 13). Is it cut?
    # Let's check: "Regrowing Cut-able Bush (26, 13): regrows immediately upon reloading the map or entering/exiting the Safari Zone."
    # Since we left the PC, the bush at (26, 13) has REGROWN!
    # Do we have Paras in our party to CUT it? Yes, TRUFFLE (Paras) is in our party.
    # But wait, is there an alternative route to the east side of Fuchsia City that doesn't require CUT?
    # Let's look at the Fuchsia City notes:
    # "To reach Column 37 from Row 14: Walk UP along Column 22 to Row 14, walk Right along Row 14 to Column 26, walk Up along Column 26 (through cut bush at 26,13)..."
    # Wait, can we bypass the cut-able bush?
    # Let's check if we can go:
    # From (1, 14), can we go to Row 8 or 9 directly?
    # Wait! "Row 7 Barrier: A continuous solid pine tree wall running horizontally from Column 13 to Column 35, completely blocking direct vertical traversal from the south to the northern corridor (Row 2)."
    # Wait, "Column 37 Passage: The ONLY walkable vertical gap in the Row 7 tree barrier, allowing players to walk UP from Row 8/9 to Row 2 to reach the northernmost corridor."
    # So we MUST go to Column 37 Row 8/9.
    # To get to Column 37, we must cross Column 26, Row 13.
    # Wait, is the bush at (26, 13) the only way?
    # Let's check if there is another way to the east.
    # Wait, what about Column 30? "Column 30 Row 14 Wandering NPC: A wandering NPC who can block traversal on Column 30 Row 14."
    # Can we walk to Column 37 on Row 14 without CUT?
    # "walk Right along Row 14 to Column 26, walk Up along Column 26 (through cut bush at 26,13)..."
    # Wait, why do we need to walk Up along Column 26?
    # Ah! Row 14 from Column 26 to Column 37 is blocked?
    # Yes, "Row 16 Tree Barrier (Columns 27-35): Solid horizontal line of trees running across Columns 27-35 on Row 16, blocking direct vertical ground crossing (Turn 36325)."
    # Wait, if Row 16 is blocked, Row 14 should be open?
    # No, wait, let's look at the map of Fuchsia City.
    # If we are on Row 14, can we walk all the way to Column 37?
    # Let's check if Row 14 is open from Column 1 to Column 37.
    # Wait, the notes say:
    # "To reach Column 37 from Row 14: Walk Right along Row 14 to Column 26, walk Up along Column 26 (through cut bush at 26,13) to Row 9, walk Left to Column 19 on Row 9, walk Up along Column 19 to Row 8, walk Right along Row 8/9 to Column 37, walk Up along Column 37 to Row 2..."
    # If Row 14 was open from Column 26 to 37, why would we need to walk up Column 26 and then do that long detour?
    # Ah! Because Row 14 east of Column 26 is blocked by walls/fences/trees!
    # So we definitely need to use CUT on the bush at (26, 13).
    # Let's write a function in our script to use CUT on the bush at (26, 13)!
    # Wait, how do we use CUT?
    # First, stand at (26, 14) facing UP.
    # Then open menu (Start), select POKEMON, select TRUFFLE (Paras), select CUT.
    # Let's check if we can do that!
    # Let's look at how CUT was used previously.
    # To use CUT:
    # `bridge.press_buttons(["Start", "sleep 600", "Down", "A", "sleep 600", "A", "sleep 600", "A", "sleep 1200", "B", "sleep 600", "B", "sleep 600"])`
    # Let's verify the menu navigation for CUT:
    # 1. Start opens menu. Cursor is at POKEDEX or last used. (Wait, in Gen 1, the cursor on Start menu is usually on the last option used, but let's press Up or Down to ensure it selects POKEMON. Usually we can select POKEMON directly if we know where the cursor is, or we can just scroll).
    # Actually, is there a simpler way?
    # Let's write a python function to CUT the bush at (26, 13).
    # Since TRUFFLE is in the party:
    # We can use CUT!
    # Wait! Is TRUFFLE still in our party?
    # Yes, our loaded notepad `Progression_And_Party_Stats` says:
    # "2. TRUFFLE (Paras) - Level: 15 - Status: Healthy"
    # Let's write the navigation path:
    # 1. Walk from (19, 28) to (26, 14):
    #    Path:
    #    - Down 4 to (19, 32)
    #    - Left 18 to (1, 32)
    #    - Up 18 to (1, 14)
    #    - Right 25 to (26, 14)
    # 2. At (26, 14), face UP and use CUT.
    # 3. Walk Up 5 to (26, 9)
    # 4. Walk Left 7 to (19, 9)
    # 5. Walk Up 1 to (19, 8)
    # 6. Walk Right 18 to (37, 8)
    # 7. Walk Up 6 to (37, 2)
    # 8. Walk Left 19 to (18, 2)
    # 9. Walk Down to enter Gatehouse at (18, 3) (Gatehouse warp)
    
    path_to_bush = (
        ["Down"] * 4 +
        ["Left"] * 18 +
        ["Up"] * 18 +
        ["Right"] * 25
    )
    
    if not run_path(path_to_bush):
        print("Failed to reach the cut-able bush!")
        return
        
    print("At (26, 14). Facing UP...")
    bridge.press_buttons(["Up", "sleep 300"])
    
    print("Using CUT...")
    # Open Start menu, go to POKEMON, select Paras, select CUT
    # We can press Start, then press Down to select POKEMON, press A.
    # In Gen 1, the Start menu layout is:
    # 1. POKEDEX
    # 2. POKEMON
    # 3. ITEM
    # 4. ACE (Player)
    # 5. SAVE
    # 6. OPTION
    # 7. EXIT
    # To go from POKEDEX to POKEMON, we press Down once, then A.
    # Let's make sure the cursor is at the top of the Start menu by pressing Up a few times first (safe reset).
    # Or we can just press Start, then Up 6 times (which wraps to the top or stays at top depending on cursor state, but in Gen 1, holding Up/pressing Up multiple times ensures we are at the top).
    # Then press Down to select POKEMON, press A.
    # Inside POKEMON menu, Paras is usually the second Pokémon in our party (first is SHELLBY).
    # So press Down once to select Paras, press A.
    # Select CUT (which is usually the first option in the pop-up menu, so press A).
    # Let's execute this button sequence:
    cut_sequence = [
        "Start", "sleep 600",
        "Up", "Up", "Up", "Up", "Up", "Up", "sleep 300", # Align to POKEDEX
        "Down", "A", "sleep 1000",                       # Select POKEMON
        "Down", "A", "sleep 1000",                       # Select Paras (2nd slot)
        "A", "sleep 1500",                               # Select CUT
        "B", "sleep 500", "B", "sleep 500"               # Close any lingering menus
    ]
    bridge.press_buttons(cut_sequence)
    time.sleep(2.0)
    
    # Verify we can walk through the bush
    pos = get_pos()
    print("Position after CUT attempt:", pos)
    
    # Path from (26, 14) through the bush to the Gatehouse entrance
    path_from_bush = (
        ["Up"] * 5 +                                                      # to (26, 9)
        ["Left"] * 7 +                                                     # to (19, 9)
        ["Up"] * 1 +                                                      # to (19, 8)
        ["Right"] * 18 +                                                   # to (37, 8)
        ["Up"] * 6 +                                                       # to (37, 2)
        ["Left"] * 19 +                                                    # to (18, 2)
        ["Down"]                                                          # to (18, 3) (Gatehouse warp)
    )
    
    if run_path(path_from_bush, check_warp=True):
        print("Successfully reached Safari Zone Gatehouse!")
    else:
        print("Failed to reach Safari Zone Gatehouse from bush!")

if __name__ == "__main__":
    main()
