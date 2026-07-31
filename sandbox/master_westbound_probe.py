import mgba

print("Starting Master Westbound Single-Step Probe...")
pos = mgba.get_coordinates()
print(f"Start Position: {pos}")

# Step 1: Walk Down to Row 15 at (50, 15)
for i in range(15 - pos['y']):
    mgba.press_buttons(["Down"])
    print(f"Down step: {mgba.get_coordinates()}")

# Step 2: Walk Left along Row 15 toward Column 19
current = mgba.get_coordinates()
for step in range(1, 35):
    mgba.press_buttons(["Left"])
    new_pos = mgba.get_coordinates()
    print(f"Left step {step}: {new_pos}")
    if new_pos['x'] == current['x'] and new_pos['y'] == current['y']:
        print(f"COLLISION at {new_pos}! Trying bypass via Up 1...")
        mgba.press_buttons(["Up", "Left", "Left", "Down"])
        current = mgba.get_coordinates()
        print(f"After bypass: {current}")
    else:
        current = new_pos
    if current['x'] <= 19:
        print(f"REACHED COLUMN 19 at {current}!")
        break
