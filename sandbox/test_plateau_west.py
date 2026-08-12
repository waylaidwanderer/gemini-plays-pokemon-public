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

def test_west_plateau_cols():
    # Currently at (27, 22)
    print("Clearing battle text...")
    bridge.press_buttons(["B", "sleep 500"])
    print("Continuing walk to the stairs from (27, 22)...")
    walk_step("Left") # To (26, 22)
    walk_step("Left") # To (25, 22)
    walk_step("Left") # To (24, 22)
    walk_step("Up")   # To (24, 21)
    walk_step("Up")   # To (24, 20)
    walk_step("Up")   # To (24, 19)
    walk_step("Up")   # To (24, 18)
    walk_step("Up")   # To (24, 17)
    walk_step("Up")   # To (24, 16)
    walk_step("Up")   # To (24, 15) (stairs)
    walk_step("Up")   # To (24, 14) (plateau)
    walk_step("Up")   # To (24, 13)
    walk_step("Up")   # To (24, 12)
    
    pos = get_pos()
    print(f"At position: {pos}")
    if pos != (24, 12):
        print("Failed to reach (24, 12).")
        return
        
    # We will test Columns 23, 22, 21, 20 by walking Left and trying UP
    for col in range(23, 19, -1):
        # Walk Left to the target column
        pos = get_pos()
        if pos is None:
            run_away()
            pos = get_pos()
        cx, cy = pos
        dx = col - cx
        if dx < 0:
            for _ in range(-dx):
                walk_step("Left")
                
        pos = get_pos()
        print(f"Testing Column {col} from pos {pos}...")
        
        # Try UP
        walk_step("Up")
        pos_after = get_pos()
        if pos_after is None:
            run_away()
            pos_after = get_pos()
            
        print(f"  Result of UP on column {col}: {pos_after}")
        if pos_after[1] < pos[1]:
            print(f"  SUCCESS! Column {col} is OPEN UP to row 11!")
            # Walk back Down to Plateau row 12
            walk_step("Down")
            return True
            
    print("All western columns blocked on north edge.")
    return False

if __name__ == "__main__":
    test_west_plateau_cols()
