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

def test_col8_route():
    # Currently at (17, 24) on the ground.
    print("Clearing 'Got away safely!' text...")
    bridge.press_buttons(["B", "sleep 500"])
    
    pos = get_pos()
    print(f"Starting position: {pos}")
    if pos is None:
        bridge.press_buttons(["B", "sleep 500"])
        pos = get_pos()
        print(f"Position retry: {pos}")
        
    cx, cy = pos
    # We want to be on Row 24. If we are not on Row 24, walk to it.
    if cy < 24:
        print(f"Walking DOWN to Row 24...")
        for _ in range(24 - cy):
            walk_step("Down")
    elif cy > 24:
        print(f"Walking UP to Row 24...")
        for _ in range(cy - 24):
            walk_step("Up")
            
    # Walk Left along Row 24 to Column 8
    print("Walking Left to Column 8...")
    for step in range(16):
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
        
    # Walk UP Column 8 to Row 10
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
        
    # Walk RIGHT along Row 10 to Column 30
    print("Walking RIGHT along Row 10...")
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
        print("SUCCESS! Column 8 and Row 10 route is completely open and unblocked!")
        # Transition to Area 1 (East)
        walk_step("Right")
        print(f"Transitioned! Pos: {get_pos()}")

if __name__ == "__main__":
    test_col8_route()
