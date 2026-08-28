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

# Dismiss "Got away safely!" text first
print("Dismissing 'Got away safely!'...")
mgba.press_buttons(["B", "sleep 500"])

# 1. Walk Left along Row 4 from Column 16 to Column 7
print("Walking Left to Column 7...")
for _ in range(9):
    safe_step("Left")

# 2. Walk Down Column 7 to Row 11
print("Walking Down to Row 11...")
for _ in range(7):
    safe_step("Down")

# 3. Step UP onto the stairs at (7, 10) to warp DOWN to 2F West
print("Stepping UP onto the stairs at (7, 10)...")
mgba.press_buttons(["Up"])
time.sleep(2.5)

print(f"Warp complete! Position on 2F West: {get_pos()}")
mgba.take_screenshot()
