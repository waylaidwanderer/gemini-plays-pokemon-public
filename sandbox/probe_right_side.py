import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def step(direction):
    old_pos = get_pos()
    print(f"Current: {old_pos}. Stepping {direction}...")
    mgba.press_buttons([direction])
    time.sleep(0.45)
    new_pos = get_pos()
    print(f"New position: {new_pos}")
    return new_pos

def run_away_or_battle():
    print("Dialogue/Battle detected! Clearing...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 600"])
    mgba.press_buttons(["B", "sleep 300"])

def safe_step(direction):
    old_pos = get_pos()
    new_pos = step(direction)
    if new_pos == old_pos:
        time.sleep(0.5)
        if get_pos() != old_pos:
            run_away_or_battle()
            time.sleep(1.0)
            return step(direction)
        else:
            print("BLOCKED physically")
            return old_pos
    return new_pos

# Walk from (16, 3) to Row 6:
# Down, Down, Down
print("Walking to Row 6 Column 16...")
safe_step("Down")
safe_step("Down")
safe_step("Down")

# Walk to Column 21 on Row 6
print("Walking to Column 21 on Row 6...")
for _ in range(5):
    safe_step("Right")

# Try to step Right to Column 22 on Row 6
print("Probing step Right from (21, 6) to (22, 6)...")
p_6 = safe_step("Right")
if p_6 != (21, 6):
    print("SUCCESS: Row 6 Column 22 is Walkable!")
    safe_step("Left") # Step back
else:
    print("Row 6 Column 22 is BLOCKED")

# Walk to Row 7 Column 21
print("Moving to Row 7 Column 21...")
safe_step("Down")

# Try to step Right to Column 22 on Row 7
print("Probing step Right from (21, 7) to (22, 7)...")
p_7 = safe_step("Right")
if p_7 != (21, 7):
    print("SUCCESS: Row 7 Column 22 is Walkable!")
    safe_step("Left")
else:
    print("Row 7 Column 22 is BLOCKED")

# Walk to Row 4 Column 21
print("Moving to Row 4 Column 21...")
safe_step("Up")
safe_step("Up")
safe_step("Up")

# Try to step Right to Column 22 on Row 4
print("Probing step Right from (21, 4) to (22, 4)...")
p_4 = safe_step("Right")
if p_4 != (21, 4):
    print("SUCCESS: Row 4 Column 22 is Walkable!")
    safe_step("Left")
else:
    print("Row 4 Column 22 is BLOCKED")

mgba.take_screenshot()
