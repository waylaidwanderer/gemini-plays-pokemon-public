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
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 3:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

# Starting at (5, 11) on 3F West, bypassing the NPC at (4, 11)
print("Bypassing NPC and toggling 3F West switch...")

# 1. Down to (5, 12)
try_step("Down")
# 2. Left to (4, 12)
try_step("Left")
# 3. Left to (3, 12)
try_step("Left")
# 4. Down to (3, 13)
try_step("Down")
# 5. Left to (2, 13)
try_step("Left")
# 6. Left to (1, 13)
try_step("Left")
# 7. Up to (1, 12)
try_step("Up")
# 8. Up to (1, 11)
try_step("Up")

print("Arrived at target spot:", get_pos())

# Face Right to face the switch
mgba.press_buttons(["Right", "sleep 200"])
# Toggle switch
mgba.press_buttons(["A", "sleep 400", "B", "sleep 200"])
print("Switch toggled! Current position and heading:", get_pos())

# Walk to 3F East via Row 9
print("Crossing 3F West Row 9 to 3F East...")
# 1. Down to (1, 12)
try_step("Down")
# 2. Down to (1, 13)
try_step("Down")
# 3. Right to (2, 13)
try_step("Right")
# 4. Right to (3, 13)
try_step("Right")
# 5. Up to (3, 12)
try_step("Up")
# 6. Up to (3, 11)
try_step("Up")
# 7. Up to (3, 10)
try_step("Up")
# 8. Up to (3, 9)
try_step("Up")
# 9. Left to (2, 9)
try_step("Left")
# 10. Left to (1, 9)
try_step("Left")

print("Arrived at Row 9, Column 1:", get_pos())

# Face Right to walk across Row 9 (now open in State B!)
# Try 12 steps Right to walk all the way to 3F East (12, 9)
for i in range(12):
    try_step("Right")
    print(f"Right step {i+1} completed. Pos:", get_pos())

sc = mgba.take_screenshot()
print("Final screenshot after Row 9 crossing:", sc)
