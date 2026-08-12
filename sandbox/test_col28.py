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

def test_col28():
    # Currently at (19, 12)
    print("Walking from (19, 12) to (28, 16)...")
    
    # 1. Walk Down to row 16
    for _ in range(4):
        walk_step("Down")
        print(f"Pos: {get_pos()}")
        
    # 2. Walk Right to column 28
    for _ in range(9):
        walk_step("Right")
        print(f"Pos: {get_pos()}")
        
    # We should be at (28, 16)
    pos = get_pos()
    print(f"Arrived at: {pos}")
    if pos != (28, 16):
        print("Failed to reach (28, 16).")
        return
        
    # 3. Walk UP column 28 and print positions
    print("Testing UP column 28...")
    for i in range(7):
        cx, cy = get_pos()
        walk_step("Up")
        pos_after = get_pos()
        print(f"Step {i}: before=({cx}, {cy}), after={pos_after}")
        if pos_after == (cx, cy):
            print(f"BLOCKED at ({cx}, {cy})!")
            break

if __name__ == "__main__":
    test_col28()
