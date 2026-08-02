import mgba

print("=== ROCK TUNNEL B1F (21, 13) PROBE ===")
start = mgba.get_coordinates()
print(f"Start pos: {start}")

# Test Up
mgba.press_buttons(["Up"])
pos_up = mgba.get_coordinates()
print(f"From {start} UP -> {pos_up}")
if pos_up != start:
    mgba.press_buttons(["Down"])

# Test Left
mgba.press_buttons(["Left"])
pos_left = mgba.get_coordinates()
print(f"From {start} LEFT -> {pos_left}")

# From pos_left, try Up, Down, Left
if pos_left != start:
    mgba.press_buttons(["Up"])
    p_lu = mgba.get_coordinates()
    print(f"  From LEFT, UP -> {p_lu}")
    if p_lu != pos_left:
        mgba.press_buttons(["Down"])

    mgba.press_buttons(["Down"])
    p_ld = mgba.get_coordinates()
    print(f"  From LEFT, DOWN -> {p_ld}")
    if p_ld != pos_left:
        mgba.press_buttons(["Up"])

    mgba.press_buttons(["Left"])
    p_ll = mgba.get_coordinates()
    print(f"  From LEFT, LEFT -> {p_ll}")
    if p_ll != pos_left:
        mgba.press_buttons(["Right"])

    # return to start
    mgba.press_buttons(["Right"])

# Test Right
mgba.press_buttons(["Right"])
pos_right = mgba.get_coordinates()
print(f"From {start} RIGHT -> {pos_right}")

# From pos_right, try Up, Down, Right
if pos_right != start:
    mgba.press_buttons(["Right"])
    p_rr = mgba.get_coordinates()
    print(f"  From RIGHT, RIGHT -> {p_rr}")

print("=== PROBE COMPLETE ===")
print(f"Final pos: {mgba.get_coordinates()}")
