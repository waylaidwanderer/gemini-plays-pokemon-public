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
    
    # 1. Right to Column 6
    if pos['x'] == 5 and pos['y'] == 11:
        pos = walk_step("Right", (6, 11))
        
    # 2. Up Column 6 to Row 2
    while pos['y'] > 2:
        pos = walk_step("Up", (pos['x'], pos['y'] - 1))
        
    # 3. Explore Right along Row 2 as far as possible (up to Column 28)
    print("Starting horizontal exploration along Row 2...")
    for col in range(7, 29):
        pos_before = mgba.get_coordinates()
        pos_after = walk_step("Right", (col, 2))
        if pos_after == pos_before:
            print(f"Blocked at {pos_before} trying to go to ({col}, 2)")
            break
            
    print("Final position after exploration:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
