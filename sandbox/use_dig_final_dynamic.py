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
    print("Opening Start menu...")
    # Press B multiple times to ensure we are in overworld
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300", "B", "sleep 300"])
    
    # Open Start menu
    mgba.press_buttons(["Start", "sleep 800"])
    
    # Take screenshot of the menu
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file)
    
    row_y_coords = [42, 90, 138, 186, 234, 282, 330]
    row_names = ["POKEDEX", "POKEMON", "ITEM", "PLAYER", "SAVE", "OPTION", "EXIT"]
    
    detected_row = None
    # Scan column x around 288 (on 480x432 scale)
    for y in range(20, 360):
        for x in range(270, 310):
            r, g, b = img.getpixel((x, y))
            if r < 50 and g < 50 and b < 50:
                # Find which row this y corresponds to
                for i, ry in enumerate(row_y_coords):
                    if abs(y - ry) < 12:
                        detected_row = i
                        break
        if detected_row is not None:
            break
            
    if detected_row is None:
        print("Error: Cursor not detected. Defaulting to POKEDEX.")
        detected_row = 0
    else:
        print(f"Detected cursor on row: {row_names[detected_row]}")
        
    # We want to go to POKEMON (row index 1)
    # Calculate moves to reach row index 1
    # If we are below row 1, we can press Up (detected_row - 1) times
    # If we are above, we can press Down (1 - detected_row) times
    moves = []
    if detected_row > 1:
        # Move Up to POKEMON
        up_clicks = detected_row - 1
        for _ in range(up_clicks):
            moves.extend(["Up", "sleep 250"])
    elif detected_row < 1:
        # Move Down to POKEMON
        down_clicks = 1 - detected_row
        for _ in range(down_clicks):
            moves.extend(["Down", "sleep 250"])
            
    # Enter POKEMON
    moves.extend(["A", "sleep 1200"])
    
    # Send movement inputs to go to POKEMON
    print("Moving cursor to POKEMON and entering...")
    mgba.press_buttons(moves)
    
    # Move Down 5 times to Slot 6 (TRUFFLE)
    print("Selecting TRUFFLE in Slot 6...")
    mgba.press_buttons([
        "Down", "sleep 250",
        "Down", "sleep 250",
        "Down", "sleep 250",
        "Down", "sleep 250",
        "Down", "sleep 250",
        "A", "sleep 1000" # Select TRUFFLE
    ])
    
    # Use DIG (Option 1)
    print("Using DIG...")
    mgba.press_buttons(["A", "sleep 3500"])
    
    pos = mgba.get_coordinates()
    print("DIG finished. Current position:", pos)

if __name__ == "__main__":
    main()
