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

def probe_all_crossings():
    # Currently at (26, 14) on top of the Plateau.
    # 1. Walk back to ground level at (24, 16)
    print("Walking back to ground level at (24, 16)...")
    walk_step("Left") # To (25, 14)
    walk_step("Left") # To (24, 14)
    walk_step("Down") # To (24, 15)
    walk_step("Down") # To (24, 16)
    print(f"Pos on ground: {get_pos()}")
    
    # 2. Walk to column 28
    walk_step("Right")
    walk_step("Right")
    walk_step("Right")
    walk_step("Right")
    print(f"Pos: {get_pos()}")
    
    # We should be at (28, 16).
    # We will test walking RIGHT on rows 16 to 22.
    for row in range(16, 23):
        # Walk to the target row on column 28
        pos = get_pos()
        if pos is None:
            run_away()
            pos = get_pos()
        cx, cy = pos
        dy = row - cy
        
        # Adjust Y coordinate
        if dy > 0:
            for _ in range(dy):
                walk_step("Down")
        elif dy < 0:
            for _ in range(-dy):
                walk_step("Up")
                
        pos = get_pos()
        print(f"Testing row {row} from pos {pos}...")
        
        # Try to walk RIGHT
        walk_step("Right")
        pos_after = get_pos()
        if pos_after is None:
            run_away()
            pos_after = get_pos()
            
        print(f"  Result of trying Right on row {row}: {pos_after}")
        if pos_after[0] > pos[0]:
            print(f"  SUCCESS! Row {row} is OPEN to Column 29!")
            # Walk back Left
            walk_step("Left")
        
if __name__ == "__main__":
    probe_all_crossings()
