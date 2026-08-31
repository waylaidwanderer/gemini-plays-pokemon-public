import mgba
import time

def flee_battle():
    print("Wild battle! Fleeing...")
    # Clean up screen text
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    # Select RUN
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    # Clear "Got away safely!"
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def search():
    # Currently at (21, 3)
    # We will walk to Column 26 and test stepping on various rows
    # to find the pitfall trap.
    
    path = [
        # Walk back to (26, 3)
        (22, 3), (23, 3), (24, 3), (25, 3), (26, 3),
        # Test Column 26 Row 2
        (26, 2),
        # Test Column 26 Row 1
        (26, 1),
        # Walk to Column 27 Row 1
        (27, 1),
        # Test Column 27 Row 2
        (27, 2),
        # Test Column 27 Row 3
        (27, 3),
        # Test Column 27 Row 4
        (27, 4),
        # Test Column 27 Row 5
        (27, 5),
        # Test Column 26 Row 6
        (26, 6),
        # Test Column 26 Row 7
        (26, 7),
    ]
    
    for target in path:
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        
        # Get direction
        direction = None
        if target[0] > cx: direction = "Right"
        elif target[0] < cx: direction = "Left"
        elif target[1] > cy: direction = "Down"
        elif target[1] < cy: direction = "Up"
        
        if direction is not None:
            print(f"Current: ({cx}, {cy}) | Stepping to: {target} via {direction}")
            mgba.press_buttons([direction])
            time.sleep(0.6)
            
            new_pos = mgba.get_coordinates()
            # If coordinates changed drastically, we fell!
            if new_pos != pos and abs(new_pos['x'] - pos['x']) + abs(new_pos['y'] - pos['y']) > 1:
                print("WARPED! Fell through pitfall! New position:", new_pos)
                return True
                
            # If we didn't move but no battle, maybe wall
            if new_pos == pos:
                print("Failed to move, checking for battle...")
                flee_battle()
                post_flee = mgba.get_coordinates()
                if post_flee == pos:
                    print(f"Blocked at {pos} trying to go to {target} (physical wall/obstacle)")
                    
    print("Search completed. No pitfall triggered.")
    return False

if __name__ == "__main__":
    search()
