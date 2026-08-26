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
        return True
    return False

def main():
    print("Checking moves of all party Pokemon...")
    # Press B to ensure clean state
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    
    # Open Start menu
    mgba.press_buttons(["Start", "sleep 800"])
    
    # Select POKEMON
    mgba.press_buttons(["Up", "sleep 150"] * 10)
    mgba.press_buttons(["Down", "sleep 250", "A", "sleep 1200"])
    
    # Scan all 6 slots
    for slot in range(6):
        print(f"Checking Slot {slot+1} moves...")
        if slot > 0:
            mgba.press_buttons(["Down", "sleep 250"])
            
        # Select Pokemon
        mgba.press_buttons(["A", "sleep 800"])
        
        # Select STATS (usually the 1st option)
        mgba.press_buttons(["A", "sleep 1200"])
        
        # Take screenshot of Page 1
        s1 = mgba.take_screenshot()
        print(f"Slot {slot+1} Stats Page 1:", s1)
        
        # Press A to go to Page 2 (Moves Page)
        mgba.press_buttons(["A", "sleep 1200"])
        s2 = mgba.take_screenshot()
        print(f"Slot {slot+1} Stats Page 2 (Moves):", s2)
        
        # Press B to go back to submenu, and B again to go back to list
        mgba.press_buttons(["B", "sleep 500", "B", "sleep 500"])
        
    # Close Pokemon menu and Start menu
    mgba.press_buttons(["B", "sleep 500", "B", "sleep 500"])

if __name__ == "__main__":
    main()
