import mgba

print("=== ROCK TUNNEL B1F COL 13 LOWER HIGHWAY NAVIGATOR ===")
pos = mgba.get_coordinates()
print(f"Start pos: {pos}")

# 1. Up to y=5
while pos['y'] > 5:
    mgba.press_buttons(["Up"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Up at {pos}")
        break
    pos = nxt
    print(f"Up step -> {pos}")

# 2. Left to x=13 along Row 5
while pos['x'] > 13:
    mgba.press_buttons(["Left"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Left at {pos}")
        break
    pos = nxt
    print(f"Left step -> {pos}")

# 3. Down along Column 13 to y=16
while pos['y'] < 16:
    mgba.press_buttons(["Down"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Down at {pos}")
        break
    pos = nxt
    print(f"Down step on Col 13 -> {pos}")

# 4. Right along Row 16 to x=21
while pos['x'] < 21:
    mgba.press_buttons(["Right"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Right at {pos}")
        break
    pos = nxt
    print(f"Right step on Row 16 -> {pos}")

print("=== NAVIGATION COMPLETE ===")
print(f"Final pos: {mgba.get_coordinates()}")
