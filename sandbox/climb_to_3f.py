import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    for _ in range(8):
        mgba.press_buttons(["B", "sleep 150"])
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 800"])
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 4:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

# Starting at (5, 10) on 2F West
print("Starting on 2F West:", get_pos())

# 1. Walk Down to (5, 11)
walk_step("Down")
print("Position 1:", get_pos())

# 2. Walk Right to (7, 11)
for _ in range(2):
    walk_step("Right")
print("Position 2:", get_pos())

# 3. Step UP onto the stairs at (7, 10) to warp UP to 3F West
print("Stepping UP onto stairs at (7, 10)...")
mgba.press_buttons(["Up", "sleep 600"])
time.sleep(1.5)

print("Final position on 3F West:", get_pos())
sc = mgba.take_screenshot()
print("Screenshot:", sc)
