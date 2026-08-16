import mgba
import time

print("--- EXITING SAFARI ZONE GATEHOUSE ---")

# We are currently at (8, 6).
# Let's walk Down until we exit the map.
# If we exit the map, get_coordinates() or a map transition will occur.
# We will do this step-by-step and inspect our coordinates.

for step in range(15):
    pos = mgba.get_coordinates()
    print(f"Step {step}: Current position = {pos}")
    
    # If the map changed, we'll see a coordinate change that doesn't match the gatehouse, or we might be at a different map.
    # In Fuchsia City, the Safari Gatehouse is at (18, 3) or around there.
    # Let's print the position.
    if pos:
        if pos['y'] > 10:
            print("We reached y > 10, walking down should exit...")
            
    # Try walking Down
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        # We bumped into something. Let's try walking Left, then Down.
        print("Bumped! Trying Left...")
        mgba.press_buttons(["Left"])
        time.sleep(0.5)

mgba.take_screenshot()
print("Final position after script:", mgba.get_coordinates())
