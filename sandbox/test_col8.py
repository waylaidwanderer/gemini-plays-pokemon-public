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

def test_v2_route():
    # Currently at (17, 22)
    print("Starting v2 ground route from (17, 22)...")
    
    # 1. Walk Down to Row 24
    walk_step("Down") # To (17, 23)
    print(f"Pos: {get_pos()}")
    walk_step("Down") # To (17, 24)
    print(f"Pos: {get_pos()}")
    
    pos = get_pos()
    if pos is None:
        run_away()
        pos = get_pos()
    print(f"At Row 24: {pos}")
    if pos[1] != 24:
        print("Failed to reach Row 24.")
        return
        
    # 2. Walk Left to Column 8
    print("Walking Left to Column 8...")
    for step in range(12):
        pos = get_pos()
        if pos is None:
            run_away()
            pos = get_pos()
        cx, cy = pos
        if cx == 8:
            break
        walk_step("Left")
        print(f"Step {step}: Pos={get_pos()}")
        
    pos = get_pos()
    print(f"At Column 8: {pos}")
    if pos[0] != 8:
        print("Failed to reach Column 8.")
        return
        
    # 3. Walk UP Column 8 to Row 10
    print("Walking UP Column 8 to Row 10...")
    for step in range(20):
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
    if pos != (8, 10):
        print("Failed to reach (8, 10).")
        return
        
    # 4. Walk RIGHT along Row 10 to Column 30
    print("Walking RIGHT along Row 10 to Column 30...")
    for step in range(25):
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
        print("SUCCESS! Column 8 and Row 10 ground route is completely open and unblocked!")
        # Transition to Area 1 (East)
        walk_step("Right")
        print(f"Transitioned! Pos: {get_pos()}")

if __name__ == "__main__":
    test_v2_route()
