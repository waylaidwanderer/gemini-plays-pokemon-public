import mgba
import time

def is_in_battle():
    img1_path = mgba.take_screenshot()
    img1 = Image.open(img1_path)
    mgba.press_buttons(["Start"])
    time.sleep(0.2)
    img2_path = mgba.take_screenshot()
    img2 = Image.open(img2_path)
    diff = ImageChops.difference(img1, img2)
    bbox = diff.getbbox()
    if bbox is None:
        return True
    else:
        mgba.press_buttons(["Start"])
        time.sleep(0.2)
        return False

def handle_battle_escape():
    print("handle_battle_escape: ESCAPING BATTLE!")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    mgba.press_buttons(["B"])
    time.sleep(1.0)

def move_safe_battle(step, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"move_safe_battle: Attempting to move '{step}' to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([step])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    attempts = 0
    while (pos_after['x'] != target_x or pos_after['y'] != target_y) and attempts < 6:
        if pos_before == pos_after:
            print("move_safe_battle: Position did not change. Checking for battle...")
            # Simple check or sleep
            time.sleep(0.5)
            mgba.press_buttons(["B"]) # clear potential battle screen
            time.sleep(0.5)
        else:
            print(f"move_safe_battle: Moved to {pos_after} instead of target ({target_x}, {target_y}).")
                
        print(f"move_safe_battle: Retrying step '{step}'...")
        mgba.press_buttons([step])
        time.sleep(0.4)
        pos_before = pos_after
        pos_after = mgba.get_coordinates()
        attempts += 1
        
    arrived = (pos_after['x'] == target_x and pos_after['y'] == target_y)
    print(f"move_safe_battle: Arrived: {arrived}. Final position: {pos_after}")
    return arrived

def main():
    # We start at (19, 7)
    pos = mgba.get_coordinates()
    print(f"Starting toggle_once from {pos}")
    
    # 1. Walk UP Column 19 to (19, 6)
    move_safe_battle("Up", 19, 6)
    
    # 2. Walk LEFT Row 6 to (10, 6)
    for x in range(18, 9, -1):
        move_safe_battle("Left", x, 6)
        
    # 3. Walk DOWN Column 10 to (10, 10)
    for y in [7, 8, 9, 10]:
        move_safe_battle("Down", 10, y)
        
    # 4. Walk LEFT to (1, 10)
    for x in range(9, 0, -1):
        move_safe_battle("Left", x, 10)
        
    # 5. Walk to (2, 12)
    move_safe_battle("Down", 1, 11)
    move_safe_battle("Down", 1, 12)
    move_safe_battle("Right", 2, 12)
    
    # 6. Toggle Switch (this will toggle to State A!)
    print("At switch. Toggling to State A...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # 7. Walk back to (1, 10)
    move_safe_battle("Left", 1, 12)
    move_safe_battle("Up", 1, 11)
    move_safe_battle("Up", 1, 10)
    
    # 8. Walk back to Column 10 Row 10
    for x in range(2, 11):
        move_safe_battle("Right", x, 10)
        
    # 9. Walk back UP to Row 6
    for y in [9, 8, 7, 6]:
        move_safe_battle("Up", 10, y)
        
    print(f"Finished toggle_once. Current position: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
