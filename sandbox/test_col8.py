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
    # Currently at (19, 12) on the Plateau.
    # 1. Walk back to ground level at (24, 16)
    print("Walking back to ground level...")
    # Walk Right to Column 24
    for _ in range(5):
        walk_step("Right")
        print(f"Pos: {get_pos()}")
        
    # Walk Down stairs
    for _ in range(4):
        walk_step("Down")
        print(f"Pos: {get_pos()}")
        
    pos = get_pos()
    print(f"Back on ground: {pos}")
    if pos != (24, 16):
        print("Failed to reach (24, 16).")
        return
        
    # 2. Walk Left along Row 16 to Column 8
    print("Walking Left to Column 8...")
    for _ in range(16):
        walk_step("Left")
        print(f"Pos: {get_pos()}")
        
    pos = get_pos()
    print(f"At column 8: {pos}")
    if pos[0] != 8:
        print("Failed to reach Column 8.")
        return
        
    # 3. Walk UP Column 8 to Row 10
    print("Walking UP Column 8...")
    for _ in range(10):
        pos = get_pos()
        if pos[1] == 10:
            break
        walk_step("Up")
        print(f"Pos: {get_pos()}")
        
    pos = get_pos()
    print(f"At row 10: {pos}")
    if pos != (8, 10):
        print("Failed to reach (8, 10).")
        return
        
    # 4. Walk RIGHT along Row 10 to Column 30
    print("Walking RIGHT along Row 10...")
    for _ in range(25):
        pos = get_pos()
        if pos[0] == 30:
            break
        walk_step("Right")
        print(f"Pos: {get_pos()}")
        
    pos = get_pos()
    print(f"At transition: {pos}")
    if pos == (30, 10):
        print("SUCCESS! Column 8 and Row 10 route is completely open and unblocked!")
        # Transition to Area 1 (East)
        walk_step("Right")
        print(f"Transitioned! Pos: {get_pos()}")

if __name__ == "__main__":
    test_col8_route()
