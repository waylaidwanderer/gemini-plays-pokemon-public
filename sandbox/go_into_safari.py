import time
import bridge

print("Running go_into_safari.py...")

# Step 1: Walk UP to (4, 2) to trigger dialogue
print("Walking UP to (4, 2) to talk to the gatekeeper...")
bridge.press_buttons(["Up"])
time.sleep(1.0)

# Step 2: Go through the dialogue and pay 500
# There are about 5-6 text boxes
print("Dismissing welcome message and selecting YES...")
bridge.press_buttons(["A"])
time.sleep(0.6)

# The Yes/No box is now open. Press A to select YES (which is default).
print("Selecting YES...")
bridge.press_buttons(["A"])
time.sleep(0.6)

print("Going through 'That'll be 500' message...")
bridge.press_buttons(["A"])
time.sleep(0.6)

print("Going through 'ACE received 30 SAFARI BALLS' message...")
bridge.press_buttons(["A"])
time.sleep(0.6)

print("Going through 'We'll call you on the PA' message...")
bridge.press_buttons(["A"])
time.sleep(0.6)

print("Going through 'Best of luck!' message...")
bridge.press_buttons(["A"])
time.sleep(1.2) # Wait for text box to close completely

# Now we should be free to walk UP to enter the Safari Zone
print("Walking UP to enter the Safari Zone...")
bridge.press_buttons(["Up"])
time.sleep(2.0) # Wait for transition warp

coords = bridge.get_coordinates()
print(f"Final coordinates inside Safari Zone: {coords}")
