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

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300", "B", "sleep 300"])
    bridge.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 300"])

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 350"])

def test_walk_east():
    print("Starting horizontal East walk test on Row 24...")
    pos = get_pos()
    if pos is None:
        run_away()
        pos = get_pos()
    print(f"Start position: {pos}")
    
    # We are currently at (12, 24). We will try to walk to (15, 24) step-by-step
    for x in range(13, 16):
        print(f"Trying to walk to ({x}, 24)...")
        walk_step("Right")
        new_pos = get_pos()
        if new_pos is None:
            run_away()
            new_pos = get_pos()
        if new_pos is not None and new_pos[0] == x and new_pos[1] == 24:
            print(f"Successfully reached ({x}, 24)!")
        else:
            print(f"Blocked! Cannot reach ({x}, 24). Current position: {new_pos}")
            break

if __name__ == "__main__":
    test_walk_east()
