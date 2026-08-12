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

def probe_fence():
    # Currently at (8, 16).
    # 1. Walk Down to Row 24
    print("Walking Down to Row 24...")
    for _ in range(8):
        pos = get_pos()
        if pos is None:
            run_away()
            pos = get_pos()
        walk_step("Down")
        print(f"Pos: {get_pos()}")
        
    pos = get_pos()
    print(f"At Row 24: {pos}")
    if pos[1] != 24:
        print("Failed to reach Row 24.")
        return
        
    # We want to test walking DOWN to Row 25 on Columns 16 to 22
    for col in range(16, 23):
        pos = get_pos()
        if pos is None:
            run_away()
            pos = get_pos()
        cx, cy = pos
        
        # Walk horizontally to the target column on Row 24
        dx = col - cx
        if dx > 0:
            for _ in range(dx):
                walk_step("Right")
        elif dx < 0:
            for _ in range(-dx):
                walk_step("Left")
                
        pos = get_pos()
        print(f"Testing Column {col} on Row 24: {pos}")
        
        # Try to walk DOWN
        walk_step("Down")
        pos_after = get_pos()
        if pos_after is None:
            run_away()
            pos_after = get_pos()
            
        print(f"  Result of DOWN on column {col}: {pos_after}")
        if pos_after[1] > pos[1]:
            print(f"  SUCCESS! Column {col} Row 25 is OPEN DOWN to Row 25/26!")
            # Walk back UP to Row 24
            walk_step("Up")
            return True
            
    print("All tested columns on Row 25 blocked.")
    return False

if __name__ == "__main__":
    probe_fence()
