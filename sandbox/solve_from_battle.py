import mgba
import time
from PIL import Image

def handle_battle_turn():
    # Detect if we are in a battle or dialogue by checking the screen
    time.sleep(0.15)
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
    if percentage > 0.90:
        # Dialogue or battle is active!
        # Let's inspect the screen to see if we have the battle menu (FIGHT / RUN)
        # Saffron Gym / Mansion battle menu has specific characteristics, but simply pressing "A"
        # will select FIGHT, and then pressing "A" again will select the first move (HYDRO PUMP).
        # To be safe, we can just press "A" repeatedly to attack, and "B" to advance text!
        print("Menu/Dialogue/Battle detected! Pressing A to advance...")
        mgba.press_buttons(["A"])
        time.sleep(0.4)
        return True
    return False

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print("Starting position:", pos)

# We are at (6, 8) facing UP toward the trainer at (6, 7).
# Let's step UP to talk to him!
if pos == {"x": 6, "y": 8}:
    print("Stepping UP to talk to the trainer...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)

# Now spam A/B to clear the dialogue and fight the battle!
print("Spamming A/B to complete the battle...")
for i in range(120): # 120 turns max
    if i % 10 == 0:
        pos = mgba.get_coordinates()
        print(f"Cycle {i}, current position: {pos}")
        if pos != {"x": 6, "y": 8}:
            # If our position changed, we might have won or moved!
            # But during battle, get_coordinates() might return None or the original position.
            pass
    
    # Press A to attack/advance, and B to clear text
    mgba.press_buttons(["A", "sleep 300", "B", "sleep 300"])
    time.sleep(0.8)

# Check our final position after the spamming is done
pos = mgba.get_coordinates()
print("Final position after battle:", pos)
mgba.take_screenshot()
