import mgba

print("=== ROCK TUNNEL B1F SOUTHBOUND PASSAGE PROBE ===")
start = mgba.get_coordinates()
print(f"Start pos: {start}")

for target_x in range(21, 28):
    curr = mgba.get_coordinates()
    while curr['x'] < target_x:
        mgba.press_buttons(["Right"])
        curr = mgba.get_coordinates()
    print(f"At ({curr['x']}, {curr['y']})...")
    
    mgba.press_buttons(["Down"])
    p_down = mgba.get_coordinates()
    if p_down['y'] > curr['y']:
        print(f"SUCCESS! SOUTHBOUND PASSAGE FOUND AT ({curr['x']}, {curr['y']}) DOWN -> {p_down}")
        while p_down['y'] < 16:
            mgba.press_buttons(["Down"])
            p_down = mgba.get_coordinates()
            print(f"  South step -> {p_down}")
        break

print("=== PROBE COMPLETE ===")
print(f"Final pos: {mgba.get_coordinates()}")
