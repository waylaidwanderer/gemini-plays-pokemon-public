import time
import bridge

print("Starting go_to_gatehouse_from_slowpoke.py...")

# Step 1: Dismiss the Slowpoke text box
print("Dismissing text box...")
bridge.press_buttons(["B"])
time.sleep(0.8)

# Step 2: Walk DOWN to exit the house
print("Exiting Slowpoke Fan's House...")
for _ in range(5):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
time.sleep(2.0) # Wait for map transition

pos = bridge.get_coordinates()
print(f"Coordinates outside: {pos} (should be (22, 14))")

if pos is not None:
    # Step 3: Walk Right 4 steps to Column 26
    print("Walking RIGHT to Column 26...")
    for _ in range(4):
        bridge.press_buttons(["Right"])
        time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 4: Walk Up 5 steps to Row 9
    print("Walking UP to Row 9...")
    for _ in range(5):
        bridge.press_buttons(["Up"])
        time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 5: Walk Left 7 steps to Column 19
    print("Walking LEFT to Column 19...")
    for _ in range(7):
        bridge.press_buttons(["Left"])
        time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 6: Walk Up 1 step to Row 8
    print("Walking UP to Row 8...")
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 7: Walk Right 18 steps to Column 37
    print("Walking RIGHT to Column 37...")
    for _ in range(18):
        bridge.press_buttons(["Right"])
        time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 8: Walk Up 6 steps to Row 2
    print("Walking UP to Row 2...")
    for _ in range(6):
        bridge.press_buttons(["Up"])
        time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 9: Walk Left 15 steps to Column 22
    print("Walking LEFT to Column 22...")
    for _ in range(15):
        bridge.press_buttons(["Left"])
        time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 10: Walk Down 2 steps to Row 4
    print("Walking DOWN to Row 4...")
    for _ in range(2):
        bridge.press_buttons(["Down"])
        time.sleep(0.6)
    pos = bridge.get_coordinates()
    print(f"Coordinates: {pos}")
    
    # Step 11: Walk Up to enter Gatehouse
    print("Entering Gatehouse...")
    bridge.press_buttons(["Up"])
    time.sleep(2.5)
    
    pos = bridge.get_coordinates()
    print(f"Coordinates inside Gatehouse: {pos}")
else:
    print("Failed to get coordinates outside.")
