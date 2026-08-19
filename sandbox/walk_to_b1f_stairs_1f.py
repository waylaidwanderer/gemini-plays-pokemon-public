import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    # First press B a couple of times to clear moves/items selection
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    # Move to RUN and press A
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    # Dismiss any "Got away safely!" text
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

# Path to B1F stairs starting from (9, 12):
path = [
    ('Right', 10, 12), ('Right', 11, 12), ('Right', 12, 12),
    ('Up', 12, 11), ('Up', 12, 10), ('Up', 12, 9), ('Up', 12, 8),
    ('Up', 12, 7), ('Up', 12, 6), ('Up', 12, 5), ('Up', 12, 4), ('Up', 12, 3),
    ('Right', 13, 3), ('Right', 14, 3), ('Right', 15, 3), ('Right', 16, 3),
    ('Right', 17, 3), ('Right', 18, 3), ('Right', 19, 3),
    ('Down', 19, 4), ('Down', 19, 5), ('Down', 19, 6), ('Down', 19, 7),
    ('Down', 19, 8), ('Down', 19, 9), ('Down', 19, 10), ('Down', 19, 11),
    ('Down', 19, 12), ('Down', 19, 13), ('Down', 19, 14), ('Down', 19, 15),
    ('Down', 19, 16), ('Down', 19, 17), ('Down', 19, 18), ('Down', 19, 19),
    ('Down', 19, 20), ('Down', 19, 21), ('Down', 19, 22), ('Down', 19, 23),
    ('Down', 19, 24),
    ('Right', 20, 24), ('Right', 21, 24)
]

print("Walking to B1F stairs...")
step_index = 0
stuck_counter = 0

while step_index < len(path):
    btn, target_x, target_y = path[step_index]
    pos = mgba.get_coordinates()
    print(f"Current Pos: {pos}, Next Step: {btn} to ({target_x}, {target_y})")
    
    # Try to take the step
    mgba.press_buttons([btn])
    time.sleep(0.3)
    
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == target_x and new_pos['y'] == target_y:
        print("Step succeeded.")
        step_index += 1
        stuck_counter = 0
    else:
        print("Failed to reach target. Checking for battle or blockage...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            # Coordinates did not change, might be in a battle
            run_from_battle()
            time.sleep(1)
            # Re-check coordinates after battle
            new_pos_after = mgba.get_coordinates()
            if new_pos_after['x'] == target_x and new_pos_after['y'] == target_y:
                step_index += 1
                stuck_counter = 0
        else:
            print("Position changed, continuing...")

print("Position after walk:", mgba.get_coordinates())
