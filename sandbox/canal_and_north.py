import mgba

def get_pos():
    p = mgba.get_coordinates()
    return p['x'], p['y']

def press(seq):
    mgba.press_buttons(seq)

def run_surf():
    # Cursor is currently at SAVE in Start menu
    # Move Up 3 to POKEMON, press A
    press(["Up", "sleep 150", "Up", "sleep 150", "Up", "sleep 150", "A", "sleep 400"])
    # Party Menu: HYDROS is at slot 1, press A
    press(["A", "sleep 400"])
    # HYDROS submenu: SURF is top option, press A
    press(["A", "sleep 600", "B", "sleep 200", "B", "sleep 200"])
    print("Pos after surf trigger:", get_pos())

    # Surf north
    for i in range(35):
        cx, cy = get_pos()
        if cy <= 71:
            print("Reached north bank at:", cx, cy)
            break
        press(["Up", "sleep 200"])
        nx, ny = get_pos()
        if (nx, ny) == (cx, cy):
            # Guard dialogue or wild battle
            # Dismiss text
            press(["A", "sleep 200", "B", "sleep 200", "A", "sleep 200", "B", "sleep 200"])
            # Escape battle if wild battle
            press(["Down", "sleep 100", "Right", "sleep 100", "A", "sleep 350", "B", "sleep 150", "B", "sleep 100"])

    print("End pos:", get_pos())

if __name__ == "__main__":
    run_surf()
