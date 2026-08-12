import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_away():
    print("Interaction/Battle detected. Clearing...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 250"])
    bridge.press_buttons(["Right", "sleep 250", "Down", "sleep 250", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 300"])

def test_north():
    # Currently at (24, 12).
    # Try to walk UP to (24, 11).
    pos = get_pos()
    print(f"Starting position: {pos}")
    
    print("Walking UP...")
    bridge.press_buttons(["Up", "sleep 450"])
    
    pos2 = get_pos()
    if pos2 is None:
        run_away()
        pos2 = get_pos()
    print(f"Position after walking UP: {pos2}")
    
    if pos2 == (24, 11):
        print("SUCCESS! Walked UP off the plateau to (24, 11)!")
    else:
        print("BLOCKED! Could not walk UP off the plateau.")

if __name__ == "__main__":
    test_north()
