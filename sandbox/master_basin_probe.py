import mgba

print("Executing Master Route 9 Eastern Probe...")
start = mgba.get_coordinates()
print(f"Start pos: {start}")

# 1. Return to Row 12 at (29, 12)
print("1. Retracing to (29, 12)...")
mgba.press_buttons(["Down"] * 3) # from (25, 2) to (25, 5)
mgba.press_buttons(["Down"])     # to (25, 6)
mgba.press_buttons(["Right"] * 4) # to (29, 6)
mgba.press_buttons(["Down"] * 6) # to (29, 12)
p1 = mgba.get_coordinates()
print(f"At: {p1}")

# 2. Walk East on Row 12 to (41, 12)
print("2. Walking East to (41, 12)...")
mgba.press_buttons(["Right"] * 12)
p2 = mgba.get_coordinates()
print(f"At: {p2}")

# 3. Ascend Col 41 gap to Row 6 highway
print("3. Ascending Col 41 gap to Row 6...")
mgba.press_buttons(["Up"] * 4)
p3 = mgba.get_coordinates()
print(f"At: {p3}")

# 4. Probe EAST along Row 6/8 past x=41 towards x=59
print("4. Probing EAST along Row 6/8 past x=41...")
for i in range(25):
    curr = mgba.get_coordinates()
    print(f"Checking pos: {curr}")
    if curr['x'] >= 58:
        print(f"*** REACHED ROUTE 10 ENTRANCE AT {curr}! ***")
        mgba.take_screenshot()
        break
        
    # Try Right
    mgba.press_buttons(["Right"])
    after = mgba.get_coordinates()
    if after['x'] == curr['x']:
        # Bushed wall going Right. Try Up/Down to bypass
        print(f"Bumped at {curr}, trying Up...")
        mgba.press_buttons(["Up", "Right"])
        a_up = mgba.get_coordinates()
        if a_up['x'] == curr['x']:
            print(f"Bumped Up, trying Down...")
            mgba.press_buttons(["Down", "Down", "Right"])

final = mgba.get_coordinates()
print(f"Final pos: {final}")
