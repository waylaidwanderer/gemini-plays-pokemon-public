import time
import bridge

print("Starting enter_safari_real.py...")

# Verify starting coordinates are (3, 5)
pos = bridge.get_coordinates()
print(f"Current coordinates: {pos}")
if pos != (3, 5):
    print("Warning: Not starting at (3, 5)!")

# Step 1: Walk to the counter at (6, 4)
print("1. Walking to the counter...")
bridge.press_buttons(["Up"])
time.sleep(0.6)

for _ in range(3):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
    
pos = bridge.get_coordinates()
print(f"Coordinates: {pos} (should be (6, 4))")

# Step 2: Talk to the Gatekeeper clerk at (6, 2)
print("2. Facing UP and talking to clerk...")
bridge.press_buttons(["Up", "sleep 300", "A"])
time.sleep(1.5)

# Step 3: Dismiss welcome message
print("3. Dismissing welcome message...")
bridge.press_buttons(["A"])
time.sleep(1.0)

# YES/NO prompt. Select YES (default).
print("4. Selecting YES...")
bridge.press_buttons(["A"])
time.sleep(1.0)

# Dismiss "That'll be 500"
print("5. Dismissing 'That'll be 500' message...")
bridge.press_buttons(["A"])
time.sleep(1.0)

# Dismiss "ACE received 30 SAFARI BALLs"
print("6. Dismissing 'ACE received 30 SAFARI BALLs' message...")
bridge.press_buttons(["A"])
time.sleep(1.0)

# Dismiss "We'll call you on the PA"
print("7. Dismissing 'We'll call you on the PA' message...")
bridge.press_buttons(["A"])
time.sleep(1.0)

# Dismiss "Best of luck!"
print("8. Dismissing 'Best of luck!' message...")
bridge.press_buttons(["A"])
time.sleep(2.0) # Wait for text box to close completely

# Step 4: Walk LEFT and UP to enter the Safari Zone
print("9. Walking to the Safari Zone entrance...")
for _ in range(3):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
    
for _ in range(4):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
time.sleep(2.5) # Wait for transition warp

coords = bridge.get_coordinates()
print(f"Final coordinates inside Safari Zone: {coords}")
