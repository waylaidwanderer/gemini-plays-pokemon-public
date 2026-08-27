import mgba
import time
from PIL import Image

def is_in_battle_or_menu():
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file)
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    
    black_or_white = 0
    total_pixels = 0
    for y in range(115, 140):
        for x in range(10, 150):
            r, g, b = img_std.getpixel((x, y))[:3]
            total_pixels += 1
            is_bw = (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200)
            if is_bw:
                black_or_white += 1
                
    percentage = black_or_white / total_pixels
    return percentage > 0.85

def escape_battle_safely():
    # Advance "appeared!" text
    mgba.press_buttons(["B"])
    time.sleep(0.4)
    
    if not is_in_battle_or_menu():
        print("No battle or menu detected.")
        return False
        
    print("Battle or menu detected! Attempting escape...")
    mgba.press_buttons(["B"])
    time.sleep(0.4)
    
    if is_in_battle_or_menu():
        print("Still in battle menu. Pressing RUN...")
        mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
        time.sleep(1.5)
        for _ in range(5):
            mgba.press_buttons(["B"])
            time.sleep(0.2)
    return True

# 1. Escape from the current battle
print("Escaping from current wild battle...")
escape_battle_safely()
time.sleep(1.0)

pos = mgba.get_coordinates()
print("Starting from:", pos)

# Try testing Column 9 from Row 3 to Row 7
success = False
for row in [3, 4, 5, 6, 7]:
    # Check if we got into a battle on previous steps and escape
    if escape_battle_safely():
        time.sleep(0.5)
        
    current_pos = mgba.get_coordinates()
    print(f"Current pos: {current_pos}. Navigating to (10, {row})...")
    
    # Walk vertically to Row
    while current_pos["y"] != row:
        if current_pos["y"] < row:
            mgba.press_buttons(["Down"])
        else:
            mgba.press_buttons(["Up"])
        time.sleep(0.5)
        
        # Check for battles during vertical movement
        if escape_battle_safely():
            time.sleep(0.5)
            
        current_pos = mgba.get_coordinates()
        
    print(f"At (10, {row}). Testing walk LEFT to (9, {row})...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    # Check if we entered battle on the Left step
    if escape_battle_safely():
        time.sleep(0.5)
        
    new_pos = mgba.get_coordinates()
    if new_pos["x"] == 9:
        print(f"SUCCESS! Crossed into B1F West NORTH at {new_pos} on Row {row}!")
        success = True
        break
    else:
        print(f"Row {row} is BLOCKED. (Pos: {new_pos})")
        # If we got displaced or turned, make sure we are at Column 10
        if new_pos["x"] != 10:
            print("Not at Column 10! Walking back...")
            mgba.press_buttons(["Right"])
            time.sleep(0.5)

if success:
    pos = mgba.get_coordinates()
    if pos["x"] == 9:
        print("Walking to the Secret Key room at (1, 5)...")
        # Walk Left on Row pos["y"] to Column 1, then align to Row 5 if needed
        target_row = pos["y"]
        while pos["x"] > 1:
            mgba.press_buttons(["Left"])
            time.sleep(0.5)
            escape_battle_safely()
            pos = mgba.get_coordinates()
            
        while pos["y"] != 5:
            if pos["y"] < 5:
                mgba.press_buttons(["Down"])
            else:
                mgba.press_buttons(["Up"])
            time.sleep(0.5)
            escape_battle_safely()
            pos = mgba.get_coordinates()
            
        print("Reached Secret Key standing tile at:", pos)
        mgba.press_buttons(["Up"]) # Face UP
        time.sleep(0.5)
        mgba.press_buttons(["A"]) # Interact with Key
        time.sleep(1.0)
        for _ in range(5):
            mgba.press_buttons(["A"]) # Dismiss dialogs
            time.sleep(0.5)
        pos = mgba.get_coordinates()
        print("Secret Key retrieved! Current position:", pos)

print("Finished script! Current position:", mgba.get_coordinates())
