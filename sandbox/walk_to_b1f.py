import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["A", "sleep 500", "A", "sleep 1500", "Right", "Down", "A", "sleep 1500", "A", "sleep 1000"])

# We are at (5, 27) inside Mansion 1F.
# We want to go to B1F stairs at (21, 24).
# Path:
# Right to (21, 27)
# Up to (21, 24) (warp)

path = [
    ('Right', 6, 27), ('Right', 7, 27), ('Right', 8, 27), ('Right', 9, 27),
    ('Right', 10, 27), ('Right', 11, 27), ('Right', 12, 27), ('Right', 13, 27),
    ('Right', 14, 27), ('Right', 15, 27), ('Right', 16, 27), ('Right', 17, 27),
    ('Right', 18, 27), ('Right', 19, 27), ('Right', 20, 27), ('Right', 21, 27),
    ('Up', 21, 26), ('Up', 21, 25), ('Up', 21, 24)
]

print("Walking to B1F stairs at (21, 24)...")
step_index = 0
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
    else:
        print("Failed to reach target. Checking for battle...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            # We are standing still. It might be a battle or menu, or we got blocked.
            # Let's check if the screen indicates a battle by trying to run.
            run_from_battle()
            time.sleep(1)
        else:
            print("Position changed, continuing...")

time.sleep(1.5) # Wait for warp transition
pos_inside_b1f = mgba.get_coordinates()
print("Position inside B1F:", pos_inside_b1f)
