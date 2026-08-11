import time
import bridge

print("Starting enter_safari_v3.py...")

# Check current coordinates (should be (4, 7))
pos = bridge.get_coordinates()
print(f"Current coordinates: {pos}")
if pos != (4, 7):
    print("Warning: Not starting at (4, 7)!")

# Step 1: Walk to (4, 3) via the Column 3 gap
print("1. Walking to (4, 3)...")
bridge.press_buttons(["Left"])
time.sleep(0.6)

for _ in range(4):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
    
bridge.press_buttons(["Right"])
time.sleep(0.6)

pos = bridge.get_coordinates()
print(f"Coordinates: {pos} (should be (4, 3))")

# Step 2: Talk to the clerk at (4, 2)
print("2. Talking to the Gatekeeper clerk...")
bridge.press_buttons(["Up", "sleep 300", "A"])
time.sleep(1.5)

# Step 3: Go through dialogue and pay 500
print("3. Dismissing welcome message...")
bridge.press_buttons(["A"])
time.sleep(1.0)

# YES/NO prompt. Select YES (default).
print("4. Selecting YES...")
bridge.press_buttons(["A"])
time.sleep(1.0)

print("5. Dismissing 'That'll be 500' message...")
bridge.press_buttons(["A"])
time.sleep(1.0)

print("6. Dismissing 'ACE received 30 SAFARI BALLs' message...")
bridge.press_buttons(["A"])
time.sleep(1.0)

print("7. Dismissing 'We'll call you on the PA' message...")
bridge.press_buttons(["A"])
time.sleep(1.0)

print("8. Dismissing 'Best of luck!' message...")
bridge.press_buttons(["A"])
time.sleep(2.0) # Wait for text box to close completely

# Step 4: Walk UP to enter the Safari Zone
print("9. Walking UP to enter the Safari Zone...")
for _ in range(3):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
time.sleep(2.5) # Wait for transition warp

coords = bridge.get_coordinates()
print(f"Final coordinates inside Safari Zone: {coords}")
