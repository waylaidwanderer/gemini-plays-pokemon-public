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

def search_up_stairs():
    # Currently at (22, 6)
    # We will walk and test tiles in the north to find the stairs UP to 2F East.
    # Note: some tiles are blocked by rubble/walls, so we use a robust path and test open ones.
    
    test_path = [
        (22, 5), (22, 4), (22, 3), (22, 2), (22, 1),
        (23, 1), (24, 1), (25, 1), (26, 1), (27, 1), (28, 1),
        (28, 2), (27, 2), (26, 2), (25, 2), (24, 2), (23, 2)
    ]
    
    for target in test_path:
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        
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
            # If we warped, map/coordinates will change drastically
            if new_pos != pos and abs(new_pos['x'] - pos['x']) + abs(new_pos['y'] - pos['y']) > 1:
                print("WARPED! New position:", new_pos)
                return True
                
            if new_pos == pos:
                print("Failed to move, checking for battle...")
                flee_battle()
                post_flee = mgba.get_coordinates()
                if post_flee == pos:
                    print(f"Blocked at {pos} trying to go to {target}")

    print("Search completed. No stairs found.")
    return False

if __name__ == "__main__":
    search_up_stairs()
