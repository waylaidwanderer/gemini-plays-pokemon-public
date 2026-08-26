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

# Let's try walking Left on Row 10 to map walkable columns
for col in range(4, 0, -1):
    mgba.press_buttons(["Left"])
    time.sleep(0.55)
    p = check_pos()
    if p["x"] == col:
        print(f"Column {col} Row 10 is walkable!")
        # Try going UP from this column
        mgba.press_buttons(["Up"])
        time.sleep(0.55)
        p_up = check_pos()
        if p_up["y"] == 9:
            print(f"Column {col} Row 9 is OPEN in State A!")
            # Walk back down
            mgba.press_buttons(["Down"])
            time.sleep(0.55)
        else:
            print(f"Column {col} Row 9 is CLOSED/Blocked in State A")
    else:
        print(f"Column {col} Row 10 is BLOCKED!")
        break

print("Left side exploration done!")
