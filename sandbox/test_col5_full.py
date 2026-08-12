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

def test_col5_route():
    # Currently at (8, 16) on the ground.
    print("Walking Left to Column 5...")
    for step in range(3):
        pos = get_pos()
        if pos is None:
            run_away()
            pos = get_pos()
        walk_step("Left")
        print(f"Step {step}: Pos={get_pos()}")
        
    pos = get_pos()
    print(f"At Column 5: {pos}")
    if pos is None or pos[0] != 5:
        print("Failed to reach Column 5.")
        return
        
    # Walk UP Column 5 to Row 10
    print("Walking UP Column 5 to Row 10...")
    for step in range(10):
        pos = get_pos()
        if pos is None:
            run_away()
            pos = get_pos()
        cx, cy = pos
        if cy == 10:
            break
        walk_step("Up")
        print(f"Step {step}: Pos={get_pos()}")
        
    pos = get_pos()
    print(f"At Row 10: {pos}")
    if pos != (5, 10):
        print("Failed to reach (5, 10).")
        return
        
    # Walk RIGHT along Row 10 to Column 30
    print("Walking RIGHT along Row 10...")
    for step in range(30):
        pos = get_pos()
        if pos is None:
            run_away()
            pos = get_pos()
        cx, cy = pos
        if cx == 30:
            break
        walk_step("Right")
        print(f"Step {step}: Pos={get_pos()}")
        
    pos = get_pos()
    print(f"At transition: {pos}")
    if pos == (30, 10):
        print("SUCCESS! Column 5 and Row 10 ground route is completely open and unblocked!")
        # Transition to Area 1 (East)
        walk_step("Right")
        print(f"Transitioned! Pos: {get_pos()}")

if __name__ == "__main__":
    test_col5_route()
