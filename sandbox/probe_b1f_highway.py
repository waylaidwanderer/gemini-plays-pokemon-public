import mgba

print("=== ROCK TUNNEL B1F COLUMN 17 DESCENT PROBE ===")
pos = mgba.get_coordinates()
print(f"Start pos: {pos}")

while pos['x'] > 17:
    mgba.press_buttons(["Left"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Left at {pos}")
        break
    pos = nxt
    print(f"Left step -> {pos}")

if pos['x'] > 17:
    while pos['y'] > 5:
        mgba.press_buttons(["Up"])
        pos = mgba.get_coordinates()
        print(f"Up step -> {pos}")
    while pos['x'] > 17:
        mgba.press_buttons(["Left"])
        pos = mgba.get_coordinates()
        print(f"Left step -> {pos}")

while pos['y'] < 16:
    mgba.press_buttons(["Down"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Down at {pos}")
        break
    pos = nxt
    print(f"Down step on Col 17 -> {pos}")

print(f"Final pos: {pos}")
