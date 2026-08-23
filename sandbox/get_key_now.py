import mgba
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
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

def walk_to(target_x, target_y):
    print(f"Walking to: ({target_x}, {target_y})")
    max_steps = 100
    steps = 0
    while steps < max_steps:
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        if x == target_x and y == target_y:
            return True
            
        if x < target_x:
            try_step("Right")
        elif x > target_x:
            try_step("Left")
        elif y < target_y:
            try_step("Down")
        elif y > target_y:
            try_step("Up")
        steps += 1
    return False

# Starting on B1F East inside "Got away safely!" textbox at (22, 3)
print("Starting ultimate Secret Key sequence from (22, 3)...")

# 0. Clear the "Got away safely!" textbox
mgba.press_buttons(["B", "sleep 250"])

# 1. Walk to switch at (15, 7)
print("Walking to (22, 7)...")
walk_to(22, 7)
print("Walking to (15, 7)...")
walk_to(15, 7)
print("Position before switch:", get_pos())

# 2. Face UP and toggle switch to State B
print("Toggling switch to State B...")
mgba.press_buttons(["Up", "sleep 250"]) # Face UP
mgba.press_buttons(["A", "sleep 2500"]) # Wait for text to print
mgba.press_buttons(["A", "sleep 2500"]) # Press Yes
mgba.press_buttons(["B", "sleep 500"])  # Close text
print("State B active!")

# 3. Walk to Row 5 Column 15
print("Walking UP to Row 5...")
try_step("Up")
try_step("Up")

# 4. Walk LEFT along Row 5 to (1, 5)
print("Walking LEFT to Secret Key room...")
walk_to(1, 5)
print("Position at Secret Key room:", get_pos())

# 5. Face UP and retrieve Secret Key at (1, 4)
print("Retrieving Secret Key...")
mgba.press_buttons(["Up", "sleep 250"]) # Face UP
mgba.press_buttons(["A", "sleep 500", "B", "sleep 500"]) # Secret Key text
mgba.press_buttons(["A", "sleep 500", "B", "sleep 500"]) # Secret Key retrieved text
print("Secret Key retrieved!")

# 6. DIG out back to Cinnabar Island
print("Escaping via DIG...")
mgba.press_buttons(["Start", "sleep 300"])
mgba.press_buttons(["Down", "sleep 150", "A", "sleep 600"]) # Select POKéMON
for _ in range(5): # 5 Down presses to select TRUFFLE (Slot 6)
    mgba.press_buttons(["Down", "sleep 150"])
mgba.press_buttons(["A", "sleep 500"]) # Select TRUFFLE
mgba.press_buttons(["A", "sleep 1000"]) # Select DIG
time.sleep(3.0)

print("SUCCESS! Final position Cinnabar Island:", get_pos())
sc = mgba.take_screenshot()
print("Final Screenshot:", sc)
