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

def walk_path_to_fall(path):
    # Walk the path. If we trigger a map transition or fall, coordinates or map will change.
    # Specifically, after stepping onto (26, 4), the player should fall to 1F.
    # We will check if the y coordinate suddenly changes, or if we get a map transition.
    for i, target in enumerate(path):
        tx, ty = target
        attempts = 0
        while attempts < 15:
            pos = mgba.get_coordinates()
            # If we fell, we won't be on 3F at our target coordinate anymore.
            # Usually, landing on 1F East inside the fenced room is around (26, 4) or (25, 4).
            # But the map transition itself will change the map. We can check if we successfully moved.
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
                attempts += 1
                print("Coordinates did not change. Checking if in battle or blocked...")
                flee_battle()
            else:
                attempts = 0
                # Check if we fell! If we stepped Down from (26, 3) to (26, 4), we should fall.
                # If we fell, our new_pos will not be (26, 4) on 3F anymore, or we'll be on 1F.
                # Let's see what happens.
                if tx == 26 and ty == 4 and (new_pos['x'] != 26 or new_pos['y'] != 4):
                    print(f"FALL DETECTED! Landed at position: {new_pos}")
                    return True
                
                if new_pos['x'] == tx and new_pos['y'] == ty:
                    print(f"[{i}] Arrived at ({tx}, {ty})")
                    break
    
    # Check if final position matches the last step
    final_pos = mgba.get_coordinates()
    print(f"Final position reached: {final_pos}")
    return False

# Path from (3, 5) to (26, 4) on 3F
path = []
# Start at (3, 5)
path.append((4, 5))
path.append((4, 4))
path.append((4, 3))
path.append((4, 2))
path.append((4, 1))

# Row 1 to Column 26
for x in range(5, 27):
    path.append((x, 1))

# Down Column 26 to Row 4
path.append((26, 2))
path.append((26, 3))
path.append((26, 4)) # Fall through pitfall!

print(f"Full path to pitfall length: {len(path)} steps")
walk_path_to_fall(path)
mgba.take_screenshot()
print("Execution finished!")
