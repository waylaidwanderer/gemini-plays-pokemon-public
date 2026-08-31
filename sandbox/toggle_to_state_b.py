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
    print("Initial Position on 3F West:", pos)
    
    # Simple relative path from (12, 5) to the switch
    # 1. Walk Up to Row 3
    while True:
        pos = mgba.get_coordinates()
        if pos['y'] <= 3:
            break
        pos = walk_step("Up", (pos['x'], pos['y'] - 1))
        
    # 2. Walk Left to Column 4 on Row 3
    while True:
        pos = mgba.get_coordinates()
        if pos['x'] <= 4:
            break
        pos = walk_step("Left", (pos['x'] - 1, pos['y']))
        
    # 3. Walk to (4, 5)
    while True:
        pos = mgba.get_coordinates()
        if pos['y'] >= 5:
            break
        pos = walk_step("Down", (pos['x'], pos['y'] + 1))
        
    # 4. Walk to (3, 5)
    pos = mgba.get_coordinates()
    if pos['x'] == 4 and pos['y'] == 5:
        pos = walk_step("Left", (3, 5))
        
    # 5. Walk to (3, 6)
    pos = mgba.get_coordinates()
    if pos['x'] == 3 and pos['y'] == 5:
        pos = walk_step("Down", (3, 6))
        
    # 6. Walk to (2, 6)
    pos = mgba.get_coordinates()
    if pos['x'] == 3 and pos['y'] == 6:
        pos = walk_step("Left", (2, 6))
        
    pos = mgba.get_coordinates()
    if pos['x'] == 2 and pos['y'] == 6:
        # Now stand at (2, 6) and face UP
        print("Facing Up to look at the switch...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        
        # Toggle switch (4 A-presses)
        print("Toggling Mewtwo Switch...")
        for press in range(1, 5):
            print(f"A-press {press}...")
            mgba.press_buttons(["A"])
            time.sleep(2.0)
            
        print("Successfully toggled switch to State B!")
    else:
        print("Failed to reach (2, 6)!")
    
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
