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
    print("Starting final solver from 1F East position:", pos)
    
    # We must be at (22, 6) on 1F East inside the fenced room
    if pos != {"x": 22, "y": 6}:
        print("Error: Player is not at (22, 6)!")
        return

    # --- STAGE 1: Walk to the staircase at (22, 2) on 1F East ---
    print("Walking UP to B1F staircase...")
    if not run_steps([
        ("Up", {"x": 22, "y": 5}),
        ("Up", {"x": 22, "y": 4}),
        ("Up", {"x": 22, "y": 3}),
        ("Up", {"x": 22, "y": 2}), # Warp down to B1F East landing at (22, 3)
    ]):
        print("Failed to warp down to B1F East.")
        return
    pos = mgba.get_coordinates()

    # --- STAGE 2: Walk B1F East to B1F West & Retrieve Secret Key ---
    if pos == {"x": 22, "y": 3} or pos == {"x": 22, "y": 2}:
        if pos == {"x": 22, "y": 3}:
            mgba.press_buttons(["Up"])
            time.sleep(1.5)
            pos = mgba.get_coordinates()
        print("Walking B1F East to B1F West...")
        # Walk left to (21, 3), down to (21, 5)
        if not run_steps([
            ("Left", {"x": 21, "y": 3}),
            ("Down", {"x": 21, "y": 4}),
            ("Down", {"x": 21, "y": 5}),
        ]):
            print("Failed to reach B1F West corridor.")
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
        print("All stages complete!")

if __name__ == "__main__":
    main()
