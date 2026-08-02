import mgba

print("=== ROCK TUNNEL B1F EAST HIGHWAY PROBE ===")
pos = mgba.get_coordinates()
print(f"Start pos: {pos}")

# 1. Up to y=4
while pos['y'] > 4:
    mgba.press_buttons(["Up"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Up at {pos}")
        break
    pos = nxt
    print(f"Up step -> {pos}")

# 2. Right to x=31
while pos['x'] < 31:
    mgba.press_buttons(["Right"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Right at {pos}")
        break
    pos = nxt
    print(f"Right step -> {pos}")

# 3. Up to y=2
while pos['y'] > 2:
    mgba.press_buttons(["Up"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Up at {pos}")
        break
    pos = nxt
    print(f"Up step -> {pos}")

# 4. Right past x=31 to x=45 along Row 2
while pos['x'] < 45:
    mgba.press_buttons(["Right"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Right at {pos}")
        break
    pos = nxt
    print(f"Right step on Row 2 -> {pos}")

print(f"Final pos: {pos}")
