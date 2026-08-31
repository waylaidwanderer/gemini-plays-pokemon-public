import mgba
import time

def toggle_switch():
    print("Currently at (3, 11). Ensuring we face Left...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)

    # 4 A-press sequence with generous delays
    for press in range(1, 5):
        print(f"A-press {press}...")
        mgba.press_buttons(["A"])
        time.sleep(2.0)

    # Grab final position
    pos = mgba.get_coordinates()
    print("Final position after toggle:", pos)

if __name__ == "__main__":
    toggle_switch()
