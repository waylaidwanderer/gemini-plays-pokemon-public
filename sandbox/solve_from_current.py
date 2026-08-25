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
    print("Starting master solver from position:", pos)
    
    # --- STAGE 0: Exit Cinnabar Lab if inside ---
    if pos == {"x": 2, "y": 3}:
        print("Inside Cinnabar Lab. Exiting first...")
        if not run_steps([
            ("Down", {"x": 2, "y": 4}),
            ("Down", {"x": 2, "y": 5}),
            ("Down", {"x": 2, "y": 6}),
            ("Down", {"x": 2, "y": 7}),
            ("Down", {"x": 6, "y": 11}), # Exited Cinnabar Lab!
        ]):
            print("Failed to exit Cinnabar Lab.")
            return
        pos = mgba.get_coordinates()

    # --- STAGE 1: DIG out to Cinnabar Island (if we are in the Mansion) ---
    # (Since we are on Cinnabar Island overworld now, we skip this)
    if pos != {"x": 11, "y": 12} and pos != {"x": 6, "y": 11}:
        pos = use_dig()
        if pos != {"x": 11, "y": 12}:
            print("DIG did not land at (11, 12). Current position:", pos)
            return
            
    # --- STAGE 2: Walk to Pokemon Mansion Entrance (Safe Eastern Route) ---
    print("Walking to Pokemon Mansion Entrance...")
    
    # If we started outside Pokémon Center at (11, 12):
    if pos == {"x": 11, "y": 12}:
        if not run_steps([
            ("Right", {"x": 12, "y": 12}),
            ("Right", {"x": 13, "y": 12}),
            ("Right", {"x": 14, "y": 12}),
            ("Right", {"x": 15, "y": 12}),
            ("Right", {"x": 16, "y": 12}),
            ("Right", {"x": 17, "y": 12}),
            ("Right", {"x": 18, "y": 12}),
        ]):
            print("Failed to walk to column 18.")
            return
        pos = mgba.get_coordinates()
        
    # If we started outside Cinnabar Lab at (6, 11):
    if pos == {"x": 6, "y": 11}:
        if not run_steps([
            ("Down", {"x": 6, "y": 12}),
            ("Right", {"x": 7, "y": 12}),
            ("Right", {"x": 8, "y": 12}),
            ("Right", {"x": 9, "y": 12}),
            ("Right", {"x": 10, "y": 12}),
            ("Right", {"x": 11, "y": 12}),
            ("Right", {"x": 12, "y": 12}),
            ("Right", {"x": 13, "y": 12}),
            ("Right", {"x": 14, "y": 12}),
            ("Right", {"x": 15, "y": 12}),
            ("Right", {"x": 16, "y": 12}),
            ("Right", {"x": 17, "y": 12}),
            ("Right", {"x": 18, "y": 12}),
        ]):
            print("Failed to walk to column 18 from Lab.")
            return
        pos = mgba.get_coordinates()

    # Now we walk up Column 18, left on Row 5, and enter the Mansion
    if not run_steps([
        ("Up", {"x": 18, "y": 11}),
        ("Up", {"x": 18, "y": 10}),
        ("Up", {"x": 18, "y": 9}),
        ("Up", {"x": 18, "y": 8}),
        ("Up", {"x": 18, "y": 7}),
        ("Up", {"x": 18, "y": 6}),
        ("Up", {"x": 18, "y": 5}),
        ("Left", {"x": 17, "y": 5}),
        ("Left", {"x": 16, "y": 5}),
        ("Left", {"x": 15, "y": 5}),
        ("Left", {"x": 14, "y": 5}),
        ("Left", {"x": 13, "y": 5}),
        ("Left", {"x": 12, "y": 5}),
        ("Left", {"x": 11, "y": 5}),
        ("Left", {"x": 10, "y": 5}),
        ("Left", {"x": 9, "y": 5}),
        ("Left", {"x": 8, "y": 5}),
        ("Left", {"x": 7, "y": 5}),
        ("Left", {"x": 6, "y": 5}),
        ("Up", {"x": 6, "y": 4}),
        ("Up", {"x": 6, "y": 3}),
        ("Up", {"x": 5, "y": 27}), # Entered 1F West!
    ]):
        print("Failed to enter Mansion.")
        return

    # --- STAGE 3: Walk to 2F West ---
    print("Walking to 2F West staircase...")
    if not run_steps([
        ("Up", {"x": 5, "y": 26}),
        ("Up", {"x": 5, "y": 25}),
        ("Up", {"x": 5, "y": 24}),
        ("Up", {"x": 5, "y": 23}),
        ("Up", {"x": 5, "y": 22}),
        ("Up", {"x": 5, "y": 21}),
        ("Up", {"x": 5, "y": 20}),
        ("Up", {"x": 5, "y": 19}),
        ("Up", {"x": 5, "y": 18}),
        ("Up", {"x": 5, "y": 17}),
        ("Up", {"x": 5, "y": 16}),
        ("Up", {"x": 5, "y": 15}),
        ("Up", {"x": 5, "y": 14}),
        ("Up", {"x": 5, "y": 13}),
        ("Up", {"x": 5, "y": 12}),
        ("Up", {"x": 5, "y": 11}),
        ("Up", {"x": 5, "y": 10}),
        ("Left", {"x": 5, "y": 11}), # Warp up to 2F West!
    ]):
        print("Failed to reach 2F West.")
        return

    # --- STAGE 4: Walk the Bypass Route to 3F East ---
    print("Executing State B Bypass Route on 2F...")
    if not run_steps([
        ("Up", {"x": 5, "y": 10}),
        ("Up", {"x": 5, "y": 9}),
        ("Up", {"x": 5, "y": 8}),
        ("Up", {"x": 5, "y": 7}),
        ("Up", {"x": 5, "y": 6}),
        ("Up", {"x": 5, "y": 5}),
        ("Up", {"x": 5, "y": 4}),
        ("Up", {"x": 5, "y": 3}),
        ("Right", {"x": 6, "y": 3}),
        ("Right", {"x": 7, "y": 3}),
        ("Right", {"x": 8, "y": 3}),
        ("Right", {"x": 9, "y": 3}),
        ("Right", {"x": 10, "y": 3}),
        ("Right", {"x": 11, "y": 3}),
        ("Right", {"x": 12, "y": 3}),
        ("Right", {"x": 13, "y": 3}),
        ("Right", {"x": 14, "y": 3}),
        ("Right", {"x": 15, "y": 3}),
        ("Right", {"x": 16, "y": 3}),
        ("Right", {"x": 17, "y": 3}),
        ("Right", {"x": 18, "y": 3}),
        ("Down", {"x": 18, "y": 4}),
        ("Down", {"x": 18, "y": 5}),
        ("Down", {"x": 18, "y": 6}),
        ("Down", {"x": 18, "y": 7}),
        ("Down", {"x": 18, "y": 8}),
        ("Down", {"x": 18, "y": 9}),
        ("Down", {"x": 18, "y": 10}),
        ("Left", {"x": 17, "y": 10}),
        ("Left", {"x": 16, "y": 10}),
        ("Left", {"x": 15, "y": 10}),
        ("Down", {"x": 16, "y": 11}), # Warp up to 3F East!
    ]):
        print("Failed to reach 3F East.")
        return

    # --- STAGE 5: Walk 3F East to Pitfall ---
    print("Walking to pitfall on 3F East...")
    if not run_steps([
        ("Right", {"x": 17, "y": 11}),
        ("Right", {"x": 18, "y": 11}),
        ("Right", {"x": 19, "y": 11}),
        ("Right", {"x": 20, "y": 11}),
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
        print("Failed to reach pitfall.")
        return

    # Step onto the actual pitfall tile
    mgba.press_buttons(["Right"])
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print("Landed on 1F East inside fenced room. Current position:", pos)
    
    # We should land at (26, 4) or similar inside the fenced room.
    # --- STAGE 6: Walk 1F East to B1F East ---
    print("Walking to B1F staircase on 1F East...")
    # Navigate to (22, 4)
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

    # --- STAGE 7: Walk B1F East to B1F West & Retrieve Secret Key ---
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
