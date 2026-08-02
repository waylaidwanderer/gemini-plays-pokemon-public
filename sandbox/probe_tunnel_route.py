import mgba

print("=== ROCK TUNNEL B1F LADDER ROUTE PROBE ===")
start = mgba.get_coordinates()
print(f"Start pos: {start}")

while start['y'] > 4:
    mgba.press_buttons(["Up"])
    start = mgba.get_coordinates()
    print(f"Moved Up -> {start}")

while start['x'] < 20:
    mgba.press_buttons(["Right"])
    start = mgba.get_coordinates()
    print(f"Moved Right -> {start}")

while start['y'] < 11:
    mgba.press_buttons(["Down"])
    start = mgba.get_coordinates()
    print(f"Moved Down -> {start}")

while start['x'] > 17:
    mgba.press_buttons(["Left"])
    start = mgba.get_coordinates()
    print(f"Moved Left -> {start}")

print(f"Final position: {mgba.get_coordinates()}")
