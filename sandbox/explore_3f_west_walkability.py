import mgba
import time

def handle_any_menu_or_battle():
    time.sleep(0.1)
    scr_file = mgba.take_screenshot()
    pos = mgba.get_coordinates()
    # No battle detection needed for walkability test as we just want to know if we can step or not
    return False

def try_step(direction, expected_coords):
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos = mgba.get_coordinates()
    if pos == expected_coords:
        return True
    return False

# Stand at (1, 10)
pos = mgba.get_coordinates()
print("Starting position:", pos)

if pos != {"x": 1, "y": 10}:
    # Walk to (1, 10)
    # We are probably at (1, 10) or can get there
    pass

# We want to test walkability on Row 9 for columns 1 to 6
# We can do this by walking to (col, 10) and trying to walk UP to (col, 9)
walkable_paths = {}

for col in range(1, 7):
    # Walk to (col, 10)
    print(f"Testing Column {col}...")
    
    # Simple pathing from (1, 10) to (col, 10):
    # Since Row 10 is the main hallway on 3F West, it is open!
    # Let's walk to (1, 10) first as a safe anchor
    mgba.get_coordinates()
    # Walk to (col, 10) by walking RIGHT or LEFT
    current_pos = mgba.get_coordinates()
    dx = col - current_pos["x"]
    if dx > 0:
        for _ in range(dx):
            mgba.press_buttons(["Right"])
            time.sleep(0.4)
    elif dx < 0:
        for _ in range(-dx):
            mgba.press_buttons(["Left"])
            time.sleep(0.4)
            
    pos = mgba.get_coordinates()
    if pos["x"] == col and pos["y"] == 10:
        # Try to step UP to (col, 9)
        success = try_step("Up", {"x": col, "y": 9})
        walkable_paths[col] = success
        if success:
            print(f"Column {col} Row 9 is WALKABLE!")
            # Walk back down to (col, 10)
            try_step("Down", {"x": col, "y": 10})
        else:
            print(f"Column {col} Row 9 is BLOCKED.")
    else:
        print(f"Failed to reach ({col}, 10), current: {pos}")
        # Walk back to (1, 10)
        current_pos = mgba.get_coordinates()
        dx = 1 - current_pos["x"]
        if dx > 0:
            for _ in range(dx):
                mgba.press_buttons(["Right"])
                time.sleep(0.4)
        elif dx < 0:
            for _ in range(-dx):
                mgba.press_buttons(["Left"])
                time.sleep(0.4)

print("Walkability results on Row 9:")
for col, walkable in walkable_paths.items():
    print(f"Column {col}: {'WALKABLE' if walkable else 'BLOCKED'}")
