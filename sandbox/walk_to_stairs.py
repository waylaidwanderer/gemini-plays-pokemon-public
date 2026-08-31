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

def explore():
    # Currently at (11, 8)
    # Step 1: Walk UP Column 11 to Row 2: (11, 7) -> (11, 6) -> (11, 5) -> (11, 4) -> (11, 3) -> (11, 2)
    print("Walking UP Column 11 to Row 2...")
    for row in range(7, 1, -1):
        while True:
            pos = mgba.get_coordinates()
            cx, cy = pos['x'], pos['y']
            if cy == row:
                break
            print(f"Current: ({cx}, {cy}) | Heading UP to row {row}")
            mgba.press_buttons(["Up"])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                print("Stuck heading UP! Fleeing/clearing...")
                flee_battle()
                
    # Step 2: Try to walk Left along Row 2 towards Column 5
    print("Attempting to walk Left along Row 2...")
    for col in range(10, 4, -1):
        while True:
            pos = mgba.get_coordinates()
            cx, cy = pos['x'], pos['y']
            if cx == col:
                break
            print(f"Current: ({cx}, {cy}) | Heading Left to column {col}")
            mgba.press_buttons(["Left"])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                print("Stuck heading Left! Fleeing/clearing...")
                flee_battle()
                post_flee = mgba.get_coordinates()
                if post_flee == pos:
                    print(f"Blocked trying to go Left at {pos}!")
                    return

    # Step 3: If we made it to Column 5, walk DOWN to the stairs at (5, 10)
    print("Made it to Column 5! Walking DOWN to (5, 10)...")
    for row in range(3, 11):
        while True:
            pos = mgba.get_coordinates()
            cx, cy = pos['x'], pos['y']
            if cy == row:
                break
            print(f"Current: ({cx}, {cy}) | Heading DOWN to row {row}")
            mgba.press_buttons(["Down"])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                print("Stuck heading DOWN! Fleeing/clearing...")
                flee_battle()

    final_pos = mgba.get_coordinates()
    print("Reached final position:", final_pos)

if __name__ == "__main__":
    explore()
