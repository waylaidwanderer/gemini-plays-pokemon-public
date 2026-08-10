import time
import bridge

print("Running go_into_safari.py (Gatehouse -> Safari Zone)...")

# We are at (4, 2) with 'We'll call you on the PA when you run out of time or SAFARI BALLS!' open.
# Step 1: Dismiss dialogue
print("Dismissing 'We'll call you on the PA...' message...")
bridge.press_buttons(["A"])
time.sleep(0.8)

# Now 'Best of luck!' message is open. Press A to dismiss it.
print("Dismissing 'Best of luck!' message...")
bridge.press_buttons(["A"])
time.sleep(1.2) # Wait for text box to close completely

# Step 2: Walk UP to enter the Safari Zone Center
print("Walking UP to enter the Safari Zone...")
for _ in range(3):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
time.sleep(2.0) # Wait for transition loading

coords = bridge.get_coordinates()
print(f"Final coordinates inside Safari Zone Center: {coords}")
