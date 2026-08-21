import mgba
import time

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.3)
    pos_after = mgba.get_coordinates()
    
    # Check if we moved
    if pos_before == pos_after:
        print(f"Blocked trying to move {direction} from {pos_before}. Handling battle/text...")
        # Press B to dismiss text or try to escape battle
        mgba.press_buttons(["B", "sleep 200", "Down", "Right", "A", "sleep 1000", "B"])
        time.sleep(1.0)
        # Re-try the move
        mgba.press_buttons([direction])
        time.sleep(0.3)
        pos_after = mgba.get_coordinates()
        print(f"After retry, position is {pos_after}")
    return pos_after

# We are at (20, 7) on 1F East.
# Path to stairs at (18, 3):
# Left 2 to (18, 7)
# Up 4 to (18, 3)

path = ["Left", "Left", "Up", "Up", "Up", "Up"]

print("Walking to 2F East stairs...")
for idx, direction in enumerate(path):
    pos_before = mgba.get_coordinates()
    pos = walk_step(direction)
    print(f"Step {idx} ({direction}): {pos_before} -> {pos}")
    # If we warped (large coordinate change or new map)
    if pos['x'] != pos_before['x'] and abs(pos['x'] - pos_before['x']) > 2:
        print("WARPED!")
        break

time.sleep(1.0)
pos = mgba.get_coordinates()
print("Final position after script:", pos)
mgba.take_screenshot()
