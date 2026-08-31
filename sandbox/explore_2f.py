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

def walk_step(direction, target):
    pos = mgba.get_coordinates()
    cx, cy = pos['x'], pos['y']
    print(f"Current: ({cx}, {cy}) | Pressing {direction} to go to {target}")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        # Check for battle
        print("No movement, checking for battle...")
        flee_battle()
        new_pos = mgba.get_coordinates()
    return new_pos

def main():
    pos = mgba.get_coordinates()
    print("Initial Position on 2F West:", pos)
    
    # Walk DOWN Column 10 as far as possible
    while True:
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        
        # Try to step Down
        new_pos = walk_step("Down", (cx, cy + 1))
        if new_pos == pos:
            print("Blocked from going Down!")
            break
            
    # Walk Left as far as possible
    while True:
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        
        # Try to step Left
        new_pos = walk_step("Left", (cx - 1, cy))
        if new_pos == pos:
            print("Blocked from going Left!")
            break
            
    print("Final Position on 2F West:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
