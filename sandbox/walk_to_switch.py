import mgba
import time

def flee_battle():
    print("Attempting to flee battle...")
    # Press B a few times to dismiss potential text or submenus
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    
    # Try to navigate to RUN and press A
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5) # Wait for escape message and transition back to overworld
    
    # Press B / A to clear "Escaped safely!" text
    mgba.press_buttons(["B", "B"])
    time.sleep(0.5)

def walk_path(path):
    for i, target in enumerate(path):
        tx, ty = target
        attempts = 0
        while attempts < 15:
            pos = mgba.get_coordinates()
            if pos['x'] == tx and pos['y'] == ty:
                print(f"[{i}] Successfully at target ({tx}, {ty})")
                break
            
            # Determine direction to move
            dx = tx - pos['x']
            dy = ty - pos['y']
            
            if dx > 0:
                direction = "Right"
            elif dx < 0:
                direction = "Left"
            elif dy > 0:
                direction = "Down"
            elif dy < 0:
                direction = "Up"
            else:
                break
            
            print(f"Moving {direction} from {pos} to reach ({tx}, {ty}). Attempt {attempts+1}")
            mgba.press_buttons([direction])
            time.sleep(0.6)
            
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                # We didn't move! Could be blocked or in battle.
                attempts += 1
                print("Coordinates did not change. Checking if in battle or blocked...")
                # Let's try to flee battle just in case
                flee_battle()
            else:
                # We moved!
                attempts = 0 # reset attempts
                if new_pos['x'] == tx and new_pos['y'] == ty:
                    print(f"[{i}] Arrived at ({tx}, {ty})")
                    break

# Generate path from (25, 12) to (3, 5) via Column 26, Row 1, Column 4, Row 5
path = []
# Start at (25, 12)
# Step 1: Walk to Column 26
path.append((26, 12))
# Step 2: Walk UP Column 26 to Row 1
for y in range(11, 0, -1):
    path.append((26, y))
# Step 3: Walk Left along Row 1 to Column 4
for x in range(25, 3, -1):
    path.append((x, 1))
# Step 4: Walk Down Column 4 to Row 5
for y in range(2, 6):
    path.append((4, y))
# Step 5: Walk Left to Column 3
path.append((3, 5))

print(f"Full path length: {len(path)} steps")
walk_path(path)
mgba.take_screenshot()
print("Walking complete!")
