import mgba

print("Starting Master Route 8 Navigation Probe...")

pos = mgba.get_coordinates()
print(f"Current Position: {pos}")

# Step 1: Walk East on Row 14/15 to map wrap / Lavender Town
for i in range(35):
    pos = mgba.get_coordinates()
    if pos['x'] == 0 and pos['y'] == 9:
        print(f"Warped to Lavender Town at {pos}!")
        break
    mgba.press_buttons(["Right"])

pos = mgba.get_coordinates()
print(f"Position after East sweep: {pos}")
