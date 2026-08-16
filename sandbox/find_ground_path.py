import mgba
import time

print("--- DIAGNOSING PATH TO EAST ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (0, 23) facing DOWN.
print("Starting at:", get_pos())

# Let's try walking DOWN to (0, 24)
mgba.press_buttons(["Down"])
time.sleep(0.4)
print("Position after Down:", get_pos())

# Now let's walk Right step-by-step and see where we get blocked
for step in range(25):
    pos_before = get_pos()
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    pos_after = get_pos()
    print(f"Step {step+1}: Tried Right. Pos before: {pos_before}, Pos after: {pos_after}")
    if pos_before == pos_after:
        print("Blocked! Let's try UP once to see if Row 23 is open...")
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        pos_up = get_pos()
        print("Pos after Up:", pos_up)
        if pos_up != pos_before:
            # We moved up. Now try going Right!
            mgba.press_buttons(["Right"])
            time.sleep(0.4)
            pos_r2 = get_pos()
            print("Tried Right on upper row. Pos:", pos_r2)
            if pos_r2 != pos_up:
                print("Successfully bypassed on upper row!")
                continue
            # If still blocked, go back down
            mgba.press_buttons(["Down"])
            time.sleep(0.4)
        
        print("Let's try DOWN once to see if Row 25 is open (if not blocked by trees)...")
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        pos_down = get_pos()
        print("Pos after Down:", pos_down)
        if pos_down != pos_before:
            mgba.press_buttons(["Right"])
            time.sleep(0.4)
            pos_r3 = get_pos()
            print("Tried Right on lower row. Pos:", pos_r3)
            if pos_r3 != pos_down:
                print("Successfully bypassed on lower row!")
                continue
            mgba.press_buttons(["Up"])
            time.sleep(0.4)
            
        print("Completely blocked vertically and horizontally at this column!")
        break

print("Diagnostic complete. Final position:", get_pos())
mgba.take_screenshot()
