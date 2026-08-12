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

def test_east_plateau():
    # Currently at (26, 14) on the Plateau.
    # 1. Walk UP to (26, 12)
    print("Walking UP to (26, 12)...")
    walk_step("Up")
    print(f"Pos: {get_pos()}")
    walk_step("Up")
    print(f"Pos: {get_pos()}")
    
    # Verify we are at (26, 12)
    pos = get_pos()
    if pos is None:
        run_away()
        pos = get_pos()
    print(f"At position: {pos}")
    if pos != (26, 12):
        print("Failed to reach (26, 12).")
        return
        
    # 2. Try walking Right on row 12
    print("Trying to walk Right from (26, 12)...")
    walk_step("Right")
    pos_after = get_pos()
    if pos_after is None:
        run_away()
        pos_after = get_pos()
    print(f"Pos after walking Right: {pos_after}")
    if pos_after == (27, 12):
        print("SUCCESS! Walked Right to (27, 12)!")
        # Try one more Right
        walk_step("Right")
        print(f"Pos after second Right: {get_pos()}")
        return
        
    # 3. Try walking Right on row 13
    print("Moving to (26, 13)...")
    walk_step("Down")
    print(f"Pos: {get_pos()}")
    print("Trying to walk Right from (26, 13)...")
    walk_step("Right")
    pos_after = get_pos()
    if pos_after is None:
        run_away()
        pos_after = get_pos()
    print(f"Pos after walking Right: {pos_after}")
    if pos_after == (27, 13):
        print("SUCCESS! Walked Right to (27, 13)!")
        return
        
    # 4. Try walking Right on row 14
    print("Moving to (26, 14)...")
    walk_step("Down")
    print(f"Pos: {get_pos()}")
    print("Trying to walk Right from (26, 14)...")
    walk_step("Right")
    pos_after = get_pos()
    if pos_after is None:
        run_away()
        pos_after = get_pos()
    print(f"Pos after walking Right: {pos_after}")
    if pos_after == (27, 14):
        print("SUCCESS! Walked Right to (27, 14)!")
        return

    print("All rows blocked.")

if __name__ == "__main__":
    test_east_plateau()
