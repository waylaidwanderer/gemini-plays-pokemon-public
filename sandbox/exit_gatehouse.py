import mgba
import time

print("--- MAPPING WARDEN'S HOUSE ---")
start_pos = mgba.get_coordinates()
print("Starting search at:", start_pos)

# We want to test walkability of surrounding tiles.
# We will try a move, see if our position changed, and if so, step back to start_pos.

def test_direction(dir_name, back_dir):
    pos_before = mgba.get_coordinates()
    # Press B to ensure no textbox is active
    mgba.press_buttons(["B"])
    time.sleep(0.2)
    
    # Try the move (press twice to handle turn if needed)
    mgba.press_buttons([dir_name])
    time.sleep(0.4)
    mgba.press_buttons([dir_name])
    time.sleep(0.4)
    
    pos_after = mgba.get_coordinates()
    if pos_after != pos_before:
        print(f"Direction {dir_name} is WALKABLE! Reached: {pos_after}")
        # Walk back
        mgba.press_buttons([back_dir])
        time.sleep(0.4)
        mgba.press_buttons([back_dir])
        time.sleep(0.4)
        return True
    else:
        print(f"Direction {dir_name} is BLOCKED!")
        return False

# Test all 4 directions from start_pos (9, 12)
test_direction("Left", "Right")
test_direction("Right", "Left")
test_direction("Up", "Down")
test_direction("Down", "Up")

mgba.take_screenshot()
print("Final position:", mgba.get_coordinates())
