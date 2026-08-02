import mgba

print("--- Starting Route 9 Basin Exit Probe ---")
start_pos = mgba.get_coordinates()
print(f"Start pos: {start_pos}")

exits_found = []

for x in range(10, 54):
    curr = mgba.get_coordinates()
    
    # Adjust y to 14
    if curr['y'] < 14:
        mgba.press_buttons(["Down"])
    elif curr['y'] > 14:
        mgba.press_buttons(["Up"])
        
    curr = mgba.get_coordinates()
    if curr['x'] < x:
        steps = ["Right"] * (x - curr['x'])
        mgba.press_buttons(steps)
    elif curr['x'] > x:
        steps = ["Left"] * (curr['x'] - x)
        mgba.press_buttons(steps)
        
    curr = mgba.get_coordinates()
    if curr['x'] != x or curr['y'] != 14:
        print(f"Could not reach ({x}, 14), currently at {curr}")
        continue
        
    # Test UP
    mgba.press_buttons(["Up"])
    pos_up = mgba.get_coordinates()
    if pos_up != {'x': x, 'y': 14}:
        print(f"EXIT UP at ({x}, 14) -> {pos_up}")
        exits_found.append((x, 14, "UP", pos_up))
        if pos_up['y'] < 14:
            mgba.press_buttons(["Down"])
        elif pos_up['y'] > 14:
            mgba.press_buttons(["Up"])
        elif pos_up['x'] < x:
            mgba.press_buttons(["Right"])
        elif pos_up['x'] > x:
            mgba.press_buttons(["Left"])

    # Test DOWN
    curr = mgba.get_coordinates()
    if curr == {'x': x, 'y': 14}:
        mgba.press_buttons(["Down"])
        pos_down = mgba.get_coordinates()
        if pos_down != {'x': x, 'y': 14}:
            print(f"EXIT DOWN at ({x}, 14) -> {pos_down}")
            exits_found.append((x, 14, "DOWN", pos_down))
            if pos_down['y'] < 14:
                mgba.press_buttons(["Down"])
            elif pos_down['y'] > 14:
                mgba.press_buttons(["Up"])
            elif pos_down['x'] < x:
                mgba.press_buttons(["Right"])
            elif pos_down['x'] > x:
                mgba.press_buttons(["Left"])

print(f"Probe finished! Exits found: {exits_found}")
final_pos = mgba.get_coordinates()
print(f"Final position: {final_pos}")
