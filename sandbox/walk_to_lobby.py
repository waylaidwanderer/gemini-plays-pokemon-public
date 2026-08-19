import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["A", "sleep 500", "A", "sleep 1500", "Right", "Down", "A", "sleep 1500", "A", "sleep 1000"])

path = [
    ('Left', 19, 12),
    ('Left', 18, 12),
    ('Up', 18, 11),
    ('Left', 17, 11),
    ('Left', 16, 11),
    ('Left', 15, 11),
    ('Left', 14, 11),
    ('Left', 13, 11),
    ('Left', 12, 11),
    ('Left', 11, 11),
    ('Left', 10, 11),
    ('Left', 9, 11),
    ('Left', 8, 11),
    ('Left', 7, 11),
    ('Left', 6, 11),
    ('Left', 5, 11)
]

print("Starting walk to lobby...")
step_index = 0
while step_index < len(path):
    btn, target_x, target_y = path[step_index]
    pos = mgba.get_coordinates()
    print(f"Current Pos: {pos}, Next Step: {btn} to ({target_x}, {target_y})")
    
    # Try to take the step
    mgba.press_buttons([btn])
    time.sleep(0.3)  # wait for movement to complete
    
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == target_x and new_pos['y'] == target_y:
        # Step succeeded!
        print("Step succeeded.")
        step_index += 1
    else:
        # Step failed or didn't reach target. Might be a battle!
        print("Failed to reach target. Checking for battle...")
        # Wait a bit more and check coordinates
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            # Coordinates are unchanged, definitely a battle or blocked
            run_from_battle()
            # After running, we should be back at the previous step's coordinate
            # Let's verify we are back in the overworld and try the step again
            time.sleep(1)
        else:
            print("Position changed, continuing...")

print("Reached lobby!")
final_pos = mgba.get_coordinates()
print("Final Position:", final_pos)
