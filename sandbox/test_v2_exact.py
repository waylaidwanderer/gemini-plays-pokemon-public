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

def test_new_route():
    print("Starting new golden route from (12, 24)...")
    
    # Starting at (12, 24)
    # 1. Walk UP to (12, 23)
    walk_step("Up")
    print(f"Pos after Up: {get_pos()}")
    
    # 2. Walk RIGHT 2 steps to (14, 23)
    walk_step("Right")
    print(f"Pos after Right 1: {get_pos()}")
    walk_step("Right")
    print(f"Pos after Right 2: {get_pos()}")
    
    pos = get_pos()
    if pos != (14, 23):
        print("Failed to reach (14, 23).")
        return
        
    # 3. Walk DOWN to (14, 26)
    walk_step("Down") # To (14, 24)
    print(f"Pos: {get_pos()}")
    walk_step("Down") # To (14, 25)
    print(f"Pos: {get_pos()}")
    walk_step("Down") # To (14, 26)
    print(f"Pos: {get_pos()}")
    
    pos = get_pos()
    if pos != (14, 26):
        print("Failed to reach (14, 26).")
        return
        
    # 4. Walk RIGHT along Row 26 to Column 30
    print("Walking RIGHT along Row 26 to Column 30...")
    for step in range(20):
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
    print(f"At Column 30 Row 26: {pos}")
    if pos[0] != 30:
        print("Failed to reach Column 30.")
        return
        
    # 5. Walk UP Column 30 to Row 11
    print("Walking UP Column 30 to Row 11...")
    for step in range(20):
        pos = get_pos()
        if pos is None:
            run_away()
            pos = get_pos()
        cx, cy = pos
        if cy == 11:
            break
        walk_step("Up")
        print(f"Step {step}: Pos={get_pos()}")
        
    pos = get_pos()
    print(f"At Row 11: {pos}")
    if pos != (30, 11):
        print("Failed to reach (30, 11).")
        return
        
    # 6. Walk LEFT to (29, 11) and then RIGHT to (30, 11) to transition
    print("Aligning and transitioning to Area 1...")
    walk_step("Left")
    print(f"Pos after Left: {get_pos()}")
    walk_step("Right")
    print(f"Pos after transition: {get_pos()}")

if __name__ == "__main__":
    test_new_route()
