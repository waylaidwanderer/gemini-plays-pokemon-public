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

def test_route():
    # Currently at (17, 11)
    # Step 1: Walk UP to (17, 7)
    print("Walking UP to (17, 7)...")
    for _ in range(4):
        pos = mgba.get_coordinates()
        print(f"Current: {pos}")
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            # Maybe a battle or obstacle
            flee_battle()
            
    # Step 2: Walk Left along Row 7 as far as possible (target Column 5)
    print("Walking Left along Row 7...")
    for col in range(16, 4, -1):
        pos = mgba.get_coordinates()
        print(f"Current: {pos} | Heading Left to column {col}")
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            # Stuck
            flee_battle()
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                print(f"Completely blocked at {pos} trying to go Left!")
                break

    # Report final position
    final_pos = mgba.get_coordinates()
    print("Final position of test:", final_pos)

if __name__ == "__main__":
    test_route()
