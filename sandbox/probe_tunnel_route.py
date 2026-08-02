import mgba

print("=== ROCK TUNNEL B1F COLUMN 17 HIGHWAY PROBE ===")
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

# 2. Left to x=17 along Row 5
while pos['x'] > 17:
    mgba.press_buttons(["Left"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Left at {pos}")
        break
    pos = nxt
    print(f"Left step -> {pos}")

# 3. Down along Column 17 past y=11 to y=16
while pos['y'] < 16:
    mgba.press_buttons(["Down"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Down at {pos}")
        break
    pos = nxt
    print(f"Down step -> {pos}")

print(f"Final pos: {pos}")
