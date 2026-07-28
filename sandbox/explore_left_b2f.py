import mgba
import time

def run_away():
    print("Encountered obstacle or battle! Attempting to run away...")
    # Press Down, Right, A to select RUN
    mgba.press_buttons(["Down", "Right", "A", "sleep 1000"])
    # Press A to dismiss "Got away safely!"
    mgba.press_buttons(["A", "sleep 500"])

def walk_step(direction):
    old_pos = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 350"])
    new_pos = mgba.get_coordinates()
    
    # If coordinates didn't change, we might be in a battle or hit a wall
    if old_pos == new_pos:
        # Check if we are in battle by trying to run
        run_away()
        # Try walking again
        mgba.press_buttons([direction, "sleep 350"])
        new_pos = mgba.get_coordinates()
    return new_pos

def main():
    print("Starting exploration to the left side of B2F...")
    
    # Current position is (24, 21)
    # We want to walk:
    # 1. Down 3 steps to (24, 24)
    # 2. Left 3 steps to (21, 24)
    # 3. Up 1 step to (21, 23)
    # 4. Left 7 steps to (14, 23)
    
    path = ["Down", "Down", "Down", "Left", "Left", "Left", "Up", "Left", "Left", "Left", "Left", "Left", "Left", "Left"]
    
    for i, step in enumerate(path):
        pos = walk_step(step)
        print(f"Step {i+1} ({step}): Coordinates={pos}")
        
    img = mgba.take_screenshot()
    print(f"Final Screenshot: {img}")

if __name__ == "__main__":
    main()
