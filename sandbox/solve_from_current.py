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
    print("Starting master solver from current position:", pos)
    
    # We must be at (3, 11) or (2, 12) or (1, 12) on 3F West
    valid_positions = [{"x": 3, "y": 11}, {"x": 2, "y": 12}, {"x": 1, "y": 12}]
    if pos not in valid_positions:
        print("Error: Player is not at a valid starting position!")
        return

    # --- STAGE 0c: If we start at (1, 12) on 3F West (already in State B) ---
    if pos == {"x": 1, "y": 12}:
        print("At (1, 12) in State B. Navigating to Column 10 Row 9...")
        if not run_steps([
            ("Down", {"x": 1, "y": 13}),
            ("Right", {"x": 2, "y": 13}),
            ("Right", {"x": 3, "y": 13}),
            ("Right", {"x": 4, "y": 13}),
            ("Right", {"x": 5, "y": 13}),
            ("Right", {"x": 6, "y": 13}),
            ("Up", {"x": 6, "y": 12}),
            ("Up", {"x": 6, "y": 11}),
            ("Right", {"x": 7, "y": 11}),
            ("Right", {"x": 8, "y": 11}),
            ("Right", {"x": 9, "y": 11}),
            ("Right", {"x": 10, "y": 11}),
            ("Up", {"x": 10, "y": 10}),
            ("Up", {"x": 10, "y": 9}),
        ]):
            print("Failed to reach Column 10 Row 9.")
            return
        pos = mgba.get_coordinates()

    # --- STAGE 1: Walk to the Switch standing position at (2, 13) ---
    if pos == {"x": 3, "y": 11}:
        print("At (3, 11). Walking around to switch standing position at (2, 13)...")
        if not run_steps([
            ("Left", {"x": 2, "y": 11}),
            ("Left", {"x": 1, "y": 11}),
            ("Down", {"x": 1, "y": 12}),
            ("Down", {"x": 1, "y": 13}),
            ("Right", {"x": 2, "y": 13}),
        ]):
            print("Failed to reach (2, 13).")
            return
        pos = mgba.get_coordinates()

    # --- STAGE 2: Toggle Switch to State B ---
    if pos == {"x": 2, "y": 13}:
        print("Toggling Mewtwo statue switch to State B...")
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        mgba.press_buttons(["A"]) # Interact with statue
        time.sleep(1.8) # Wait for dialogue
        mgba.press_buttons(["A"]) # Press Yes
        time.sleep(1.8) # Wait for pressed dialogue
        mgba.press_buttons(["A"]) # Dismiss dialogue
        time.sleep(1.0)
        mgba.press_buttons(["B"]) # Leftover text safety
        time.sleep(0.5)
        print("Successfully toggled switch to State B!")
        pos = mgba.get_coordinates()

    # --- STAGE 3: Walk from switch to Column 10 Row 9 ---
    if pos == {"x": 2, "y": 12}:
        print("Navigating from switch (2, 12) to Column 10 Row 9...")
        if not run_steps([
            ("Down", {"x": 2, "y": 13}),
            ("Right", {"x": 3, "y": 13}),
            ("Right", {"x": 4, "y": 13}),
            ("Right", {"x": 5, "y": 13}),
            ("Right", {"x": 6, "y": 13}),
            ("Up", {"x": 6, "y": 12}),
            ("Up", {"x": 6, "y": 11}),
            ("Right", {"x": 7, "y": 11}),
            ("Right", {"x": 8, "y": 11}),
            ("Right", {"x": 9, "y": 11}),
            ("Right", {"x": 10, "y": 11}),
            ("Up", {"x": 10, "y": 10}),
            ("Up", {"x": 10, "y": 9}),
        ]):
            print("Failed to reach Column 10 Row 9.")
            return
        pos = mgba.get_coordinates()

    # --- STAGE 4: Cross to 3F East and Walk to Column 20 ---
    if pos == {"x": 10, "y": 9}:
        print("Crossing horizontally on Row 9 to Column 20 on 3F East...")
        if not run_steps([
            ("Right", {"x": 11, "y": 9}),
            ("Right", {"x": 12, "y": 9}),
            ("Right", {"x": 13, "y": 9}),
            ("Right", {"x": 14, "y": 9}),
            ("Right", {"x": 15, "y": 9}),
            ("Right", {"x": 16, "y": 9}),
            ("Right", {"x": 17, "y": 9}),
            ("Right", {"x": 18, "y": 9}),
            ("Right", {"x": 19, "y": 9}),
            ("Right", {"x": 20, "y": 9}),
        ]):
            print("Failed to reach Column 20 on Row 9.")
            return
        pos = mgba.get_coordinates()

    # --- STAGE 5: Walk UP Column 20 and RIGHT Row 3 to Pitfall ---
    if pos == {"x": 20, "y": 9}:
        print("Walking UP Column 20 and RIGHT along Row 3 to pitfall...")
        if not run_steps([
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
            print("Failed to reach (25, 3).")
            return

        # Step onto the actual pitfall tile to drop
        mgba.press_buttons(["Right"])
        time.sleep(1.0)
        pos = mgba.get_coordinates()
        print("Landed on 1F East inside fenced room. Current position:", pos)
    
    # --- STAGE 6: Align to (22, 4) on 1F East ---
    if pos != {"x": 22, "y": 3} and pos != {"x": 22, "y": 2} and pos["y"] < 10:
        print("Walking to B1F staircase on 1F East...")
        while pos["x"] > 22:
            mgba.press_buttons(["Left"])
            time.sleep(0.4)
            pos = mgba.get_coordinates()
        while pos["x"] < 22:
            mgba.press_buttons(["Right"])
            time.sleep(0.4)
            pos = mgba.get_coordinates()
        while pos["y"] > 4:
            mgba.press_buttons(["Up"])
            time.sleep(0.4)
            pos = mgba.get_coordinates()
        while pos["y"] < 4:
            mgba.press_buttons(["Down"])
            time.sleep(0.4)
            pos = mgba.get_coordinates()
        print("Successfully aligned to (22, 4):", pos)
        
        if not run_steps([
            ("Up", {"x": 22, "y": 3}),
            ("Up", {"x": 22, "y": 2}), # Warp down to B1F East landing at (22, 3)!
        ]):
            print("Failed to warp down to B1F East.")
            return
        pos = mgba.get_coordinates()

    # --- STAGE 7: Walk B1F East to B1F West & Retrieve Secret Key ---
    if pos == {"x": 22, "y": 3}:
        print("Walking B1F East to B1F West...")
        if not run_steps([
            ("Down", {"x": 22, "y": 4}),
            ("Down", {"x": 22, "y": 5}),
        ]):
            print("Failed to reach Row 5 on B1F East.")
            return
            
        print("Walking Left across Row 5 through open gate...")
        # Walk LEFT along Row 5 to Column 1
        pos = mgba.get_coordinates()
        while pos["x"] > 1:
            if handle_any_menu_or_battle():
                pos = mgba.get_coordinates()
            mgba.press_buttons(["Left"])
            time.sleep(0.4)
            pos = mgba.get_coordinates()
            
        print("At Secret Key spot:", pos)
        
        # Turn UP and press A to retrieve Secret Key
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        mgba.press_buttons(["A"])
        time.sleep(1.8) # Wait for text
        mgba.press_buttons(["A"]) # Dismiss key retrieved text
        time.sleep(1.0)
        mgba.press_buttons(["B"]) # Leftover text
        time.sleep(0.5)
        
        # --- STAGE 8: Escape with DIG ---
        use_dig()
        print("All stages complete!")

if __name__ == "__main__":
    main()
