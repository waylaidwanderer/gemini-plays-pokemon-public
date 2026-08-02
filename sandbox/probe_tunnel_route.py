import mgba

print("=== ROCK TUNNEL 1F CORRIDOR PROBE ===")
pos = mgba.get_coordinates()
print(f"Start pos: {pos}")

while pos['x'] > 13:
    mgba.press_buttons(["Left"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Left at {pos}")
        break
    pos = nxt
    print(f"Left step -> {pos}")

while pos['y'] < 11:
    mgba.press_buttons(["Down"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Down at {pos}")
        break
    pos = nxt
    print(f"Down step -> {pos}")

while pos['x'] < 17:
    mgba.press_buttons(["Right"])
    nxt = mgba.get_coordinates()
    if nxt == pos:
        print(f"Hit wall moving Right at {pos}")
        break
    pos = nxt
    print(f"Right step -> {pos}")

print(f"Final pos: {pos}")
