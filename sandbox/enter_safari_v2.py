import time
import bridge

print("Starting enter_safari_v2.py...")

# Check current coordinates (should be (4, 7))
pos = bridge.get_coordinates()
print(f"Current coordinates inside Gatehouse: {pos}")
if pos != (4, 7):
    print("Warning: Not starting at (4, 7)!")

# Step 1: Walk to (3, 2)
print("Walking to (3, 2)...")
bridge.press_buttons(["Left"])
time.sleep(0.6)

for _ in range(5):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
    
pos = bridge.get_coordinates()
print(f"Coordinates: {pos} (should be (3, 2))")

# Step 2: Talk to the Gatekeeper clerk
print("Talking to the Gatekeeper clerk...")
bridge.press_buttons(["Up", "sleep 300", "A"])
time.sleep(1.5)

# Step 3: Go through dialogue and pay 500
print("1. Dismissing welcome message...")
bridge.press_buttons(["A"])
time.sleep(1.0)

# The YES/NO box is now open. Press A to select YES (default).
print("2. Selecting YES...")
bridge.press_buttons(["A"])
time.sleep(1.0)

print("3. Going through 'That'll be 500' message...")
bridge.press_buttons(["A"])
time.sleep(1.0)

print("4. Going through 'ACE received 30 SAFARI BALLs' message...")
bridge.press_buttons(["A"])
time.sleep(1.0)

print("5. Going through 'We'll call you on the PA' message...")
bridge.press_buttons(["A"])
time.sleep(1.0)

print("6. Going through 'Best of luck!' message...")
bridge.press_buttons(["A"])
time.sleep(2.0) # Wait for text box to close completely

# Step 4: Walk UP to enter the Safari Zone
print("7. Walking UP to enter the Safari Zone...")
for _ in range(3):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
time.sleep(2.5) # Wait for transition warp

coords = bridge.get_coordinates()
print(f"Final coordinates inside Safari Zone: {coords}")
