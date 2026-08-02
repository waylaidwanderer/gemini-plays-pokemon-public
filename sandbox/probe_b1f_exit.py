import mgba

print("=== ROCK TUNNEL B1F EAST-SOUTH EXIT PROBE ===")
start = mgba.get_coordinates()
print(f"Start pos: {start}")

# 1. Up to y=5
while start['y'] > 5:
    mgba.press_buttons(["Up"])
    start = mgba.get_coordinates()
    print(f"Up step -> {start}")

# 2. Right to x=31 along Row 5
while start['x'] < 31:
    mgba.press_buttons(["Right"])
    start = mgba.get_coordinates()
    print(f"Right step -> {start}")

# 3. Down to y=7 at x=31
while start['y'] < 7:
    mgba.press_buttons(["Down"])
    start = mgba.get_coordinates()
    print(f"Down step -> {start}")

# 4. Probe DOWN at x=31, 30, 29, 28, 27, 26, 25, 24
for target_x in range(31, 23, -1):
    curr = mgba.get_coordinates()
    while curr['x'] > target_x:
        mgba.press_buttons(["Left"])
        curr = mgba.get_coordinates()
    print(f"At ({curr['x']}, {curr['y']})...")
    
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
