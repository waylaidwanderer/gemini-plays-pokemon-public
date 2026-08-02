import mgba

print("=== ROCK TUNNEL B1F (22, 13) ROUTE PROBE ===")
pos = mgba.get_coordinates()
print(f"Start pos: {pos}")

# 1. Left to x=20
while pos['x'] > 20:
    mgba.press_buttons(["Left"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Left at {pos}")
        break
    pos = nxt
    print(f"Left step -> {pos}")

# 2. Up to y=11
while pos['y'] > 11:
    mgba.press_buttons(["Up"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Up at {pos}")
        break
    pos = nxt
    print(f"Up step -> {pos}")

# 3. Try moving Left along Row 11 towards x=17
while pos['x'] > 17:
    mgba.press_buttons(["Left"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Left at {pos}")
        break
    pos = nxt
    print(f"Left step -> {pos}")

# 4. If reached (17, 11), try moving Down to Row 16
if pos == {'x': 17, 'y': 11}:
    print("Reached (17, 11) ladder tile!")
else:
    mgba.press_buttons(["Down"])
    print(f"From {pos} DOWN -> {mgba.get_coordinates()}")

print("=== PROBE COMPLETE ===")
print(f"Final pos: {mgba.get_coordinates()}")
