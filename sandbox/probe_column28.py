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

def probe_up_column28():
    print("Starting UP walk test on Column 28 from current position...")
    pos = get_pos()
    if pos is None:
        run_away()
        pos = get_pos()
    print(f"Start position: {pos}")
    
    # We will try to walk UP step-by-step from y=22 to y=11 on Column 28
    for y in range(pos[1] - 1, 10, -1):
        print(f"Trying to walk UP to (28, {y})...")
        walk_step("Up")
        new_pos = get_pos()
        if new_pos is None:
            run_away()
            new_pos = get_pos()
        if new_pos is not None and new_pos[0] == 28 and new_pos[1] == y:
            print(f"Successfully reached (28, {y})!")
        else:
            print(f"Blocked! Cannot reach (28, {y}). Current position: {new_pos}")
            break

if __name__ == "__main__":
    probe_up_column28()
