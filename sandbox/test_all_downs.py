import mgba

print("Walking to Route 10 pocket...")
# 1. Walk from (20, 8) to (50, 14):
# Right 9 times to (29, 8)
# Down 6 times to (29, 14)
# Right 21 times to (50, 14)
mgba.press_buttons(["Right"] * 9 + ["Down"] * 6 + ["Right"] * 21)

pos = mgba.get_coordinates()
print(f"Arrived at: {pos}")

# 2. Test Down on Columns 50, 51, 52, 53
for target_x in [50, 51, 52, 53]:
    # Walk to target_x on Row 14, then Down to Row 15
    print(f"\nWalking to ({target_x}, 14)...")
    # We can use get_coordinates to navigate safely
    curr = mgba.get_coordinates()
    dx = target_x - curr['x']
    if dx > 0:
        mgba.press_buttons(["Right"] * dx)
    elif dx < 0:
        mgba.press_buttons(["Left"] * abs(dx))
        
    dy = 14 - curr['y']
    if dy > 0:
        mgba.press_buttons(["Down"] * dy)
    elif dy < 0:
        mgba.press_buttons(["Up"] * abs(dy))
        
    pos = mgba.get_coordinates()
    print(f"Now at: {pos}")
    
    # Walk Down to Row 15
    print("Walking Down to Row 15...")
    mgba.press_buttons(["Down"])
    pos = mgba.get_coordinates()
    print(f"Now at: {pos}")
    
    # Try walking Down to Row 16
    print("Testing Down to Row 16...")
    mgba.press_buttons(["Down"])
    new_pos = mgba.get_coordinates()
    print(f"After testing Down: {new_pos}")
    if new_pos['y'] > 15:
        print(f"SUCCESS! Walked Down from Column {target_x}!")
        break
    # Otherwise, return to Row 14 to move to next column
    if new_pos['y'] == 15:
        mgba.press_buttons(["Up"])
