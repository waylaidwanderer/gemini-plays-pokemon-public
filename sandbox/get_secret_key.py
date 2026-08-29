from PIL import Image, ImageChops
import mgba
import time

def is_in_battle():
    img1_path = mgba.take_screenshot()
    img1 = Image.open(img1_path)
    mgba.press_buttons(["Start"])
    time.sleep(0.25)
    img2_path = mgba.take_screenshot()
    img2 = Image.open(img2_path)
    diff = ImageChops.difference(img1, img2)
    bbox = diff.getbbox()
    if bbox is None:
        print("is_in_battle: TRUE")
        return True
    else:
        print("is_in_battle: FALSE. Closing menu...")
        mgba.press_buttons(["Start"])
        time.sleep(0.25)
        return False

def handle_battle_escape():
    print("handle_battle_escape: ESCAPING BATTLE...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    mgba.press_buttons(["B"])
    time.sleep(1.0)

def move_safe_battle(step, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"move_safe_battle: Moving '{step}' to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([step])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    # Check if map transitioned or we fell (coordinates shift out of range or map changes)
    # The player falls to 1F East inside the fenced room (around (26, 4) or (25, 6))
    # We can detect if we fell by checking if the coordinate y-position changed unexpectedly 
    # or if we are no longer on 3F (which has y up to 18, but 1F East is different)
    # Actually, we can check if y coordinate went to 1F East
    
    attempts = 0
    while (pos_after['x'] != target_x or pos_after['y'] != target_y) and attempts < 6:
        # Check if we fell (our position changed significantly or we are not at target but didn't hit a wall)
        if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2):
            print(f"move_safe_battle: Significant coordinate shift detected! Fell or warped? Current: {pos_after}")
            return True
            
        if pos_before == pos_after:
            print("move_safe_battle: Position did not change. Checking battle...")
            if is_in_battle():
                handle_battle_escape()
            else:
                print("move_safe_battle: Turn-in-place or wall. Retrying...")
        else:
            print(f"move_safe_battle: Moved but to {pos_after} instead of target ({target_x}, {target_y}). Checking battle...")
            if is_in_battle():
                handle_battle_escape()
            else:
                print("move_safe_battle: Unexpected overworld movement.")
                
        print(f"move_safe_battle: Retrying step '{step}'...")
        mgba.press_buttons([step])
        time.sleep(0.4)
        pos_before = pos_after
        pos_after = mgba.get_coordinates()
        attempts += 1
        
    return pos_after['x'] == target_x and pos_after['y'] == target_y

def main():
    print("get_secret_key: Executing full path starting from 3F West...")
    
    pos = mgba.get_coordinates()
    print(f"Start coordinates: {pos}")
    
    # If we are on 3F:
    # Walk Right along Row 11 to Column 10
    if pos['y'] == 11 and pos['x'] <= 10:
        for x in range(pos['x'] + 1, 11):
            if not move_safe_battle("Right", x, 11): return
            
    pos = mgba.get_coordinates()
    # Walk Up Column 10 to Row 6
    if pos['x'] == 10 and pos['y'] > 6:
        for y in range(pos['y'] - 1, 5, -1):
            if not move_safe_battle("Up", 10, y): return
            
    pos = mgba.get_coordinates()
    # Walk Right Row 6 to Column 19
    if pos['y'] == 6 and pos['x'] < 19:
        for x in range(pos['x'] + 1, 20):
            if not move_safe_battle("Right", x, 6): return
            
    pos = mgba.get_coordinates()
    # Walk Up Column 19 to Row 4
    if pos['x'] == 19 and pos['y'] > 4:
        for y in range(pos['y'] - 1, 3, -1):
            if not move_safe_battle("Up", 19, y): return
            
    pos = mgba.get_coordinates()
    # Walk Right to (20, 4) then UP to (20, 3)
    if pos['x'] == 19 and pos['y'] == 4:
        if not move_safe_battle("Right", 20, 4): return
        if not move_safe_battle("Up", 20, 3): return
        
    pos = mgba.get_coordinates()
    # Walk Right along Row 3 to Column 26
    if pos['y'] == 3 and pos['x'] < 26:
        for x in range(pos['x'] + 1, 27):
            # Check if we fall while walking to Row 3 Column 26
            if not move_safe_battle("Right", x, 3):
                # We might have fallen
                pos = mgba.get_coordinates()
                if pos['y'] != 3:
                    print(f"Fell through pit! Landed at: {pos}")
                    break
                    
    pos = mgba.get_coordinates()
    # If we are still on Row 3 Column 26, walk DOWN to Row 6 to trigger pitfall
    if pos['x'] == 26 and pos['y'] == 3:
        for y in range(4, 7):
            if not move_safe_battle("Down", 26, y):
                pos = mgba.get_coordinates()
                if pos['y'] != y:
                    print(f"Fell through pit at y={y}! Landed at: {pos}")
                    break
                    
    # Now we should have fallen to 1F East inside the fenced room!
    # Let's verify our coordinates
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print(f"Landed on 1F East: {pos}")
    
    # 1F East Fenced Room to stairs at (22, 2)
    # Walk to (21, 2) then RIGHT onto stairs at (22, 2)
    # The stairs can land us at (26, 4) or similar depending on where we dropped.
    # Let's navigate to (21, 2)
    if pos['y'] > 2:
        for y in range(pos['y'] - 1, 1, -1):
            if not move_safe_battle("Up", pos['x'], y): return
            
    pos = mgba.get_coordinates()
    if pos['x'] > 21:
        for x in range(pos['x'] - 1, 20, -1):
            if not move_safe_battle("Left", x, pos['y']): return
            
    pos = mgba.get_coordinates()
    if pos['y'] != 2:
        # Move vertically to Row 2
        if pos['y'] < 2:
            if not move_safe_battle("Down", pos['x'], 2): return
        elif pos['y'] > 2:
            if not move_safe_battle("Up", pos['x'], 2): return
            
    pos = mgba.get_coordinates()
    print(f"Standing at {pos}, ready to step onto stairs at (22, 2)...")
    # Step RIGHT onto the stairs at (22, 2) to warp DOWN to B1F East
    if not move_safe_battle("Right", 22, 2):
        pos = mgba.get_coordinates()
        if pos['x'] == 22 and pos['y'] == 2:
            print("Successfully warped down to B1F East!")
            
    # Allow warp animation to finish
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print(f"Coordinates after B1F East warp: {pos}")
    
    # On B1F East:
    # 1. Walk down to (22, 4)
    if pos['y'] < 4:
        for y in range(pos['y'] + 1, 5):
            if not move_safe_battle("Down", 22, y): return
            
    pos = mgba.get_coordinates()
    # 2. Walk LEFT along Row 4 to Column 19 (19, 4)
    if pos['x'] > 19:
        for x in range(pos['x'] - 1, 18, -1):
            if not move_safe_battle("Left", x, 4): return
            
    pos = mgba.get_coordinates()
    # 3. Walk DOWN to (19, 5)
    if pos['y'] == 4:
        if not move_safe_battle("Down", 19, 5): return
        
    pos = mgba.get_coordinates()
    # 4. Walk LEFT along Row 5 all the way to B1F West (1, 5)
    if pos['y'] == 5 and pos['x'] > 1:
        for x in range(pos['x'] - 1, 0, -1):
            if not move_safe_battle("Left", x, 5): return
            
    pos = mgba.get_coordinates()
    print(f"At B1F West Secret Key Room: {pos}")
    
    # Retrieve the Secret Key at (1, 4)
    print("Facing UP towards Secret Key...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Retrieving Secret Key...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Dismiss dialogue text boxes
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print(f"Final coordinates: {pos}")

if __name__ == "__main__":
    main()
