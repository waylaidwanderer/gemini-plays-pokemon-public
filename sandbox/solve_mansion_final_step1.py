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
    print("Starting master solver step 1, current coords:", pos)
    
    valid_positions = [{"x": 10, "y": 5}, {"x": 10, "y": 7}, {"x": 11, "y": 12}]
    if pos not in valid_positions:
        print("Error: Player is not at a valid starting position!")
        return

    # --- STAGE 0: DIG out from B1F East if we are there ---
    if pos == {"x": 10, "y": 5}:
        pos = use_dig()
        if pos != {"x": 10, "y": 7} and pos != {"x": 11, "y": 12}:
            print("DIG did not land at Cinnabar Island. Current position:", pos)
            return

    # If we landed at (11, 12), walk Left to (10, 12), then Up to (10, 7)
    if pos == {"x": 11, "y": 12}:
        if not run_steps([
            ("Left", {"x": 10, "y": 12}),
        ]):
            return
        pos = mgba.get_coordinates()

    # From (10, 12) we walk UP to (10, 7)
    if pos == {"x": 10, "y": 12}:
        if not run_steps([
            ("Up", {"x": 10, "y": 11}),
            ("Up", {"x": 10, "y": 10}),
            ("Up", {"x": 10, "y": 9}),
            ("Up", {"x": 10, "y": 8}),
            ("Up", {"x": 10, "y": 7}),
        ]):
            return
        pos = mgba.get_coordinates()

    # --- STAGE 1: Walk to Mansion entrance via Column 12 Right-Side Bypass ---
    if pos == {"x": 10, "y": 7}:
        print("Walking to Pokemon Mansion Entrance...")
        if not run_steps([
            ("Right", {"x": 11, "y": 7}),
            ("Right", {"x": 12, "y": 7}),
            ("Down", {"x": 12, "y": 8}),
            ("Down", {"x": 12, "y": 9}),
            ("Down", {"x": 12, "y": 10}),
            ("Down", {"x": 12, "y": 11}),
            ("Down", {"x": 12, "y": 12}),
            ("Left", {"x": 11, "y": 12}),
            ("Left", {"x": 10, "y": 12}),
            ("Left", {"x": 9, "y": 12}),
            ("Left", {"x": 8, "y": 12}),
            ("Left", {"x": 7, "y": 12}),
            ("Left", {"x": 6, "y": 12}),
            ("Up", {"x": 6, "y": 11}),
            ("Left", {"x": 5, "y": 11}),
            ("Left", {"x": 4, "y": 11}),
            ("Up", {"x": 4, "y": 10}),
            ("Up", {"x": 4, "y": 9}),
            ("Up", {"x": 4, "y": 8}),
            ("Up", {"x": 4, "y": 7}),
            ("Up", {"x": 4, "y": 6}),
            ("Up", {"x": 4, "y": 5}),
            ("Up", {"x": 4, "y": 4}),
            ("Up", {"x": 4, "y": 3}),
            ("Right", {"x": 5, "y": 3}),
            ("Right", {"x": 6, "y": 3}),
        ]):
            return
            
        # Extra step up to land inside at (5, 27)
        mgba.press_buttons(["Up"])
        time.sleep(1.5)
        pos = mgba.get_coordinates()
        print("Entered Mansion 1F West:", pos)

    # --- STAGE 2: Walk UP Column 5 on 1F West to stairs ---
    if pos == {"x": 5, "y": 27}:
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

    # Navigating on 3F West
    if pos == {"x": 7, "y": 11} or pos == {"x": 7, "y": 10}:
        print("Navigating on 3F West...")
        if pos == {"x": 7, "y": 10}:
            if not walk_step("Down", {"x": 7, "y": 11}):
                return
        pos = mgba.get_coordinates()

    # Now we are at (7, 11). Walk LEFT to Column 6 Row 11
    if pos == {"x": 7, "y": 11}:
        if not run_steps([
            ("Left", {"x": 6, "y": 11}),
        ]):
            return
        pos = mgba.get_coordinates()

    # Try walking UP to (6, 10). If blocked, it means gate at (6, 9) is closed (State A).
    # If successful, it means gate is open (State B).
    if pos == {"x": 6, "y": 11}:
        print("Testing if 3F West gate at (6, 9) is open (State B)...")
        gate_open = walk_step("Up", {"x": 6, "y": 10}, retries=2)
        pos = mgba.get_coordinates()
        
        if not gate_open:
            print("Gate is CLOSED! We are in State A. Navigating to switch to toggle to State B...")
            # We are at (6, 11). Walk to switch at (2, 13)
            if not run_steps([
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
            
            # Toggle switch to State B
            if pos == {"x": 2, "y": 13}:
                print("Toggling Mewtwo statue switch to State B...")
                mgba.press_buttons(["Up"])
                time.sleep(0.4)
                mgba.press_buttons(["A"]) # Interact
                time.sleep(1.8)
                mgba.press_buttons(["A"]) # YES
                time.sleep(1.8)
                mgba.press_buttons(["A"]) # Dismiss
                time.sleep(1.0)
                mgba.press_buttons(["B"])
                time.sleep(0.5)
                print("Successfully toggled switch to State B!")
                pos = mgba.get_coordinates()
                
            # Walk from switch (2, 12) to Column 10 Row 9
            if pos == {"x": 2, "y": 12}:
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
        else:
            print("Gate is OPEN! We are already in State B. Proceeding directly to Column 10 Row 9...")
            # We are at (6, 10). Walk through the open gate to (10, 9)
            if not run_steps([
                ("Up", {"x": 6, "y": 9}),
                ("Up", {"x": 6, "y": 8}),
                ("Right", {"x": 7, "y": 8}),
                ("Right", {"x": 8, "y": 8}),
                ("Right", {"x": 9, "y": 8}),
                ("Right", {"x": 10, "y": 8}),
                ("Down", {"x": 10, "y": 9}),
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
