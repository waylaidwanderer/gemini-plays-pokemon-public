import mgba
import time
from PIL import Image, ImageChops

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
        return True
    else:
        mgba.press_buttons(["Start"])
        time.sleep(0.25)
        return False

def handle_battle_escape():
    print("ESCAPING BATTLE...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    mgba.press_buttons(["B"])
    time.sleep(1.0)

def step_one(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        if is_in_battle():
            handle_battle_escape()
            mgba.press_buttons([direction])
            time.sleep(0.4)
            pos_after = mgba.get_coordinates()
            
    # Warp/Fall check
    if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2):
        print(f"WARPED/FELL! Landed at: {pos_after}")
        return True
        
    return pos_after['x'] == target_x and pos_after['y'] == target_y

def main():
    print("go_to_2f_and_cross: Starting from (12, 11)...")
    pos = mgba.get_coordinates()
    print(f"Start coordinates: {pos}")
    
    # 1. Walk UP Column 12 directly to Row 3 (12, 3)
    if pos['x'] == 12 and pos['y'] > 3:
        print("Walking up Column 12 to Row 3...")
        for y in range(pos['y'] - 1, 2, -1):
            if not step_one("Up", 12, y):
                print(f"Failed at step 'Up' to (12, {y})")
                return
            
    pos = mgba.get_coordinates()
    # 2. Walk RIGHT along Row 3 to Column 18 (18, 3)
    if pos['y'] == 3 and pos['x'] < 18:
        print("Crossing horizontally on Row 3 to Column 18...")
        for x in range(pos['x'] + 1, 19):
            if not step_one("Right", x, 3):
                print(f"Failed at step 'Right' to ({x}, 3)")
                return
            
    pos = mgba.get_coordinates()
    # 3. Walk DOWN Column 18 to Row 10 (18, 10)
    if pos['x'] == 18 and pos['y'] < 10:
        print("Walking down Column 18 to Row 10...")
        for y in range(pos['y'] + 1, 11):
            if not step_one("Down", 18, y):
                print(f"Failed at step 'Down' to (18, {y})")
                return
            
    pos = mgba.get_coordinates()
    # 4. Walk LEFT along Row 10 to (15, 10)
    if pos['x'] == 18 and pos['y'] == 10:
        print("Walking left along Row 10 to (15, 10)...")
        for x in range(17, 14, -1):
            if not step_one("Left", x, 10):
                print(f"Failed at step 'Left' to ({x}, 10)")
                return
            
    pos = mgba.get_coordinates()
    # 5. Step DOWN onto stairs at (15, 11) to warp UP to 3F East
    if pos['x'] == 15 and pos['y'] == 10:
        print("Stepping onto stairs to warp to 3F East...")
        mgba.press_buttons(["Down"])
        time.sleep(1.5) # Wait for map transition to 3F East
        
    pos = mgba.get_coordinates()
    print(f"Landed on 3F East? Position: {pos}")
    # Landing coordinates on 3F East is (16, 11) or (15, 11)
    
    # 6. Walk to Column 20 Row 3 (20, 3)
    if pos['y'] == 11 and 14 <= pos['x'] <= 17:
        # Walk RIGHT to Column 20
        for x in range(pos['x'] + 1, 21):
            if not step_one("Right", x, 11): return
        # Walk UP Column 20 to Row 3
        for y in range(10, 2, -1):
            if not step_one("Up", 20, y): return
            
    pos = mgba.get_coordinates()
    # 7. Walk RIGHT Row 3 to Column 26 (26, 3) and drop down pitfall
    if pos['y'] == 3 and 15 <= pos['x'] < 26:
        print("Walking right to Column 26 Row 3...")
        for x in range(pos['x'] + 1, 27):
            if not step_one("Right", x, 3):
                # Check if we fell
                pos = mgba.get_coordinates()
                if pos['y'] != 3:
                    print(f"Fell through pit! Landed at: {pos}")
                    return
                    
    pos = mgba.get_coordinates()
    # 8. Walk DOWN Column 26 to Row 6 (26, 6) to trigger pitfall if we didn't fall yet
    if pos['x'] == 26 and pos['y'] == 3:
        print("Walking down Column 26 to trigger pitfall...")
        for y in range(4, 7):
            if not step_one("Down", 26, y):
                pos = mgba.get_coordinates()
                if pos['y'] != y:
                    print(f"Fell through pit at y={y}! Landed at: {pos}")
                    return
                    
    print(f"Script complete. Final coordinates: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
