import sys
import time
import os
import mgba

def get_pos():
    pos = mgba.get_coordinates()
    if pos is None:
        return None
    return pos['x'], pos['y']

def walk_step(direction):
    mgba.press_buttons([direction, "sleep 350"])

def enter_center_and_open_pc():
    print("Step 1: Walking to Pokemon Center from overworld...")
    # Walk to (19, 28)
    walk_step("Down") # 24, 28
    for _ in range(5):
        walk_step("Left") # to 19, 28
    
    # Enter center
    print("Step 2: Entering Pokemon Center...")
    walk_step("Up") # to 19, 27 -> transition
    time.sleep(2.0)
    
    pos = get_pos()
    print(f"Inside Pokemon Center? Coordinates: {pos}")
    if pos is None:
        print("Failed to get coordinates, taking screenshot...")
        mgba.take_screenshot()
        return
        
    # Walk to column 13
    print("Step 3: Navigating to column 13...")
    current_x = pos[0]
    while current_x < 13:
        walk_step("Right")
        new_pos = get_pos()
        if new_pos is None:
            print("Encountered collision or menu inside?")
            break
        current_x = new_pos[0]
        print(f"Current x: {current_x}")
        
    # Walk to row 4
    print("Step 4: Navigating to row 4...")
    pos = get_pos()
    if pos is not None:
        current_y = pos[1]
        while current_y > 4:
            walk_step("Up")
            new_pos = get_pos()
            if new_pos is None:
                break
            current_y = new_pos[1]
            print(f"Current y: {current_y}")
            
    # Face UP to face the PC
    print("Step 5: Facing UP to face PC...")
    walk_step("Up")
    time.sleep(0.5)
    
    pos = get_pos()
    print(f"Standing at: {pos}")
    
    # Take screenshot of the PC setup
    mgba.take_screenshot()
    
    # Step 6: Interact with PC
    print("Step 6: Pressing A to boot PC...")
    mgba.press_buttons(["A", "sleep 1000"])
    mgba.take_screenshot()
    
    # Advance dialogue "ACE booted up the PC."
    print("Step 7: Advancing boot dialogue...")
    mgba.press_buttons(["A", "sleep 1000"])
    mgba.take_screenshot()
    
    # Select ACE's PC (the first option)
    print("Step 8: Selecting ACE's PC...")
    mgba.press_buttons(["A", "sleep 1000"])
    mgba.take_screenshot()
    
    # Select WITHDRAW ITEM (the first option)
    print("Step 9: Selecting WITHDRAW ITEM...")
    mgba.press_buttons(["A", "sleep 1000"])
    mgba.take_screenshot()

if __name__ == "__main__":
    enter_center_and_open_pc()
