import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    return p['x'], p['y']

def press(seq):
    mgba.press_buttons(seq)

def clear_dialogue():
    press(["A", "sleep 200", "A", "sleep 200", "B", "sleep 200", "B", "sleep 200"])

def start_surf():
    # Standing at (11, 104) facing North
    # Start menu -> Pokemon -> HYDROS -> SURF
    press([
        "Start", "sleep 250",
        "Up", "sleep 100", "Up", "sleep 100", "Up", "sleep 100", "Up", "sleep 100",
        "Down", "sleep 100",
        "A", "sleep 350",
        "Up", "sleep 100", "Up", "sleep 100", "Up", "sleep 100", "Up", "sleep 100",
        "A", "sleep 350",
        "Up", "sleep 100", "Up", "sleep 100",
        "A", "sleep 600",
        "B", "sleep 200", "B", "sleep 200"
    ])

def surf_north():
    print("Initial pos:", get_pos())
    clear_dialogue()
    # Step Up to (11, 104)
    press(["Up", "sleep 200"])
    print("At water edge:", get_pos())
    start_surf()
    print("After surf attempt pos:", get_pos())
    
    # Surf north to row 71
    # On water, wild encounters may happen
    for _ in range(35):
        cx, cy = get_pos()
        if cy <= 71:
            print("Reached north bank at:", cx, cy)
            break
        press(["Up", "sleep 180"])
        nx, ny = get_pos()
        if (nx, ny) == (cx, cy):
            # Battle or dialogue (Soul guard at 11, 96)
            # Dismiss text / run
            press(["A", "sleep 180", "B", "sleep 180", "A", "sleep 180", "B", "sleep 180"])
            press(["Down", "sleep 100", "Right", "sleep 100", "A", "sleep 350", "B", "sleep 150", "B", "sleep 100"])

    print("End pos after surf north:", get_pos())

if __name__ == "__main__":
    surf_north()
