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
    print("Initial Position on 3F East:", pos)
    
    # 1. Walk to stairs at (22, 1) and warp DOWN to 2F East
    # Current is (23, 3)
    if pos['x'] == 23 and pos['y'] == 3:
        pos = walk_step("Left", (22, 3))
        
    if pos['x'] == 22 and pos['y'] == 3:
        pos = walk_step("Up", (22, 2))
        
    if pos['x'] == 22 and pos['y'] == 2:
        print("Stepping UP onto the stairs (22, 1)...")
        mgba.press_buttons(["Up"])
        time.sleep(1.5) # Wait for warp
        
    pos = mgba.get_coordinates()
    print("Position after warp attempt:", pos)
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
