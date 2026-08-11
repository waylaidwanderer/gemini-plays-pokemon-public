import mgba
import time

print("Running walk_safari.py to go to the Secret House...")

# From (11, 12) in Area 3 (West):
# 8 steps Down to (11, 20)
# 8 steps Left to (3, 20)
# 1 step Up to (3, 19) (Secret House door)

path = ["Down"] * 8 + ["Left"] * 8 + ["Up"] * 1

def walk_path(path):
    for i, direction in enumerate(path):
        print(f"\n--- Step {i+1}/{len(path)}: Moving {direction} ---")
        
        attempts = 0
        while attempts < 20:
            start_pos = mgba.get_coordinates()
            print(f"Current coordinates before move: {start_pos}")
            
            # Press direction button
            mgba.press_buttons([direction])
            time.sleep(0.6)
            
            new_pos = mgba.get_coordinates()
            print(f"Coordinates after move attempt: {new_pos}")
            
            if new_pos != start_pos:
                print(f"Successfully moved to {new_pos}")
                break
            else:
                # Coordinates did not change! Could be a wild battle.
                print("We did not move! Attempting to clear text/escape battle...")
                # Escape sequence: B to dismiss any dialogue/submenus, then Down, Right, A to RUN
                mgba.press_buttons(["B", "sleep 200", "Down", "sleep 200", "Right", "sleep 200", "A"])
                time.sleep(1.8) # Wait for escape animation or text scroll
                attempts += 1
        else:
            print("ERROR: Stuck! Failed to move after 20 attempts.")
            return False
            
    print("\nPath traversal complete!")
    return True

success = walk_path(path)
if success:
    final_coords = mgba.get_coordinates()
    print(f"Final coordinates: {final_coords}")
else:
    print("Path traversal failed!")
