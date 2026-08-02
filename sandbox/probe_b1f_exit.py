import mgba

print("=== ROCK TUNNEL B1F ROW 2 NORTH/EAST HIGHWAY PROBE ===")
pos = mgba.get_coordinates()
print(f"Start pos: {pos}")

# 1. Up to y=2 along Col 27
while pos['y'] > 2:
    mgba.press_buttons(["Up"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Up at {pos}")
        break
    pos = nxt
    print(f"Up step -> {pos}")

# 2. Right along Row 2 to x=37
while pos['x'] < 37:
    mgba.press_buttons(["Right"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Right at {pos}")
        break
    pos = nxt
    print(f"Right step on Row 2 -> {pos}")

print("=== PROBE COMPLETE ===")
print(f"Final pos: {mgba.get_coordinates()}")
