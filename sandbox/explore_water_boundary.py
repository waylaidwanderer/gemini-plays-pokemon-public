import mgba
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)

def step(direction):
    curr = mgba.get_coordinates()
    cx, cy = curr['x'], curr['y']
    mgba.press_buttons([direction])
    time.sleep(0.45)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == cx and new_pos['y'] == cy:
        escape_battle()
        time.sleep(0.5)
        after = mgba.get_coordinates()
        if after['x'] == cx and after['y'] == cy:
            return False, (cx, cy)
        return True, (after['x'], after['y'])
    return True, (new_pos['x'], new_pos['y'])

print("Exploring the pond boundary starting from (19, 9)...")
# We want to find any way to reach Row 12.
# Let's walk Left along Row 9 (which is completely grass-free and open) as far as we can.
# And at each column, we will try to walk DOWN to see how far down we can go!
# We will print the maximum Y reached for each Column from 9 to 19.

for col in range(19, 8, -1):
    # Walk to (col, 9)
    print(f"Navigating to ({col}, 9)...")
    while True:
        curr = mgba.get_coordinates()
        cx, cy = curr['x'], curr['y']
        if cx == col and cy == 9:
            break
        # Move towards (col, 9)
        if cx < col: btn = "Right"
        elif cx > col: btn = "Left"
        elif cy < 9: btn = "Down"
        else: btn = "Up"
        success, pos = step(btn)
        if not success:
            print(f"Failed to reach ({col}, 9)")
            break
            
    # Try to walk DOWN as far as possible at this column
    print(f"Probing DOWN at Column {col}...")
    down_steps = 0
    while True:
        curr = mgba.get_coordinates()
        success, pos = step("Down")
        if success:
            down_steps += 1
            if pos[1] >= 12:
                print(f"SUCCESS! Reached Row {pos[1]} at Column {col}!")
                # Walk back up to Row 9
                for _ in range(down_steps):
                    step("Up")
                break
        else:
            print(f"Blocked DOWN at Row {curr['y']} for Column {col}")
            # Walk back up to Row 9
            for _ in range(down_steps):
                step("Up")
            break

print("Probing complete.")
mgba.take_screenshot()
