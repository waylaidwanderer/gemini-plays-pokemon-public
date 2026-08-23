import mgba
import time

def run_from_battle():
    print("In battle! Running...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 100"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 500"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 100"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 5:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

# Starting at (11, 12)
print("Initial position:", mgba.get_coordinates())

# 1. Walk to (6, 13)
walk_step("Down")
for _ in range(5):
    walk_step("Left")

print("Arrived at Column 6:", mgba.get_coordinates())

# 2. Walk UP to (6, 3) and enter Mansion
for _ in range(11):
    walk_step("Up")

print("Entered Mansion! Current position:", mgba.get_coordinates())
sc = mgba.take_screenshot()
print("Screenshot:", sc)
