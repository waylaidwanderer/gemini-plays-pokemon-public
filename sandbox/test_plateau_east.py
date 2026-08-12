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

def test_boundaries():
    # Currently at (25, 21).
    # Let's walk UP to row 14 to see if we can go Right.
    # Rows 12-14 is where the Central Plateau is supposed to be.
    
    # 1. Walk UP to row 14
    for _ in range(7): # 21 to 14 is 7 steps
        pos = get_pos()
        if pos is None:
            run_away()
            pos = get_pos()
        print(f"Current pos before walking Up: {pos}")
        walk_step("Up")
        
    pos = get_pos()
    print(f"Reached row: {pos}")
    
    # 2. Walk Right to column 26
    while True:
        pos = get_pos()
        if pos is None:
            run_away()
            pos = get_pos()
        cx, cy = pos
        if cx >= 26:
            break
        print(f"Walking Right from {pos}...")
        walk_step("Right")
        
    pos = get_pos()
    print(f"Standing at {pos}. Let's test walking RIGHT...")
    
    # Try walking Right 3 times
    for i in range(3):
        pos = get_pos()
        if pos is None:
            run_away()
            pos = get_pos()
        print(f"Test {i}: before = {pos}")
        walk_step("Right")
        pos2 = get_pos()
        if pos2 is None:
            run_away()
            pos2 = get_pos()
        print(f"Test {i}: after = {pos2}")
        if pos2[0] > pos[0]:
            print("SUCCESS! We walked Right off the plateau!")
            return

    print("BLOCKED! Could not walk Right off the plateau.")

if __name__ == "__main__":
    test_boundaries()
