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
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    mgba.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A", "sleep 1000", "B"])
    time.sleep(1.5)

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
        else:
            time.sleep(0.2)
            mgba.press_buttons([direction])
            time.sleep(0.4)
            pos_after = mgba.get_coordinates()
            
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return True
    return False

def walk_path(coords):
    for target_x, target_y in coords:
        pos_before = mgba.get_coordinates()
        dx = target_x - pos_before['x']
        dy = target_y - pos_before['y']
        
        direction = ""
        if dx > 0: direction = "Right"
        elif dx < 0: direction = "Left"
        elif dy > 0: direction = "Down"
        elif dy < 0: direction = "Up"
        
        if not step_one(direction, target_x, target_y):
            return False
    return True

def main():
    print("probe_balcony_v3: Starting...")
    pos = mgba.get_coordinates()
    print(f"Current pos: {pos}")
    
    # 1. Walk from (10, 16) up to (12, 12)
    setup_path = [
        (10, 15), (10, 14), (10, 13), (10, 12),
        (11, 12), (12, 12)
    ]
    if not walk_path(setup_path):
        print("Failed to reach (12, 12)")
        return
        
    print("Reached (12, 12). Probing vertical columns through Row 13...")
    
    # We will try columns from 12 to 20
    for x in range(12, 21):
        print(f"Testing Column {x}...")
        # Walk to Column x on Row 12
        col_path = []
        curr_x = mgba.get_coordinates()['x']
        if curr_x < x:
            for tx in range(curr_x + 1, x + 1):
                col_path.append((tx, 12))
        elif curr_x > x:
            for tx in range(curr_x - 1, x - 1, -1):
                col_path.append((tx, 12))
                
        if col_path:
            if not walk_path(col_path):
                print(f"Blocked walking horizontally to Column {x} on Row 12.")
                continue
                
        # Try to step Down to Row 13
        if step_one("Down", x, 13):
            print(f"SUCCESS: Column {x} is open at Row 13!")
            # Try to step further Down to Row 14
            if step_one("Down", x, 14):
                print(f"SUCCESS: Column {x} is open at Row 14!")
                # Let's see if we can go all the way to Row 16
                walk_path([(x, 15), (x, 16)])
                pos_after = mgba.get_coordinates()
                if pos_after['y'] == 16:
                    print(f"SUCCESS: Column {x} reaches Row 16!")
                    # Walk to balcony and drop!
                    balcony_path = []
                    # From (x, 16), walk to (16, 16)
                    if x < 16:
                        for tx in range(x + 1, 17):
                            balcony_path.append((tx, 16))
                    elif x > 16:
                        for tx in range(x - 1, 15, -1):
                            balcony_path.append((tx, 16))
                    # Walk Down Column 16 to (16, 18)
                    balcony_path.extend([(16, 17), (16, 18)])
                    # Walk Right to (19, 18)
                    balcony_path.extend([(17, 18), (18, 18), (19, 18)])
                    
                    if walk_path(balcony_path):
                        print("At (19, 18). Stepping Down to drop...")
                        mgba.press_buttons(["Down"])
                        time.sleep(1.0)
                        pos_end = mgba.get_coordinates()
                        if pos_end['y'] != 18 or pos_end['x'] != 19:
                            print("SUCCESSFULLY FELL TO B1F!!!")
                            return
                    else:
                        print("Failed to navigate to balcony.")
                        return
            # Step back UP to Row 12 to continue probing
            step_one("Up", x, 12)
            
    print("Probing finished.")

if __name__ == "__main__":
    main()
