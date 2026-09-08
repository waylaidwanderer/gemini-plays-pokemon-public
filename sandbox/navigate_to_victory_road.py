import mgba

def run_step():
    # 1. Dismiss Surf textbox
    mgba.press_buttons(["B", "sleep 400"])
    pos = mgba.get_coordinates()
    print("Surfing pos:", pos)

    # 2. Surf north along canal to row 86
    curr = mgba.get_coordinates()
    if curr['y'] <= 103 and curr['y'] > 86:
        mgba.press_buttons(["Up"] * (curr['y'] - 86) + ["sleep 200"])
        print("At row 86:", mgba.get_coordinates())

    # 3. Left to col 6 (bypass island)
    curr = mgba.get_coordinates()
    if curr['y'] <= 86 and curr['x'] > 6:
        mgba.press_buttons(["Left"] * (curr['x'] - 6) + ["sleep 200"])
        print("At col 6:", mgba.get_coordinates())

    # 4. North along col 6 to row 75
    curr = mgba.get_coordinates()
    if curr['x'] == 6 and curr['y'] > 75:
        mgba.press_buttons(["Up"] * (curr['y'] - 75) + ["sleep 200"])
        print("At (6, 75):", mgba.get_coordinates())

    # 5. Right to col 10
    curr = mgba.get_coordinates()
    if curr['y'] <= 75 and curr['x'] < 10:
        mgba.press_buttons(["Right"] * (10 - curr['x']) + ["sleep 200"])
        print("At (10, 75):", mgba.get_coordinates())

    # 6. North to row 71 (landing onto green lawn!)
    curr = mgba.get_coordinates()
    if curr['x'] == 10 and curr['y'] > 71:
        mgba.press_buttons(["Up"] * (curr['y'] - 71) + ["sleep 300"])
        print("Canal landing pos:", mgba.get_coordinates())

    # 7. Walk North along Col 10 past Volcano check (66) to row 61
    curr = mgba.get_coordinates()
    if curr['y'] <= 71 and curr['y'] > 61:
        mgba.press_buttons(["Up"] * (curr['y'] - 61) + ["sleep 200"])
        print("At row 61:", mgba.get_coordinates())

    # 8. Left to Col 7 (ledge gap), Up 1 to row 60
    curr = mgba.get_coordinates()
    if curr['y'] == 61 and curr['x'] > 7:
        mgba.press_buttons(["Left"] * (curr['x'] - 7) + ["Up"] + ["sleep 200"])
        print("At (7, 60):", mgba.get_coordinates())

    # 9. Walk North along Col 7 past Earth Badge check to row 31
    curr = mgba.get_coordinates()
    if curr['x'] == 7 and curr['y'] > 31:
        mgba.press_buttons(["Up"] * (curr['y'] - 31) + ["sleep 200"])
        print("At row 31:", mgba.get_coordinates())

    # 10. Left 3 to (4, 31), Up 1 through Archway to (4, 30)
    curr = mgba.get_coordinates()
    if curr['y'] == 31 and curr['x'] > 4:
        mgba.press_buttons(["Left"] * (curr['x'] - 4) + ["Up"] + ["sleep 200"])
        print("Through Archway at:", mgba.get_coordinates())

    # 11. Right 2 to (6, 30), North 8 to (6, 22)
    curr = mgba.get_coordinates()
    if curr['y'] == 30 and curr['x'] < 6:
        mgba.press_buttons(["Right"] * (6 - curr['x']) + ["Up"] * 8 + ["sleep 200"])
        print("At Row 22 Highway:", mgba.get_coordinates())

    # 12. Left 4 to (2, 22), North 21 to (2, 1)
    curr = mgba.get_coordinates()
    if curr['y'] == 22 and curr['x'] > 2:
        mgba.press_buttons(["Left"] * (curr['x'] - 2) + ["Up"] * 21 + ["sleep 200"])
        print("At Cave Entrance (2, 1):", mgba.get_coordinates())

    # 13. Step Up into Cave Entrance at (2, 1)
    curr = mgba.get_coordinates()
    if curr['x'] == 2 and curr['y'] <= 1:
        mgba.press_buttons(["Up", "sleep 500"])
        print("Inside Victory Road 1F! Pos:", mgba.get_coordinates())

run_step()
