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
    # Currently at (27, 5)
    # Walk and test ALL pink checkered tiles in the Scientist room
    path = [
        # Row 5
        (28, 5), (27, 5), (26, 5), (25, 5),
        # Row 4
        (25, 4), (26, 4), (27, 4), (28, 4),
        # Row 3
        (27, 3), (26, 3), (25, 3), (24, 3), (23, 3),
        # Row 6 & 7 on Column 28
        (28, 5), (28, 6), (28, 7)
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
                
            # If we didn't move but no battle, check for battle
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
