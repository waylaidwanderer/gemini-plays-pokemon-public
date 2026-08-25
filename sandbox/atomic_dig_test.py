import mgba
import time
from PIL import Image

def get_start_menu_index():
    scr = mgba.take_screenshot()
    img = Image.open(scr)
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    
    y_coords = [16, 32, 48, 64, 80, 96, 112]
    for i, y in enumerate(y_coords):
        is_dark = False
        for dy in range(-2, 3):
            r, g, b = img_std.getpixel((89, y + dy))
            if r < 50 and g < 50 and b < 50:
                is_dark = True
                break
        if is_dark:
            return i
    return -1

def main():
    idx = get_start_menu_index()
    print("Detected Start menu index:", idx)
    if idx == -1:
        print("Error: Start menu cursor not found!")
        return
        
    target = 1
    buttons = []
    if idx > target:
        for _ in range(idx - target):
            buttons.append("Up")
            buttons.append("sleep 350")
    elif idx < target:
        for _ in range(target - idx):
            buttons.append("Down")
            buttons.append("sleep 350")
            
    buttons.append("A")
    buttons.append("sleep 1200")
    
    for _ in range(7):
        buttons.append("Down")
        buttons.append("sleep 350")
        
    buttons.append("A")
    buttons.append("sleep 1000")
    buttons.append("A")
    buttons.append("sleep 4000")
    
    print("Executing buttons:", buttons)
    mgba.press_buttons(buttons)
    print("New position after DIG:", mgba.get_coordinates())

if __name__ == "__main__":
    main()
