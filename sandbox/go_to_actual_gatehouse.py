import time
import bridge

print("Starting go_to_actual_gatehouse.py...")

# Step 1: Dismiss Slowpoke text screens
print("Dismissing first text screen...")
bridge.press_buttons(["B"])
time.sleep(1.0)

print("Dismissing second text screen...")
bridge.press_buttons(["B"])
time.sleep(1.0)

# Step 2: Navigate out of the Slowpoke Fan's House
print("Walking to the exit mat...")
# Currently at (4, 3) logically (or (4, 2) according to RAM, but let's walk safely)
# We walk Left, Down, Down, Right, Down
bridge.press_buttons(["Left"])
time.sleep(0.6)
bridge.press_buttons(["Down"])
time.sleep(0.6)
bridge.press_buttons(["Down"])
time.sleep(0.6)
bridge.press_buttons(["Right"])
time.sleep(0.6)
bridge.press_buttons(["Down"])
time.sleep(0.6)

# Step into the exit mat
print("Exiting house...")
bridge.press_buttons(["Down"])
time.sleep(2.5) # Wait for map transition

pos = bridge.get_coordinates()
print(f"Coordinates outside: {pos} (should be (22, 14))")

if pos is not None:
    # Step 3: Walk to the bush at (26, 14)
    print("Walking to (26, 14)...")
    for _ in range(4):
        bridge.press_buttons(["Right"])
        time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 4: Face UP and CUT
    print("Facing UP...")
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
    
    print("Opening Start menu and using CUT...")
    # Menu sequence: Start -> A (POKéMON) -> Down (TRUFFLE) -> A -> Down (CUT) -> A -> A (dismiss text)
    bridge.press_buttons([
        "Start", "sleep 500",
        "A", "sleep 1200",
        "Down", "sleep 500",
        "A", "sleep 1200",
        "Down", "sleep 500",
        "A", "sleep 3000",
        "A", "sleep 1000",
        "A", "sleep 1000"
    ])
    time.sleep(1.5)
    
    # Step 5: Walk UP Column 26 to Row 9
    print("Walking UP to Row 9...")
    for _ in range(5):
        bridge.press_buttons(["Up"])
        time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 6: Walk Left to Column 19
    print("Walking LEFT to Column 19...")
    for _ in range(7):
        bridge.press_buttons(["Left"])
        time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 7: Walk Up to Row 8
    print("Walking UP to Row 8...")
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 8: Walk Right to Column 37
    print("Walking RIGHT to Column 37...")
    for _ in range(18):
        bridge.press_buttons(["Right"])
        time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 9: Walk Up to Row 2
    print("Walking UP to Row 2...")
    for _ in range(6):
        bridge.press_buttons(["Up"])
        time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 10: Walk Left to Column 18
    print("Walking LEFT to Column 18...")
    for _ in range(19):
        bridge.press_buttons(["Left"])
        time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 11: Walk Down to Row 4
    print("Walking DOWN to Row 4...")
    for _ in range(2):
        bridge.press_buttons(["Down"])
        time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 12: Enter Gatehouse
    print("Entering ACTUAL Safari Gatehouse...")
    bridge.press_buttons(["Up"])
    time.sleep(2.5)
    
    pos = bridge.get_coordinates()
    print(f"Coordinates inside actual Gatehouse: {pos}")
else:
    print("Failed to exit house or get coordinates.")
