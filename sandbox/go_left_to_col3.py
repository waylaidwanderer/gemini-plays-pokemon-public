import mgba
import time

print("Running go_left_to_col3.py...")

# Path to walk Left 17 steps from (20, 23) to (3, 23)
path = ["Left"] * 17

def walk_path(path):
    for i, direction in enumerate(path):
        print(f"\n--- Step {i+1}/{len(path)}: Moving {direction} ---")
        
        attempts = 0
        while attempts < 15:
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
                # Coordinates did not change! Could be a wild battle or bump.
                # Let's check if we bumped into a wall by doing a quick test, or if it is a battle.
                print("We did not move! Attempting to run from battle...")
                mgba.press_buttons(["B", "sleep 200", "Down", "sleep 200", "Right", "sleep 200", "A"])
                time.sleep(1.8)
                
                post_battle_pos = mgba.get_coordinates()
                if post_battle_pos != start_pos:
                    print(f"Position changed after run attempt: {post_battle_pos}")
                    break
                
                attempts += 1
        else:
            print("ERROR: Stuck! Failed to move after 15 attempts.")
            return False
            
    print("\nPath traversal complete!")
    return True

success = walk_path(path)
if success:
    print(f"Final coordinates: {mgba.get_coordinates()}")
else:
    print("Path traversal failed!")
