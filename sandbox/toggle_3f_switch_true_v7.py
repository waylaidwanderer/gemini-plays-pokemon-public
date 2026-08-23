import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    # Clean running sequence in a single call to prevent overworld movement after battle ends
    mgba.press_buttons([
        "B", "sleep 150", "B", "sleep 150", "B", "sleep 150", 
        "Right", "sleep 150", "Down", "sleep 150", "A", "sleep 2000"
    ])

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

# Starting at (8, 13) on 3F West/East in State A
print("Resuming definitive 3F switch toggle and drop script from (8, 13)...")

# 1. Walk Up to Row 12 (8, 12)
print("Walking Up to Row 12...")
try_step("Up")
print("Position:", get_pos())

# 2. Walk Right to (12, 12) along Row 12 (which is open in State A!)
print("Walking Right to (12, 12)...")
for _ in range(4):
    try_step("Right")
print("Position:", get_pos())

# 3. Walk Up to (12, 11)
print("Walking Up to (12, 11)...")
try_step("Up")
print("Position:", get_pos())

# 4. Face Up towards the switch at (12, 10)
print("Facing Up towards the switch...")
mgba.press_buttons(["Up", "sleep 250"])

# 5. Examine and toggle the switch to State B
print("Toggling the switch at (12, 10)...")
mgba.press_buttons(["A", "sleep 2500"]) # Wait for text to print
mgba.press_buttons(["A", "sleep 2500"]) # Press Yes
mgba.press_buttons(["B", "sleep 500"]) # Close text
print("Switch toggled!")

# 6. Walk Up to Row 6 (now open in State B!)
print("Walking to Row 6...")
for _ in range(5):
    try_step("Up")
print("Position on Row 6:", get_pos())

# 7. Walk Right to pitfall at (26, 6)
print("Walking to pitfall at (26, 6)...")
for _ in range(14):
    try_step("Right")
print("Position at pitfall (should have dropped to 1F East):", get_pos())

sc = mgba.take_screenshot()
print("Final Screenshot:", sc)
