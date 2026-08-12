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

def test_column5():
    # Currently at (8, 24).
    # 1. Walk Left to (5, 24)
    print("Walking Left to Column 5...")
    for _ in range(3):
        walk_step("Left")
        print(f"Pos: {get_pos()}")
        
    pos = get_pos()
    print(f"At Column 5: {pos}")
    if pos is None or pos[0] != 5:
        print("Failed to reach Column 5.")
        return
        
    # 2. Walk UP Column 5 as far as possible
    print("Probing UP on Column 5...")
    for step in range(15):
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
    test_column5()
