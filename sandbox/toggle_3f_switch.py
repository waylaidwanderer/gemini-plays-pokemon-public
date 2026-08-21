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

# Current position: (7, 10) on 3F West.
# Path to (2, 10):
# Down to (7, 11)
# Left 5 to (2, 11)
# Up 1 to (2, 10)

path = ["Down", "Left", "Left", "Left", "Left", "Left", "Up"]

print("Walking to switch on 3F West...")
for direction in path:
    pos = walk_step(direction)
    print("At:", pos)

time.sleep(1.0)
pos = mgba.get_coordinates()
print("Standing at switch position:", pos)

# Press A to toggle the switch
print("Pressing A to toggle switch...")
mgba.press_buttons(["A", "sleep 500", "A", "sleep 500"])
time.sleep(1.0)

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
