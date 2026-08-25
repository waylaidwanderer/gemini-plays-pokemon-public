import mgba
import time
from PIL import Image

def handle_battle_and_run():
    print("Handling battle, attempting to run...")
    # Wait for battle transitions / text
    time.sleep(1.0)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
        
    # We should be in the battle menu now (FIGHT/PKMN/ITEM/RUN)
    # The RUN button is at Bottom-Right in the 2x2 grid.
    # From FIGHT (top-left): press Down to PKMN/RUN, Right to ITEM/RUN, A to select.
    # Let's press Down, Right, A.
    print("Pressing Down, Right, A to RUN...")
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
    time.sleep(2.0)
    
    # Press B to dismiss any run message
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    
    pos = mgba.get_coordinates()
    print("Coordinates after running from battle:", pos)
    return pos

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        # Check if we got into a wild battle while walking
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
            print("Battle or dialogue detected during walk! Running...")
            handle_battle_and_run()
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
    print("Starting solve_mansion_final_step2.py, current coords:", pos)
    
    # We are in a battle on (22, 1). Let's run first.
    pos = handle_battle_and_run()
    
    # Wait, if we are at (22, 1) or (22, 2) or (22, 3) (landing stairs on B1F East)
    # Let's walk to Column 21 Row 5
    print("Navigating to B1F East to B1F West...")
    if pos == {"x": 22, "y": 1}:
        if not run_steps([
            ("Down", {"x": 22, "y": 2}),
            ("Down", {"x": 22, "y": 3}),
            ("Left", {"x": 21, "y": 3}),
            ("Down", {"x": 21, "y": 4}),
            ("Down", {"x": 21, "y": 5}),
        ]):
            return
    elif pos == {"x": 22, "y": 2}:
        if not run_steps([
            ("Down", {"x": 22, "y": 3}),
            ("Left", {"x": 21, "y": 3}),
            ("Down", {"x": 21, "y": 4}),
            ("Down", {"x": 21, "y": 5}),
        ]):
            return
    elif pos == {"x": 22, "y": 3}:
        if not run_steps([
            ("Left", {"x": 21, "y": 3}),
            ("Down", {"x": 21, "y": 4}),
            ("Down", {"x": 21, "y": 5}),
        ]):
            return
            
    pos = mgba.get_coordinates()

    print("Walking Left across Row 5 through open gate...")
    while pos["x"] > 1:
        # Check battle
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
            print("Battle or dialogue detected during walk! Running...")
            handle_battle_and_run()
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
