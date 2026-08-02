import mgba

print("=== ROCK TUNNEL B1F ROW 4 EAST/SOUTH PROBE ===")
start = mgba.get_coordinates()
print(f"Start pos: {start}")

# 1. Up to y=4
while start['y'] > 4:
    mgba.press_buttons(["Up"])
    start = mgba.get_coordinates()
    print(f"Up step -> {start}")

# 2. Walk East along Row 4 testing DOWN at each x from 20 to 30
for target_x in range(20, 31):
    curr = mgba.get_coordinates()
    while curr['x'] < target_x:
        mgba.press_buttons(["Right"])
        curr = mgba.get_coordinates()
    print(f"At ({curr['x']}, {curr['y']})...")

    # Test Down
    mgba.press_buttons(["Down"])
    p_down = mgba.get_coordinates()
    if p_down['y'] > curr['y']:
        print(f"SUCCESS! SOUTHBOUND PASSAGE FOUND AT ({curr['x']}, {curr['y']}) DOWN -> {p_down}")
        while True:
            mgba.press_buttons(["Down"])
            nxt = mgba.get_coordinates()
            if nxt['y'] > p_down['y']:
                p_down = nxt
                print(f"  South step -> {p_down}")
            else:
                break
        if p_down['y'] >= 16:
            print(f"REACHED LOWER B1F HIGHWAY AT {p_down}!")
            break
        else:
            while mgba.get_coordinates()['y'] > 4:
                mgba.press_buttons(["Up"])

print("=== PROBE COMPLETE ===")
print(f"Final pos: {mgba.get_coordinates()}")
