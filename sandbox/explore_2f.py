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
    print("Initial Position on 2F:", pos)
    
    # 1. Walk Down Column 10 to Row 6
    while pos['y'] < 6:
        pos = walk_step("Down", (pos['x'], pos['y'] + 1))
        
    # 2. Explore Right along Row 6 as far as possible
    print("Exploring Right along Row 6...")
    for col in range(11, 29):
        pos_before = mgba.get_coordinates()
        pos_after = walk_step("Right", (col, 6))
        if pos_after == pos_before:
            print(f"Blocked at {pos_before} trying to go to ({col}, 6)")
            break
            
    print("Final position after Row 6 exploration:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
