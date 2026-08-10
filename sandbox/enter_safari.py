import time
import bridge

print("Running enter_safari.py to go through dialogue and enter Safari Zone...")

# We are at (3, 2) with 'Welcome to the SAFARI ZONE!' text box open.
# Step 1: Go through dialogue and pay 500
print("1. Dismissing welcome message...")
bridge.press_buttons(["A"])
time.sleep(0.6)

# The YES/NO box is now open. Press A to select YES (default).
print("2. Selecting YES...")
bridge.press_buttons(["A"])
time.sleep(0.6)

print("3. Going through 'That'll be 500' message...")
bridge.press_buttons(["A"])
time.sleep(0.6)

print("4. Going through 'ACE received 30 SAFARI BALLs' message...")
bridge.press_buttons(["A"])
time.sleep(0.6)

print("5. Going through 'We'll call you on the PA' message...")
bridge.press_buttons(["A"])
time.sleep(0.6)

print("6. Going through 'Best of luck!' message...")
bridge.press_buttons(["A"])
time.sleep(1.2) # Wait for text box to close completely

# Step 2: Walk UP to enter the Safari Zone
print("7. Walking UP to enter the Safari Zone...")
for _ in range(3):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
time.sleep(2.0) # Wait for transition warp

coords = bridge.get_coordinates()
print(f"Final coordinates inside Safari Zone: {coords}")

