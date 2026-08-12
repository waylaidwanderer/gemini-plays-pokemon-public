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

def test_west_plateau():
    print("Testing LEFT from (20, 12)...")
    pos = get_pos()
    print(f"Current pos: {pos}")
    
    # Try Left
    walk_step("Left")
    pos2 = get_pos()
    print(f"Pos after Left: {pos2}")
    
    if pos2 == (19, 12):
        # Try Left again
        walk_step("Left")
        pos3 = get_pos()
        print(f"Pos after second Left: {pos3}")
        
        # Try UP
        print("Trying UP from new pos...")
        walk_step("Up")
        print(f"Pos after UP: {get_pos()}")

if __name__ == "__main__":
    test_west_plateau()
