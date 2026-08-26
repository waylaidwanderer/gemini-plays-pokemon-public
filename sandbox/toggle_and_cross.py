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

if p == {"x": 6, "y": 11}:
    # Let's walk Left to (5, 11)
    print("Walking Left to (5, 11)...")
    mgba.press_buttons(["Left"])
    time.sleep(0.55)
    p = check_pos()
    
    if p == {"x": 5, "y": 11}:
        # Try walking UP Column 5
        print("At (5, 11). Trying to walk UP Column 5...")
        mgba.press_buttons(["Up"]) # to (5, 10)
        time.sleep(0.55)
        p = check_pos()
        
        if p == {"x": 5, "y": 10}:
            print("Successfully walked UP to (5, 10). Trying to walk UP to (5, 9)...")
            mgba.press_buttons(["Up"])
            time.sleep(0.55)
            p = check_pos()
            
            if p == {"x": 5, "y": 9}:
                print("At (5, 9). Trying UP to (5, 8)...")
                mgba.press_buttons(["Up"])
                time.sleep(0.55)
                p = check_pos()
                
                if p == {"x": 5, "y": 8}:
                    print("SUCCESS! Column 5 Row 9 is OPEN! We are in State B!")
                    # Continue up to Row 3
                    steps_up = [
                        ("Up", {"x": 5, "y": 7}),
                        ("Up", {"x": 5, "y": 6}),
                        ("Up", {"x": 5, "y": 5}),
                        ("Up", {"x": 5, "y": 4}),
                        ("Up", {"x": 5, "y": 3}),
                    ]
                    for d, expected in steps_up:
                        mgba.press_buttons([d])
                        time.sleep(0.55)
                        # Handle wild battle if any
                        scr = mgba.take_screenshot()
                        from PIL import Image
                        img = Image.open(scr).resize((160, 144), Image.Resampling.NEAREST)
                        black_or_white = 0
                        total_pixels = 0
                        for y in range(115, 140):
                            for x in range(10, 150):
                                r, g, b = img.getpixel((x, y))
                                total_pixels += 1
                                if (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200):
                                    black_or_white += 1
                        if black_or_white / total_pixels > 0.90:
                            print("Battle detected during climbing! Stopping script.")
                            exit(1)
                        p = check_pos()
                        if p != expected:
                            print(f"Failed to reach {expected}, actual: {p}")
                            exit(1)
                    print("Reached (5, 3)! Now we can cross horizontally to 2F East!")
                    
                else:
                    print("BLOCKED at (5, 9) trying to go UP to (5, 8). We are in State A!")
                    # Walk back down to (5, 11)
                    mgba.press_buttons(["Down"])
                    time.sleep(0.55)
            else:
                print("BLOCKED at (5, 10) trying to go UP to (5, 9).")
        else:
            print("BLOCKED at (5, 11) trying to go UP to (5, 10). Trying stairs at (7, 10)...")
            # If Column 5 Row 10 is blocked, let's try (7, 10) stairs
            steps_stairs = [
                ("Right", {"x": 6, "y": 11}),
                ("Right", {"x": 7, "y": 11}),
                ("Up", {"x": 7, "y": 10}),
            ]
            for d, expected in steps_stairs:
                mgba.press_buttons([d])
                time.sleep(1.5 if d == "Up" else 0.55)
                p = check_pos()
                if p != expected:
                    # Check if we successfully warped to 3F West!
                    # 3F West landing is at (7, 11) on 3F West!
                    # But wait, how do we distinguish 2F (7, 11) from 3F (7, 11)?
                    # We can take a screenshot or check tiles.
                    # On 3F West at (7, 11), Column 6 Row 11 is red checkerboard. On 2F, it is pink.
                    print(f"Failed to reach expected {expected}, current position: {p}")
                    break
else:
    print("Not starting at (6, 11)")
