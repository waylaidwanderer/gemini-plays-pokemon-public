from PIL import Image, ImageChops
import mgba
import time

def is_in_battle():
    # Take first screenshot
    img1_path = mgba.take_screenshot()
    img1 = Image.open(img1_path)
    
    # Press Start
    mgba.press_buttons(["Start"])
    time.sleep(0.15)
    
    # Take second screenshot
    img2_path = mgba.take_screenshot()
    img2 = Image.open(img2_path)
    
    # Compare images
    diff = ImageChops.difference(img1, img2)
    bbox = diff.getbbox()
    if bbox is None:
        # Identical: must be a battle or dialogue text
        print("is_in_battle: TRUE (No screen change on Start)")
        return True
    else:
        # Different: menu opened. Close it!
        print("is_in_battle: FALSE (Screen changed on Start). Closing menu...")
        mgba.press_buttons(["Start"])
        time.sleep(0.15)
        return False

def handle_battle_escape():
    print("handle_battle_escape: Initiating battle run...")
    # Press B first to clear any initial text like "Wild Ponyta appeared!"
    mgba.press_buttons(["B"])
    time.sleep(0.3)
    
    # Press Down, Right, A to select RUN
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    
    # Press B to dismiss "Got away safely!" or any other battle end screen
    mgba.press_buttons(["B"])
    time.sleep(0.5)

def move_safe_battle(step, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"move_safe_battle: Moving '{step}' towards ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([step])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    attempts = 0
    while (pos_after['x'] != target_x or pos_after['y'] != target_y) and attempts < 5:
        if pos_before == pos_after:
            print("move_safe_battle: Position did not change. Checking for battle...")
            if is_in_battle():
                handle_battle_escape()
            else:
                # We hit a wall!
                print(f"move_safe_battle: Hit a solid wall at ({pos_after['x']}, {pos_after['y']}) trying to move '{step}'!")
                return False
        else:
            print(f"move_safe_battle: Unexpected position {pos_after}. Checking for battle...")
            if is_in_battle():
                handle_battle_escape()
            else:
                print("move_safe_battle: In overworld but coordinate mismatch.")
        
        print(f"move_safe_battle: Retrying move '{step}' to target ({target_x}, {target_y})...")
        mgba.press_buttons([step])
        time.sleep(0.4)
        pos_after = mgba.get_coordinates()
        attempts += 1
        
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        print(f"move_safe_battle: Arrived at target: {pos_after}")
        return True
    else:
        print(f"move_safe_battle: Failed to reach target ({target_x}, {target_y}). Final: {pos_after}")
        return False

def toggle_switch_to_state_b():
    print("toggle_switch_to_state_b: Standing at (2, 12) facing UP. Toggling...")
    # Step-by-step switch sequence
    # 1. Interact with statue
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # 2. Advance to Yes/No prompt
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # 3. Select YES
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # 4. Dismiss "Who wouldn't?" and back to overworld
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    print("toggle_switch_to_state_b: Switch toggled to State B!")

def solve():
    # We are currently at (6, 13)
    pos = mgba.get_coordinates()
    print(f"solve: Starting at {pos}")
    
    # 1. Walk to (1, 10)
    # Walk left along Row 13 to Column 1
    for x in [5, 4, 3, 2, 1]:
        if not move_safe_battle("Left", x, 13):
            return
            
    # Walk up Column 1 to Row 10
    for y in [12, 11, 10]:
        if not move_safe_battle("Up", 1, y):
            return
            
    # 2. Test the gate at (1, 9)
    print("solve: Testing if gate at (1, 9) is open (State B)...")
    success = move_safe_battle("Up", 1, 9)
    if not success:
        print("solve: Gate is CLOSED. We are in State A. Going to toggle switch...")
        # Walk to (2, 12)
        for y in [11, 12]:
            move_safe_battle("Down", 1, y)
        move_safe_battle("Right", 2, 12)
        
        # Toggle switch to State B
        toggle_switch_to_state_b()
        
        # Walk back to (1, 10)
        move_safe_battle("Left", 1, 12)
        for y in [11, 10]:
            move_safe_battle("Up", 1, y)
            
        # Try walking through the gate again
        print("solve: Re-testing gate at (1, 9)...")
        if not move_safe_battle("Up", 1, 9):
            print("solve: CRITICAL ERROR - Gate is still closed after toggle!")
            return
            
    # 3. Walk UP Column 1 to Row 6
    for y in [8, 7, 6]:
        if not move_safe_battle("Up", 1, y):
            return
            
    # 4. Walk RIGHT on Row 6 to Column 21
    for x in range(2, 22):
        if not move_safe_battle("Right", x, 6):
            return
            
    # 5. Walk LEFT to Column 19
    for x in [20, 19]:
        if not move_safe_battle("Left", x, 6):
            return
            
    # 6. Walk UP Column 19 to Row 3
    for y in [5, 4, 3]:
        if not move_safe_battle("Up", 19, y):
            return
            
    # 7. Walk RIGHT on Row 3 to Column 26
    for x in range(20, 27):
        if not move_safe_battle("Right", x, 3):
            return
            
    # 8. Drop through the pitfall!
    print("solve: Arrived at pitfall entrance (26, 3). Stepping into pitfall...")
    mgba.press_buttons(["Right"])
    time.sleep(1.0)
    mgba.press_buttons(["Down"])
    time.sleep(1.0)
    print(f"solve: Final position after drop: {mgba.get_coordinates()}")

if __name__ == "__main__":
    solve()
