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

def test_column14():
    # Currently at (5, 24)
    print("Walking RIGHT along Row 24 to Column 14...")
    for step in range(12):
        pos = get_pos()
        if pos is None:
            run_away()
            pos = get_pos()
        cx, cy = pos
        if cx == 14:
            break
        walk_step("Right")
        print(f"Step {step}: Pos={get_pos()}")
        
    pos = get_pos()
    print(f"At Column 14 Row 24: {pos}")
    if pos[0] != 14:
        print("Failed to reach Column 14.")
        return
        
    # Try to walk UP to (14, 23)
    print("Trying UP on Column 14...")
    walk_step("Up")
    pos_after = get_pos()
    if pos_after is None:
        run_away()
        pos_after = get_pos()
    print(f"Pos after UP: {pos_after}")
    
    if pos_after == (14, 23):
        print("SUCCESS! Column 14 is open going UP to Row 23!")
        # Try to walk Left on Row 23 to Column 10
        print("Testing Left on Row 23...")
        for _ in range(4):
            walk_step("Left")
            print(f"Pos: {get_pos()}")
    else:
        print("BLOCKED! Column 14 is blocked going UP.")

if __name__ == "__main__":
    test_column14()
