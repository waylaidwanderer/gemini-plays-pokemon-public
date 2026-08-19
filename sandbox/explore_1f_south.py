import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Walking DOWN column 10 to row 25 on 1F...")

current_y = 20
target_y = 25

while current_y < target_y:
    pos = mgba.get_coordinates()
    print(f"1F: At {pos}, moving DOWN to row {current_y + 1}...")
    mgba.press_buttons(["Down"])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['y'] > pos['y'] and new_pos['x'] == 10:
        print("Moved successfully.")
        current_y = new_pos['y']
    else:
        print("Blocked or in battle, checking...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            run_from_battle()
            time.sleep(1.0)
            new_pos_after = mgba.get_coordinates()
            current_y = new_pos_after['y']
        else:
            current_y = new_pos['y']

print("Arrived at:", mgba.get_coordinates())
mgba.take_screenshot()
