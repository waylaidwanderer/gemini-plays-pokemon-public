import mgba

print("=== ROCK TUNNEL B1F EAST-SOUTH EXIT PROBE ===")
start = mgba.get_coordinates()
print(f"Start pos: {start}")

for target_x in range(21, 32):
    curr = mgba.get_coordinates()
    while curr['x'] < target_x:
        mgba.press_buttons(["Right"])
        curr = mgba.get_coordinates()
        
    print(f"Testing at ({curr['x']}, {curr['y']})...")
    
    mgba.press_buttons(["Down"])
    p_down = mgba.get_coordinates()
    if p_down['y'] > curr['y']:
        print(f"SUCCESS! SOUTHBOUND PASSAGE FOUND AT ({curr['x']}, {curr['y']}) DOWN -> {p_down}")
        c = p_down
        while True:
            mgba.press_buttons(["Down"])
            c2 = mgba.get_coordinates()
            if c2['y'] > c['y']:
                c = c2
                print(f"  Climbed deeper South -> {c}")
            else:
                break
        print(f"Deepest South reached from x={target_x}: {c}")
        if c['y'] >= 12:
            print(f"FOUND MAJOR SOUTHBOUND HIGHWAY AT {c}!")
            break
        else:
            while mgba.get_coordinates()['y'] > curr['y']:
                mgba.press_buttons(["Up"])

print("=== PROBE COMPLETE ===")
print(f"Final pos: {mgba.get_coordinates()}")
