import mgba
import time
from PIL import Image

def handle_any_menu_or_battle():
    time.sleep(0.1)
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

def use_dig():
    print("Executing atomic DIG sequence with 350ms delays...")
    dig_sequence = [
        "B", "sleep 300",
        "B", "sleep 300",
        "B", "sleep 300",
        "Start", "sleep 800",
        "Up", "sleep 350",
        "Up", "sleep 350",
        "Up", "sleep 350",
        "Up", "sleep 350",
        "Up", "sleep 350",
        "Up", "sleep 350",
        "Up", "sleep 350",
        "Up", "sleep 350",
        "Up", "sleep 350",
        "Up", "sleep 350",
        "Down", "sleep 350",
        "A", "sleep 1200",
        "Down", "sleep 350",
        "Down", "sleep 350",
        "Down", "sleep 350",
        "Down", "sleep 350",
        "Down", "sleep 350",
        "A", "sleep 800",
        "A", "sleep 3500"
    ]
    mgba.press_buttons(dig_sequence)
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print("DIG finished. Current position:", pos)
    return pos

def main():
    pos = mgba.get_coordinates()
    print("Starting final solver from 3F East:", pos)
    
    if pos != {"x": 12, "y": 9}:
        print("Error: Player is not at (12, 9) on 3F East!")
        return

    # --- STAGE 1: Walk to Column 20 on 3F East ---
    print("Navigating on 3F East to Column 20...")
    if not run_steps([
        ("Down", {"x": 12, "y": 10}),
        ("Down", {"x": 12, "y": 11}),
        ("Right", {"x": 13, "y": 11}),
        ("Right", {"x": 14, "y": 11}),
        ("Right", {"x": 15, "y": 11}),
        ("Right", {"x": 16, "y": 11}),
        ("Right", {"x": 17, "y": 11}),
        ("Right", {"x": 18, "y": 11}),
        ("Right", {"x": 19, "y": 11}),
        ("Right", {"x": 20, "y": 11}),
    ]):
        return
    pos = mgba.get_coordinates()

    # --- STAGE 2: Walk UP Column 20 and RIGHT to Pitfall ---
    if pos == {"x": 20, "y": 11}:
        print("Walking UP Column 20 and RIGHT to the pitfall at (26, 3)...")
        if not run_steps([
            ("Up", {"x": 20, "y": 10}),
            ("Up", {"x": 20, "y": 9}),
            ("Up", {"x": 20, "y": 8}),
            ("Up", {"x": 20, "y": 7}),
            ("Up", {"x": 20, "y": 6}),
            ("Up", {"x": 20, "y": 5}),
            ("Up", {"x": 20, "y": 4}),
            ("Up", {"x": 20, "y": 3}),
            ("Right", {"x": 21, "y": 3}),
            ("Right", {"x": 22, "y": 3}),
            ("Right", {"x": 23, "y": 3}),
            ("Right", {"x": 24, "y": 3}),
            ("Right", {"x": 25, "y": 3}),
        ]):
            return
        
        # Step Right onto the actual pitfall tile at (26, 3) to fall
        mgba.press_buttons(["Right"])
        time.sleep(1.5)
        pos = mgba.get_coordinates()
        print("Dropped down! Current position:", pos)

    # --- STAGE 3: Warp 1F East -> B1F East ---
    # We are inside the fenced room. Use dynamic walking to reach Column 18 Row 3
    if pos["y"] < 10:
        print("Walking to B1F East stairs inside fenced room dynamically...")
        while pos["x"] > 18:
            if handle_any_menu_or_battle():
                pos = mgba.get_coordinates()
            mgba.press_buttons(["Left"])
            time.sleep(0.4)
            pos = mgba.get_coordinates()
            
        while pos["y"] > 3:
            if handle_any_menu_or_battle():
                pos = mgba.get_coordinates()
            mgba.press_buttons(["Up"])
            time.sleep(0.4)
            pos = mgba.get_coordinates()
            
        while pos["y"] < 3:
            if handle_any_menu_or_battle():
                pos = mgba.get_coordinates()
            mgba.press_buttons(["Down"])
            time.sleep(0.4)
            pos = mgba.get_coordinates()
            
        print("At (18, 3). Walking to stairs at (22, 2)...")
        if not run_steps([
            ("Right", {"x": 19, "y": 3}),
            ("Right", {"x": 20, "y": 3}),
            ("Right", {"x": 21, "y": 3}),
            ("Right", {"x": 22, "y": 3}),
            ("Up", {"x": 22, "y": 2}),
        ]):
            return
        
        # Extra step up to trigger warp
        mgba.press_buttons(["Up"])
        time.sleep(1.5)
        pos = mgba.get_coordinates()
        print("Landed on B1F East at:", pos)

    # --- STAGE 4: Cross to B1F West & Retrieve Secret Key ---
    if pos == {"x": 22, "y": 3}:
        print("Navigating B1F East to B1F West...")
        if not run_steps([
            ("Left", {"x": 21, "y": 3}),
            ("Down", {"x": 21, "y": 4}),
            ("Down", {"x": 21, "y": 5}),
        ]):
            return
        pos = mgba.get_coordinates()

        print("Walking Left across Row 5 through open gate...")
        while pos["x"] > 1:
            if handle_any_menu_or_battle():
                pos = mgba.get_coordinates()
            mgba.press_buttons(["Left"])
            time.sleep(0.4)
            pos = mgba.get_coordinates()
            print(f"Current: {pos}")
            
        print("At Secret Key spot:", pos)
        
        # Turn UP and press A to retrieve Secret Key
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        mgba.press_buttons(["A"])
        time.sleep(1.8) # Wait for text
        mgba.press_buttons(["A"]) # Dismiss key retrieved text
        time.sleep(1.0)
        mgba.press_buttons(["B"]) # Leftover text safety
        time.sleep(0.5)
        print("Secret Key retrieved successfully!")
        
        # Escape with DIG
        use_dig()
        print("Mansion completely solved!")

if __name__ == "__main__":
    main()
