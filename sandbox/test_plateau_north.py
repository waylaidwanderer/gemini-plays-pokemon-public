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

def test_cols():
    # Currently at (27, 16)
    # 1. Walk Left to (24, 16)
    path_to_stairs = ["Left", "Left", "Left"]
    for d in path_to_stairs:
        walk_step(d)
        print(f"Pos: {get_pos()}")
        
    # 2. Walk UP onto the Plateau to row 12
    for _ in range(4):
        walk_step("Up")
        print(f"Pos: {get_pos()}")
        
    # We should be at (24, 12)
    # Test Column 25
    print("Moving to column 25...")
    walk_step("Right")
    pos_25 = get_pos()
    print(f"Pos: {pos_25}")
    if pos_25 == (25, 12):
        print("Trying UP on column 25...")
        walk_step("Up")
        pos_after = get_pos()
        print(f"Pos after UP: {pos_after}")
        if pos_after == (25, 11):
            print("SUCCESS on Column 25!")
            return
        # Go back to row 12
        walk_step("Down")
        
    # Test Column 26
    print("Moving to column 26...")
    walk_step("Right")
    pos_26 = get_pos()
    print(f"Pos: {pos_26}")
    if pos_26 == (26, 12):
        print("Trying UP on column 26...")
        walk_step("Up")
        pos_after = get_pos()
        print(f"Pos after UP: {pos_after}")
        if pos_after == (26, 11):
            print("SUCCESS on Column 26!")
            return
            
    print("Both Column 25 and 26 blocked.")

if __name__ == "__main__":
    test_cols()
