import mgba
import time

def step_to_test(direction, tx, ty):
    pos = mgba.get_coordinates()
    if pos['x'] == tx and pos['y'] == ty:
        return True
        
    print(f"At {pos}. Attempting to move {direction} to ({tx}, {ty})...")
    mgba.press_buttons([direction])
    time.sleep(0.5)
    new_pos = mgba.get_coordinates()
    
    if new_pos == pos:
        print("Did not move. Pressing direction again...")
        mgba.press_buttons([direction])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        
    print(f"Result position: {new_pos}")
    return new_pos['x'] == tx and new_pos['y'] == ty

def main():
    print("Exploring south-west balcony door from (3, 11)...")
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    
    # We are at (3, 11). Walk to (2, 12)
    path = [
        ("Left", 2, 11),
        ("Down", 2, 12),
    ]
    for d, tx, ty in path:
        if not step_to_test(d, tx, ty):
            print("Failed to reach (2, 12).")
            mgba.take_screenshot()
            return
            
    # Now walk DOWN as far as possible to find the door
    print("Walking Down vertically from (2, 12)...")
    curr_y = 12
    for i in range(10):
        curr_y += 1
        pos_before = mgba.get_coordinates()
        print(f"Step {i+1}: Trying Down to row {curr_y}...")
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
        pos_after = mgba.get_coordinates()
        print("Position after Down:", pos_after)
        
        if pos_after == pos_before:
            # We are blocked! Let's check if there's a door next to us or if we can go Left/Right
            print("Blocked walking Down. Checking if we can walk Left/Right to find a doorway...")
            mgba.take_screenshot()
            break
            
        # Check if map transitioned
        # (The system note format handles map transition, but let's check coordinates)
        if pos_after['y'] < 5: 
            print("Map Transition Detected! Landed at:", pos_after)
            mgba.take_screenshot()
            return

if __name__ == "__main__":
    main()
