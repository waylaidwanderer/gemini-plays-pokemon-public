import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 100"])
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 500"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 100"])

def try_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        # Check if in battle
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 3:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

# Starting at (1, 11) on 3F West in State A
print("Starting definitive 3F switch toggle and drop script...")

# 1. Walk Down to Row 13
print("Walking to Row 13...")
try_step("Down")
try_step("Down")
print("Position:", get_pos())

# 2. Walk Right to Column 3
print("Walking to Column 3...")
try_step("Right")
try_step("Right")
print("Position:", get_pos())

# 3. Walk Up to Row 11
print("Walking to Row 11...")
try_step("Up")
try_step("Up")
print("Position:", get_pos())

# 4. Walk Right to Column 12 (3F East)
print("Walking to 3F East at (12, 11)...")
for _ in range(9):
    try_step("Right")
print("Position on 3F East:", get_pos())

# 5. Face Up towards the switch at (12, 10)
print("Facing Up towards the switch...")
mgba.press_buttons(["Up", "sleep 250"])

# 6. Examine and toggle the switch to State B
print("Toggling the switch at (12, 10)...")
mgba.press_buttons(["A", "sleep 2500"]) # Wait for text to print
mgba.press_buttons(["A", "sleep 2500"]) # Press Yes
mgba.press_buttons(["B", "sleep 500"]) # Close text
print("Switch toggled!")

# 7. Walk Up to Row 6
print("Walking to Row 6...")
for _ in range(5):
    try_step("Up")
print("Position on Row 6:", get_pos())

# 8. Walk Right to pitfall at (26, 6)
print("Walking to pitfall at (26, 6)...")
for _ in range(14):
    try_step("Right")
print("Position at pitfall (should have dropped to 1F East):", get_pos())

sc = mgba.take_screenshot()
print("Final Screenshot:", sc)
