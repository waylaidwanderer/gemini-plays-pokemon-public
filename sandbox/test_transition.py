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

def test_shortcut():
    print("Testing direct horizontal transition on Row 22...")
    
    # Starting at (27, 24)
    path = ["Up", "Up", "Right", "Right", "Right"]
    
    for i, direction in enumerate(path):
        pos = get_pos()
        if pos is None:
            run_away()
            pos = get_pos()
        print(f"Step {i}: pos before = {pos}")
        
        walk_step(direction)
        
        pos2 = get_pos()
        if pos2 is None:
            run_away()
            pos2 = get_pos()
        print(f"Step {i}: pos after = {pos2}")
        
        # If we transitioned to Area 1 (East), the coordinate will be (0, 22)
        if pos2 == (0, 22) or pos2 == (0, 23):
            print("SUCCESS! Transitioned to Area 1 (East) successfully!")
            break

if __name__ == "__main__":
    test_shortcut()
