import mgba
import time

def check_pos():
    pos = mgba.get_coordinates()
    print("CURRENT POSITION:", pos)
    return pos

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

p = check_pos()

if p == {"x": 6, "y": 10}:
    # Walk to (2, 11)
    print("Walking to (2, 11)...")
    steps = [
        ("Down", {"x": 6, "y": 11}),
        ("Left", {"x": 5, "y": 11}),
        ("Left", {"x": 4, "y": 11}), # Wait! Is (4, 11) blocked by Burglar?
    ]
    # Let's check if (4, 11) is blocked.
    # The Burglar was at (4, 11) on Turn 61908. But on Turn 61917, he was at (9, 11)!
    # Let's walk to (2, 11) via Row 11 if possible, else Row 13.
    # Let's try walking along Row 11 first.
    steps = [
        ("Down", {"x": 6, "y": 11}),
        ("Left", {"x": 5, "y": 11}),
        ("Left", {"x": 4, "y": 11}),
        ("Left", {"x": 3, "y": 11}),
        ("Left", {"x": 2, "y": 11}),
    ]
    
    # We will try Row 11. If it fails (meaning blocked), we will go via Row 13!
    for i, (d, expected) in enumerate(steps):
        mgba.press_buttons([d])
        time.sleep(0.55)
        p = check_pos()
        if p != expected:
            print(f"Blocked at {p}! Trying alternative Row 13 bypass...")
            # Walk to Row 13
            # We are at p. Let's walk Down to Row 13.
            curr_x = p["x"]
            curr_y = p["y"]
            if curr_y == 11:
                mgba.press_buttons(["Down"])
                time.sleep(0.55)
                mgba.press_buttons(["Down"])
                time.sleep(0.55)
            # Walk Left along Row 13
            for x in range(curr_x - 1, 1, -1):
                mgba.press_buttons(["Left"])
                time.sleep(0.55)
            # Walk Up to (2, 11)
            mgba.press_buttons(["Up"])
            time.sleep(0.55)
            mgba.press_buttons(["Up"])
            time.sleep(0.55)
            p = check_pos()
            break
            
    if p == {"x": 2, "y": 11}:
        print("At (2, 11)! Facing UP towards (2, 10)...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        
        # Press A
        print("Pressing A...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        # Take a screenshot to inspect dialogue
        scr = mgba.take_screenshot()
        from PIL import Image
        img = Image.open(scr).resize((160, 144), Image.Resampling.NEAREST)
        img.save("mansion_switch_dialogue_UP_at_2_11.png")
        print("Saved mansion_switch_dialogue_UP_at_2_11.png")
        
        # Let's check if the dialogue opened
        black_or_white = 0
        total_pixels = 0
        for y in range(115, 140):
            for x in range(10, 150):
                r, g, b = img.getpixel((x, y))
                total_pixels += 1
                if (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200):
                    black_or_white += 1
        if black_or_white / total_pixels > 0.90:
            print("Dialogue open! Toggling switch to State B...")
            # Select YES
            mgba.press_buttons(["A"])
            time.sleep(1.5)
            # Dismiss result
            mgba.press_buttons(["A"])
            time.sleep(1.0)
            mgba.press_buttons(["A"])
            time.sleep(1.0)
            print("Successfully toggled switch to State B!")
        else:
            print("No dialogue opened!")
else:
    print("Not starting at (6, 10)")
