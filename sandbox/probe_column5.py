import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 250"])
    bridge.press_buttons(["Right", "sleep 250", "Down", "sleep 250", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 300"])

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 400"])

def test_bypass():
    # Currently at (5, 24)
    print("Testing Column 5 bypass via Column 4...")
    
    # 1. Walk Left to Column 4
    walk_step("Left") # To (4, 24)
    print(f"Pos: {get_pos()}")
    
    # 2. Walk UP to Row 22
    walk_step("Up") # To (4, 23)
    print(f"Pos: {get_pos()}")
    walk_step("Up") # To (4, 22)
    print(f"Pos: {get_pos()}")
    
    pos = get_pos()
    if pos != (4, 22):
        print("Failed to reach (4, 22).")
        return
        
    # 3. Walk Right to Column 5
    walk_step("Right") # To (5, 22)
    print(f"Pos: {get_pos()}")
    
    pos = get_pos()
    if pos != (5, 22):
        print("Failed to reach (5, 22).")
        return
        
    # 4. Probing UP on Column 5 as far as possible
    print("Probing UP on Column 5 from (5, 22)...")
    for step in range(12):
        cx, cy = get_pos()
        walk_step("Up")
        pos_after = get_pos()
        if pos_after is None:
            run_away()
            pos_after = get_pos()
        print(f"Step {step}: before=({cx}, {cy}), after={pos_after}")
        if pos_after == (cx, cy):
            print(f"BLOCKED! Could not move UP from ({cx}, {cy}).")
            break

if __name__ == "__main__":
    test_bypass()
