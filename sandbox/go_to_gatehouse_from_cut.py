import time
import bridge

print("Starting go_to_gatehouse_from_cut.py...")

# Verify position is (26, 14)
pos = bridge.get_coordinates()
print(f"Current coordinates: {pos}")
if pos != (26, 14):
    print("Warning: Not starting at (26, 14)!")

# Step 6: Facing UP and using CUT...
print("Step 6: Executing CUT menu sequence...")
# Since the menu cursor was on ITEM last time, we press:
# Start -> Up (to POKéMON) -> A -> Down (to TRUFFLE) -> A -> A (to select CUT)
bridge.press_buttons([
    "Start", "sleep 400",
    "Up", "sleep 400",
    "A", "sleep 1000",
    "Down", "sleep 400",
    "A", "sleep 1000",
    "A", "sleep 2500"
])
time.sleep(1.0)

# Dismiss the CUT text
bridge.press_buttons(["A", "sleep 500", "A"])
time.sleep(1.5)

# Verify if we can walk Up now
print("Checking if we can walk UP...")
bridge.press_buttons(["Up"])
time.sleep(0.6)
pos = bridge.get_coordinates()
print(f"Coordinates after first step UP: {pos}")

# If we successfully walked Up, we should be at (26, 13)
if pos == (26, 13):
    print("Successfully CUT the bush and walked onto (26, 13)!")
    
    # Step 7: Walk UP to Row 9 (remaining 4 steps UP)
    print("Step 7: Walking UP to Row 9...")
    for _ in range(4):
        bridge.press_buttons(["Up"])
        time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 8: Walk Left to Column 19
    print("Step 8: Walking Left to Column 19...")
    for _ in range(7):
        bridge.press_buttons(["Left"])
        time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 9: Walk Up to Row 8
    print("Step 9: Walking Up to Row 8...")
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 10: Walk Right to Column 37
    print("Step 10: Walking Right to Column 37...")
    for _ in range(18):
        bridge.press_buttons(["Right"])
        time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 11: Walk Up to Row 2
    print("Step 11: Walking Up to Row 2...")
    for _ in range(6):
        bridge.press_buttons(["Up"])
        time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 12: Walk Left to Column 22
    print("Step 12: Walking Left to Column 22...")
    for _ in range(15):
        bridge.press_buttons(["Left"])
        time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 13: Walk Down to Row 4
    print("Step 13: Walking Down to Row 4...")
    for _ in range(2):
        bridge.press_buttons(["Down"])
        time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 14: Walk Up to enter Gatehouse
    print("Step 14: Entering Gatehouse...")
    bridge.press_buttons(["Up"])
    time.sleep(2.5)
    
    pos = bridge.get_coordinates()
    print(f"Coordinates inside Gatehouse: {pos}")
else:
    print("Failed to cut the bush or walk UP.")
