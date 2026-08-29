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
    print(f"Moving {direction} to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        if is_in_battle():
            handle_battle_escape()
            mgba.press_buttons([direction])
            time.sleep(0.4)
            pos_after = mgba.get_coordinates()
            
    # Pitfall check - did we fall?
    if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2):
        print(f"WARPED/FELL! Landed at: {pos_after}")
        return True
        
    return pos_after['x'] == target_x and pos_after['y'] == target_y

def main():
    print("cross_3f_from_stairs: Starting from 3F West stairs...")
    pos = mgba.get_coordinates()
    print(f"Start coordinates: {pos}")
    
    # 1. Stand at (7, 11)
    if pos['x'] == 7 and pos['y'] == 10:
        if not step_one("Down", 7, 11): return
        pos = mgba.get_coordinates()
        
    # 2. Walk Left to (5, 11)
    if pos['y'] == 11 and pos['x'] > 5:
        for x in range(pos['x'] - 1, 4, -1):
            if not step_one("Left", x, 11): return
        pos = mgba.get_coordinates()
        
    # 3. Walk Down Column 5 to Row 13 (5, 13)
    if pos['x'] == 5 and pos['y'] < 13:
        for y in range(pos['y'] + 1, 14):
            if not step_one("Down", 5, y): return
        pos = mgba.get_coordinates()
        
    # 4. Walk Left Row 13 to Column 1 (1, 13)
    if pos['y'] == 13 and pos['x'] > 1:
        for x in range(pos['x'] - 1, 0, -1):
            if not step_one("Left", x, 13): return
        pos = mgba.get_coordinates()
        
    # 5. Walk Up Column 1 to Row 6 (1, 6)
    if pos['x'] == 1 and pos['y'] > 6:
        for y in range(pos['y'] - 1, 5, -1):
            if not step_one("Up", 1, y): return
        pos = mgba.get_coordinates()
        
    # 6. Walk Right Row 6 to Column 20 (20, 6)
    if pos['y'] == 6 and pos['x'] < 20:
        for x in range(pos['x'] + 1, 21):
            if not step_one("Right", x, 6): return
        pos = mgba.get_coordinates()
        
    # 7. Walk Up Column 20 to Row 3 (20, 3)
    if pos['x'] == 20 and pos['y'] > 3:
        for y in range(pos['y'] - 1, 2, -1):
            if not step_one("Up", 20, y): return
        pos = mgba.get_coordinates()
        
    # 8. Walk Right Row 3 to Column 26 (26, 3)
    if pos['y'] == 3 and pos['x'] < 26:
        for x in range(pos['x'] + 1, 27):
            if not step_one("Right", x, 3):
                # Check if we fell early
                pos = mgba.get_coordinates()
                if pos['y'] != 3:
                    print(f"Fell through pit! Landed at: {pos}")
                    return
        pos = mgba.get_coordinates()
        
    # 9. Walk Down Column 26 to Row 6 (26, 6) to trigger pitfall
    if pos['x'] == 26 and pos['y'] == 3:
        print("Walking down Column 26 to trigger pitfall...")
        for y in range(4, 7):
            if not step_one("Down", 26, y):
                pos = mgba.get_coordinates()
                if pos['y'] != y:
                    print(f"Fell through pit at y={y}! Landed at: {pos}")
                    return
                    
    print(f"Completed! Final coordinates: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
