import mgba

print("Starting Lower Highway Westbound Probe...")
pos = mgba.get_coordinates()
print(f"Start Position: {pos}")

# Step 1: Walk Down to Row 14
for i in range(14 - pos['y']):
    mgba.press_buttons(["Down"])
    print(f"Down step: {mgba.get_coordinates()}")

# Step 2: Walk Left along Row 14 toward Column 3
current = mgba.get_coordinates()
for step in range(1, 45):
    mgba.press_buttons(["Left"])
    new_pos = mgba.get_coordinates()
    print(f"Left step {step}: {new_pos}")
    if new_pos['x'] == current['x'] and new_pos['y'] == current['y']:
        print(f"BUMP at {new_pos}! Trying bypass via Down 1, Left 2, Up 1...")
        mgba.press_buttons(["Down", "Left", "Left", "Up"])
        current = mgba.get_coordinates()
        print(f"After bypass: {current}")
    else:
        current = new_pos
    if current['x'] <= 3:
        print(f"SUCCESS! Reached Column {current['x']} at {current}!")
        break
