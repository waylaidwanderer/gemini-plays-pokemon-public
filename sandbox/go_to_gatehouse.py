import time
import sys
import bridge

# Set stdout to use utf-8
sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_step(direction):
    bridge.press_buttons([direction])
    time.sleep(0.4)

def cut_bush():
    print("Cutting the bush at (26, 13)...")
    # Menu sequence to use CUT
    # 1. Open Start menu
    bridge.press_buttons(["Start", "sleep 600"])
    # 2. Go Down to PARTY (usually 1 down from POKEDEX if POKEMON, let's be careful)
    # The menu order in standard Red/Blue is:
    # POKEDEX
    # POKEMON (Party)
    # ITEM
    # ACE (Player)
    # SAVE
    # OPTION
    # EXIT
    # Since cursor starts at POKEDEX or ITEM (usually POKEDEX), we go DOWN 1 to select POKEMON
    # Let's press Down once, then A
    bridge.press_buttons(["Down", "sleep 300", "A", "sleep 1200"])
    
    # We are in the party screen.
    # TRUFFLE (Paras) is in the party. Let's find him.
    # Usually TRUFFLE is the second or third Pokemon.
    # Let's assume TRUFFLE is at slot 2 (1 press of Down) or slot 3 (2 presses of Down).
    # Wait, we can look at our party stats:
    # 1. SHELLBY (Blastoise)
    # 2. TRUFFLE (Paras)
    # Yes! TRUFFLE is in slot 2.
    # So we press Down once to highlight TRUFFLE, then press A.
    bridge.press_buttons(["Down", "sleep 300", "A", "sleep 800"])
    
    # Now the sub-menu for Paras is open:
    # CUT
    # STATS
    # SWITCH
    # CANCEL
    # CUT is the first option, so we press A.
    bridge.press_buttons(["A", "sleep 2500"])
    
    # Let's clear the textboxes after CUT
    print("Clearing cut textboxes...")
    bridge.press_buttons(["A", "sleep 500", "A", "sleep 500", "B", "sleep 500", "B", "sleep 500"])

def main():
    # Target path points
    path_points = [
        # 1. Walk UP Column 1 to Row 21
        (1, 21),
        # 2. Walk RIGHT Row 21 to Column 22
        (22, 21),
        # 3. Walk UP Column 22 to Row 14
        (22, 14),
        # 4. Walk RIGHT Row 14 to Column 26
        (26, 14),
        # 5. Walk UP Column 26 to Row 9 (passing the bush at 26,13)
        (26, 9),
        # 6. Walk LEFT Row 9 to Column 19
        (19, 9),
        # 7. Walk UP Column 19 to Row 8
        (19, 8),
        # 8. Detour around NPC at 24,8
        (23, 9),
        (25, 9),
        (25, 8),
        # 8b. Walk RIGHT Row 8 to Column 37
        (37, 8),
        # 9. Walk UP Column 37 to Row 2
        (37, 2),
        # 10. Walk LEFT Row 2 to Column 22
        (22, 2),
        # 11. Walk DOWN Column 22 to Row 4
        (22, 4),
        # 12. Walk LEFT Row 4 to Column 18
        (18, 4),
        # 13. Walk UP Column 18 to Row 3 (enter Gatehouse!)
        (18, 3)
    ]
    
    print(f"Starting path navigation from: {get_pos()}")
    
    for idx, target in enumerate(path_points):
        print(f"--- Segment {idx+1}: Navigating to target {target} ---")
        consecutive_bumps = 0
        
        while True:
            curr = get_pos()
            if curr is None:
                time.sleep(0.5)
                continue
                
            if curr == target:
                print(f"Reached segment target: {curr}")
                break
                
            # Determine direction
            dx = target[0] - curr[0]
            dy = target[1] - curr[1]
            
            direction = None
            if dx > 0:
                direction = "Right"
            elif dx < 0:
                direction = "Left"
            elif dy > 0:
                direction = "Down"
            elif dy < 0:
                direction = "Up"
                
            if direction is None:
                break
                
            print(f"Current: {curr}, Target: {target}, Walking {direction}...")
            walk_step(direction)
            
            next_pos = get_pos()
            if next_pos == curr:
                consecutive_bumps += 1
                print(f"Bumped! (Count: {consecutive_bumps})")
                
                # Check if we are stuck at the bush at (26, 13)
                if curr == (26, 14) and target == (26, 9) and direction == "Up":
                    print("Detected bush blockage at (26, 13). Attempting CUT...")
                    cut_bush()
                    consecutive_bumps = 0 # Reset bump count after action
                elif consecutive_bumps >= 5:
                    print("Too many consecutive bumps! We might be truly stuck or blocked by something. Aborting.")
                    return
            else:
                consecutive_bumps = 0 # Reset on success

    print(f"Path navigation complete. Current position: {get_pos()}")

if __name__ == "__main__":
    main()
