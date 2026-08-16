import mgba
import time
from PIL import Image

def get_textbox_ratio():
    screenshot_path = mgba.take_screenshot()
    img = Image.open(screenshot_path)
    gray = img.convert("L")
    
    white_pixels = 0
    total_pixels = 0
    
    for x in range(60, 420):
        for y in range(360, 405):
            r, g, b, *a = img.getpixel((x, y))
            if r > 220 and g > 220 and b > 220 and abs(r - g) < 15 and abs(g - b) < 15:
                white_pixels += 1
            total_pixels += 1
            
    return white_pixels / total_pixels

# We are at (6, 2) facing RIGHT.
# We press RIGHT once more to step onto (7, 2).

print("--- STEPPING RIGHT TO (7, 2) ---")
mgba.press_buttons(["Right"])
time.sleep(0.5)

# Press A to speak to clerk
print("Speaking to clerk...")
mgba.press_buttons(["A"])
time.sleep(1.0)
print("TextBox ratio after A:", get_textbox_ratio())

# Complete payment dialogue (A 12 times)
print("Completing dialogue...")
for i in range(12):
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print(f"Step {i+1}: position={pos}, TextBox ratio={get_textbox_ratio()}")
    if pos and (pos['x'] != 6 and pos['x'] != 7):
        print("Successfully warped into Safari Zone Center!")
        break

time.sleep(1.5)
final_pos = mgba.get_coordinates()
print("Final Position:", final_pos)
mgba.take_screenshot()
