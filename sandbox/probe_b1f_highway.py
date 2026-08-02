import mgba

print("=== ROCK TUNNEL B1F COL 13 SOUTHBOUND HIGHWAY PROBE ===")
pos = mgba.get_coordinates()
print(f"Start pos: {pos}")

# 1. Left to x=13 along Row 7
while pos['x'] > 13:
    mgba.press_buttons(["Left"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Left at {pos}")
        break
    pos = nxt
    print(f"Left step -> {pos}")

# 2. Down along Column 13 to y=16
while pos['y'] < 16:
    mgba.press_buttons(["Down"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Down at {pos}")
        break
    pos = nxt
    print(f"Down step on Col 13 -> {pos}")

# 3. Right along Row 16 to x=21
while pos['x'] < 21:
    mgba.press_buttons(["Right"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Right at {pos}")
        break
    pos = nxt
    print(f"Right step on Row 16 -> {pos}")

print(f"Final pos: {pos}")
