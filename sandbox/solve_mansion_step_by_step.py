import mgba
import time
from PIL import Image

def handle_any_menu_or_battle():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file)
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    
    black_or_white = 0
    total_pixels = 0
    for y in range(115, 140):
        for x in range(10, 150):
            r, g, b = img_std.getpixel((x, y))
            total_pixels += 1
            is_bw = (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200)
            if is_bw:
                black_or_white += 1
                
    percentage = black_or_white / total_pixels
    if percentage > 0.90:
        print(f"Menu/Dialogue detected! (B/W: {percentage*100:.2f}%)")
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        
        # Check if still in battle
        scr_file2 = mgba.take_screenshot()
        img2 = Image.open(scr_file2)
        img_std2 = img2.resize((160, 144), Image.Resampling.NEAREST)
        black_or_white2 = 0
        for y in range(115, 140):
            for x in range(10, 150):
                r, g, b = img_std2.getpixel((x, y))
                is_bw = (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200)
                if is_bw:
                    black_or_white2 += 1
        percentage2 = black_or_white2 / total_pixels
        
        if percentage2 > 0.90:
            print("Still in battle. Running...")
            mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
            time.sleep(1.5)
            # Dismiss run text
            for _ in range(4):
                mgba.press_buttons(["B"])
                time.sleep(0.3)
        return True
    return False

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        if handle_any_menu_or_battle():
            pos = mgba.get_coordinates()
            if pos == expected_coords:
                return True
        mgba.press_buttons([direction])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction}, current position: {pos}")
            return True
        print(f"Blocked or battle! Retrying {direction} to {expected_coords} (attempt {i+1}/{retries}), current: {pos}")
        time.sleep(0.3)
    return False

def run_steps(steps):
    for d, c in steps:
        if not walk_step(d, c):
            return False
    return True

def main():
    pos = mgba.get_coordinates()
    print("Mansion step-by-step master solver. Current position:", pos)
    
    # Dismiss any text
    mgba.press_buttons(["B"])
    time.sleep(0.3)
    
    success = True
    
    # --- STAGE 1: Cinnabar Island Overworld ---
    if pos == {"x": 11, "y": 12}:
        print("STAGE 1: Re-entering Pokémon Mansion...")
        if not run_steps([
            ("Down", {"x": 11, "y": 13}),
            ("Left", {"x": 10, "y": 13}),
            ("Left", {"x": 9, "y": 13}),
            ("Left", {"x": 8, "y": 13}),
            ("Left", {"x": 7, "y": 13}),
            ("Left", {"x": 6, "y": 13}),
            ("Up", {"x": 6, "y": 12}),
            ("Up", {"x": 6, "y": 11}),
            ("Up", {"x": 6, "y": 10}),
            ("Up", {"x": 6, "y": 9}),
            ("Up", {"x": 6, "y": 8}),
            ("Up", {"x": 6, "y": 7}),
            ("Up", {"x": 6, "y": 6}),
            ("Up", {"x": 6, "y": 5}),
            ("Up", {"x": 6, "y": 4}),
            ("Up", {"x": 6, "y": 3}),
        ]):
            success = False
            
        if success:
            print("Entering the Mansion door...")
            mgba.press_buttons(["Up"])
            time.sleep(2.0)
            print("New position:", mgba.get_coordinates())
            
    # --- STAGE 2: Mansion 1F West ---
    pos = mgba.get_coordinates()
    if success and pos == {"x": 5, "y": 27}:
        print("STAGE 2: Walking to 1F West stairs...")
        for y in range(26, 9, -1):
            if not walk_step("Up", {"x": 5, "y": y}):
                success = False
                break
                
        if success:
            print("Warping UP to 2F West...")
            mgba.press_buttons(["Up"])
            time.sleep(1.5)
            print("New position:", mgba.get_coordinates())
            
    # --- STAGE 3: Mansion 2F West (State A -> State B) ---
    pos = mgba.get_coordinates()
    if success and pos == {"x": 5, "y": 11}:
        print("STAGE 3: Walking to 2F West switch...")
        if not run_steps([
            ("Left", {"x": 4, "y": 11}),
            ("Left", {"x": 3, "y": 11}),
            ("Left", {"x": 2, "y": 11}),
            ("Down", {"x": 2, "y": 12}),
        ]):
            success = False
            
        if success:
            print("At (2, 12)! Toggling switch to State B...")
            mgba.press_buttons(["Up"])
            time.sleep(0.4)
            mgba.press_buttons(["A"]) # "A secret switch!"
            time.sleep(0.8)
            mgba.press_buttons(["A"]) # select YES
            time.sleep(0.8)
            mgba.press_buttons(["A"]) # "Pressed it!"
            time.sleep(0.8)
            
            print("Switch toggled to State B! Walking back to stairs...")
            if not run_steps([
                ("Right", {"x": 3, "y": 12}),
                ("Up", {"x": 3, "y": 11}),
                ("Right", {"x": 4, "y": 11}),
                ("Right", {"x": 5, "y": 11}),
                ("Right", {"x": 6, "y": 11}),
                ("Right", {"x": 7, "y": 11}),
            ]):
                success = False
                
        if success:
            print("Warping UP to 3F West...")
            mgba.press_buttons(["Up"])
            time.sleep(1.5)
            print("New position:", mgba.get_coordinates())
            
    # --- STAGE 4: Mansion 3F West (State B -> State A) ---
    pos = mgba.get_coordinates()
    if success and pos == {"x": 7, "y": 11}:
        print("STAGE 4: Walking to 3F West switch...")
        if not run_steps([
            ("Down", {"x": 7, "y": 11}), # align
            ("Left", {"x": 6, "y": 11}),
            ("Left", {"x": 5, "y": 11}),
            ("Left", {"x": 4, "y": 11}),
            ("Left", {"x": 3, "y": 11}),
            ("Left", {"x": 2, "y": 11}),
            ("Left", {"x": 1, "y": 11}),
            ("Down", {"x": 1, "y": 12}),
            ("Right", {"x": 2, "y": 12}),
        ]):
            success = False
            
        if success:
            print("At (2, 12) on 3F West! Toggling switch to State A...")
            mgba.press_buttons(["Up"])
            time.sleep(0.4)
            mgba.press_buttons(["A"]) # "A secret switch!"
            time.sleep(0.8)
            mgba.press_buttons(["A"]) # select YES
            time.sleep(0.8)
            mgba.press_buttons(["A"]) # "Pressed it!"
            time.sleep(0.8)
            
            print("Switch toggled to State A! Walking back to warp DOWN...")
            if not run_steps([
                ("Left", {"x": 1, "y": 12}),
                ("Up", {"x": 1, "y": 11}),
                ("Right", {"x": 2, "y": 11}),
                ("Right", {"x": 3, "y": 11}),
                ("Right", {"x": 4, "y": 11}),
                ("Right", {"x": 5, "y": 11}),
                ("Right", {"x": 6, "y": 11}),
                ("Right", {"x": 7, "y": 11}),
            ]):
                success = False
                
        if success:
            print("Warping DOWN to 2F West...")
            mgba.press_buttons(["Up"])
            time.sleep(1.5)
            print("New position:", mgba.get_coordinates())

if __name__ == "__main__":
    main()
