import mgba

print("Executing Route 9 Row 6 West Probe...")
start = mgba.get_coordinates()
print(f"Start pos: {start}")

# 1. Walk East 19 steps on Row 14 from (10, 14) to (29, 14)
print("1. Walking East to (29, 14)...")
mgba.press_buttons(["Right"] * 19)
p1 = mgba.get_coordinates()
print(f"At: {p1}")

# 2. Step UP to Row 12 at (29, 12)
print("2. Stepping UP to Row 12...")
mgba.press_buttons(["Up", "Up"])
p2 = mgba.get_coordinates()
print(f"At: {p2}")

# 3. Walk East 12 steps on Row 12 to (41, 12)
print("3. Walking East to (41, 12)...")
mgba.press_buttons(["Right"] * 12)
p3 = mgba.get_coordinates()
print(f"At: {p3}")

# 4. Step UP through Col 41 gap to Row 6 highway
print("4. Stepping UP Col 41 gap...")
mgba.press_buttons(["Up", "Up", "Up", "Up"])
p4 = mgba.get_coordinates()
print(f"At: {p4}")

# 5. Sweep WEST along Row 6 from current x down to 30, probing UP at each tile
print("5. Sweeping WEST along Row 6 testing UP at each tile...")
found = False
for i in range(15):
    curr = mgba.get_coordinates()
    print(f"\n--- Testing at x={curr['x']}, y={curr['y']} ---")
    
    # Try UP
    mgba.press_buttons(["Up"])
    p_up = mgba.get_coordinates()
    if p_up['y'] < curr['y']:
        print(f"*** ASCENT GAP FOUND at x={curr['x']}, moved UP to {p_up}! ***")
        mgba.take_screenshot()
        found = True
        break
        
    # Step Left
    mgba.press_buttons(["Left"])

final_pos = mgba.get_coordinates()
print(f"\nFinal position: {final_pos}")
