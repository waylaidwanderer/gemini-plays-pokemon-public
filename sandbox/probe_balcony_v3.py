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
    
    # 1. Walk from (12, 12) up Column 12 to Row 3
    setup_path = [
        (12, 11), (12, 10), (12, 9), (12, 8), (12, 7), (12, 6), (12, 5), (12, 4), (12, 3)
    ]
    if not walk_path(setup_path):
        print("Failed to reach (12, 3)")
        return
        
    print("Reached (12, 3). Probing central columns...")
    
    # We will try columns from 13 to 22
    for x in range(13, 23):
        # Walk to Column x on Row 3
        curr_pos = mgba.get_coordinates()
        curr_x = curr_pos['x']
        print(f"Testing Column {x} from Column {curr_x}...")
        
        col_path = []
        if curr_x < x:
            for tx in range(curr_x + 1, x + 1):
                col_path.append((tx, 3))
        elif curr_x > x:
            for tx in range(curr_x - 1, x - 1, -1):
                col_path.append((tx, 3))
                
        if col_path:
            if not walk_path(col_path):
                print(f"Blocked walking horizontally to Column {x} on Row 3.")
                # If we are blocked on Row 3, we cannot test further right columns easily, so break
                break
                
        # Try to step Down Column x through Rows 4-16
        print(f"Column {x}: Attempting to walk Down...")
        blocked = False
        reached_y = 3
        for y in range(4, 17):
            if step_one("Down", x, y):
                reached_y = y
            else:
                blocked = True
                print(f"Column {x}: Blocked at Row {y}")
                break
                
        if reached_y == 16:
            print(f"SUCCESS: Column {x} is completely open to Row 16!!!")
            # Let's walk to the balcony!
            # Balcony door is at (16, 17) or (16, 18)
            balcony_path = []
            if x < 16:
                for tx in range(x + 1, 17):
                    balcony_path.append((tx, 16))
            elif x > 16:
                for tx in range(x - 1, 15, -1):
                    balcony_path.append((tx, 16))
            balcony_path.extend([(16, 17), (16, 18), (17, 18), (18, 18), (19, 18)])
            
            print(f"Navigating to balcony: {balcony_path}")
            if walk_path(balcony_path):
                print("At (19, 18). Stepping Down to drop...")
                mgba.press_buttons(["Down"])
                time.sleep(1.0)
                pos_end = mgba.get_coordinates()
                if pos_end['y'] != 18 or pos_end['x'] != 19:
                    print("SUCCESSFULLY FELL TO B1F!!!")
                    return
            else:
                print("Failed to walk to balcony from bottom.")
                return
                
        # If we got blocked, walk back UP to Row 3 to test the next column
        if blocked and reached_y > 3:
            print(f"Column {x}: Retreating back Up to Row 3...")
            for y in range(reached_y - 1, 2, -1):
                step_one("Up", x, y)
                
    print("Probing of central columns finished.")

if __name__ == "__main__":
    main()
