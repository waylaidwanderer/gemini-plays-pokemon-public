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

# Starting at (5, 11) on 3F West in State A
print("Starting script to toggle switch on 3F East and drop...")

# 1. Walk Right along Row 11 to (12, 11) on 3F East
print("Walking to (12, 11)...")
for _ in range(7):
    try_step("Right")
print("Position:", get_pos())

# 2. Face Up towards the switch at (12, 10)
print("Facing Up towards the switch...")
mgba.press_buttons(["Up", "sleep 250"])

# 3. Examine and toggle the switch to State B
print("Toggling the switch at (12, 10)...")
mgba.press_buttons(["A", "sleep 2500"]) # Wait for text to print
mgba.press_buttons(["A", "sleep 2500"]) # Press Yes
mgba.press_buttons(["B", "sleep 500"]) # Close text
print("Switch toggled!")

# 4. Walk Up to Row 6 (now open in State B!)
print("Walking Up to Row 6...")
for _ in range(5):
    try_step("Up")
print("Position on Row 6:", get_pos())

# 5. Walk Right to pitfall at (26, 6)
print("Walking to pitfall at (26, 6)...")
for _ in range(14):
    try_step("Right")
print("Position at pitfall (should have dropped to 1F East):", get_pos())

sc = mgba.take_screenshot()
print("Final Screenshot:", sc)
