import time
import sys
import bridge

# Set stdout to use utf-8
sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 350"])

def test_moves():
    print("Testing left-side paths from (2, 14)...")
    pos = get_pos()
    print(f"Start pos: {pos}")
    
    # Let's walk DOWN to (2, 16)
    walk_step("Down")
    walk_step("Down")
    pos = get_pos()
    print(f"At: {pos}")
    
    # Try Left to (1, 16)
    walk_step("Left")
    pos = get_pos()
    print(f"At: {pos}")
    
    if pos == (1, 16):
        # We are at (1, 16). Let's test going Left, Down, Up
        for d in ["Left", "Down", "Up"]:
            print(f"Testing {d} from (1, 16)...")
            walk_step(d)
            npos = get_pos()
            print(f"Result: {npos}")
            if npos != (1, 16) and npos is not None:
                # Walk back
                opp = {"Left": "Right", "Down": "Up", "Up": "Down"}[d]
                walk_step(opp)
                
    # Walk back to (2, 14) to keep start position
    pos = get_pos()
    if pos == (1, 16):
        walk_step("Right")
    pos = get_pos()
    if pos == (2, 16):
        walk_step("Up")
        walk_step("Up")
    print(f"Back at start? {get_pos()}")

if __name__ == "__main__":
    test_moves()
