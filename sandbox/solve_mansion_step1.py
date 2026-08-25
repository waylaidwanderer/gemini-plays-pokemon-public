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
    print("Starting master solver step 1 from B1F East:", pos)
    
    if pos != {"x": 10, "y": 5}:
        print("Error: Player is not at (10, 5)!")
        return

    # --- STAGE 0: DIG out from B1F East ---
    pos = use_dig()
    if pos != {"x": 11, "y": 12}:
        print("DIG did not land at (11, 12). Current position:", pos)
        return

    # --- STAGE 1: Walk to Pokemon Mansion Entrance (Safe Row 4 Bypass) ---
    print("Walking to Pokemon Mansion Entrance...")
    if not run_steps([
        ("Right", {"x": 12, "y": 12}),
        ("Right", {"x": 13, "y": 12}),
        ("Right", {"x": 14, "y": 12}),
        ("Right", {"x": 15, "y": 12}),
        ("Right", {"x": 16, "y": 12}),
        ("Right", {"x": 17, "y": 12}),
        ("Right", {"x": 18, "y": 12}),
        ("Up", {"x": 18, "y": 11}),
        ("Up", {"x": 18, "y": 10}),
        ("Up", {"x": 18, "y": 9}),
        ("Up", {"x": 18, "y": 8}),
        ("Up", {"x": 18, "y": 7}),
        ("Up", {"x": 18, "y": 6}),
        ("Up", {"x": 18, "y": 5}),
        ("Up", {"x": 18, "y": 4}),
        ("Left", {"x": 17, "y": 4}),
        ("Left", {"x": 16, "y": 4}),
        ("Left", {"x": 15, "y": 4}),
        ("Left", {"x": 14, "y": 4}),
        ("Left", {"x": 13, "y": 4}),
        ("Left", {"x": 12, "y": 4}),
        ("Left", {"x": 11, "y": 4}),
        ("Left", {"x": 10, "y": 4}),
        ("Left", {"x": 9, "y": 4}),
        ("Left", {"x": 8, "y": 4}),
        ("Left", {"x": 7, "y": 4}),
        ("Left", {"x": 6, "y": 4}),
        ("Up", {"x": 6, "y": 3}),
        ("Up", {"x": 5, "y": 27}), # Entered 1F West!
    ]):
        print("Failed to enter Mansion.")
        return
    pos = mgba.get_coordinates()

    # --- STAGE 2: Walk UP Column 5 on 1F West to stairs ---
    print("Walking UP Column 5 on 1F West...")
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
    ]):
        return
    pos = mgba.get_coordinates()

    # --- STAGE 3: Warp 1F -> 2F West ---
    if pos == {"x": 5, "y": 10}:
        print("Warping UP to 2F West...")
        mgba.press_buttons(["Up"])
        time.sleep(1.5)
        pos = mgba.get_coordinates()
        print("Landed on 2F West at:", pos)

    # Navigating to 2F-to-3F stairs
    if pos == {"x": 5, "y": 11} or pos == {"x": 6, "y": 10}:
        print("Navigating to 2F-to-3F stairs...")
        if pos == {"x": 5, "y": 11}:
            if not run_steps([
                ("Up", {"x": 5, "y": 10}),
                ("Right", {"x": 6, "y": 10}),
                ("Right", {"x": 7, "y": 10}),
            ]):
                return
        elif pos == {"x": 6, "y": 10}:
            if not run_steps([
                ("Right", {"x": 7, "y": 10}),
            ]):
                return
        pos = mgba.get_coordinates()

    # --- STAGE 4: Warp 2F -> 3F West ---
    if pos == {"x": 7, "y": 10}:
        print("Warping UP to 3F West...")
        mgba.press_buttons(["Up"])
        time.sleep(1.5)
        pos = mgba.get_coordinates()
        print("Landed on 3F West at:", pos)

    # Navigating to 3F West switch standing position
    if pos == {"x": 7, "y": 11} or pos == {"x": 7, "y": 10}:
        print("Navigating to 3F West switch at (2, 13)...")
        if pos == {"x": 7, "y": 10}:
            if not walk_step("Down", {"x": 7, "y": 11}):
                return
        if not run_steps([
            ("Left", {"x": 6, "y": 11}),
            ("Left", {"x": 5, "y": 11}),
            ("Left", {"x": 4, "y": 11}),
            ("Left", {"x": 3, "y": 11}),
            ("Left", {"x": 2, "y": 11}),
            ("Left", {"x": 1, "y": 11}),
            ("Down", {"x": 1, "y": 12}),
            ("Down", {"x": 1, "y": 13}),
            ("Right", {"x": 2, "y": 13}),
        ]):
            return
        pos = mgba.get_coordinates()

    # --- STAGE 5: Toggle switch to State B ---
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

    # --- STAGE 6: Walk from switch to Column 10 Row 9 on 3F West ---
    if pos == {"x": 2, "y": 12}:
        print("Navigating from switch to Column 10 Row 9...")
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
            return
        pos = mgba.get_coordinates()

    # --- STAGE 7: Cross 3F West to 3F East ---
    if pos == {"x": 10, "y": 9}:
        print("Crossing horizontally to 3F East...")
        mgba.press_buttons(["Right"])
        time.sleep(1.5)
        pos = mgba.get_coordinates()
        print("Landed on 3F East at:", pos)
        
    if pos == {"x": 11, "y": 9} or pos == {"x": 12, "y": 9}:
        # Step Down to Row 11 to align for the final leg
        print("Aligning on 3F East...")
        run_steps([
            ("Down", {"x": pos["x"], "y": 10}),
            ("Down", {"x": pos["x"], "y": 11}),
        ])
        print("Final position:", mgba.get_coordinates())

if __name__ == "__main__":
    main()
