import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["A", "sleep 500", "A", "sleep 1500", "Right", "Down", "A", "sleep 1500", "A", "sleep 1000"])

# 1. Walk from (13, 7) to (16, 4) on Mansion 1F to warp into Cinnabar Lab room
path1 = [
    ('Right', 14, 7), ('Right', 15, 7), ('Right', 16, 7),
    ('Up', 16, 6), ('Up', 16, 5), ('Up', 16, 4)
]

print("Walking to door (16, 4)...")
step_index = 0
while step_index < len(path1):
    btn, target_x, target_y = path1[step_index]
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
            run_from_battle()
            time.sleep(1)
        else:
            print("Position changed, continuing...")

# Wait for warp transition inside the Lab room
print("Warped into Lab room!")
time.sleep(1.5)

# Inside the Lab room (should be 2, 7), walk Down to exit back outside
print("Exiting Lab room to Cinnabar Island...")
mgba.press_buttons(["Down", "sleep 1500"])
time.sleep(2.0)

# Outside on Cinnabar Island, the landing spot is (6, 10).
# Let's walk to Mansion entrance (6, 3) bypassing column 6 row 9 (Lab door).
print("Walking to Mansion entrance...")
path_outside = [
    ("Left", "sleep 300"),  # to (5, 10)
    ("Up", "sleep 300"),    # to (5, 9)
    ("Up", "sleep 300"),    # to (5, 8)
    ("Up", "sleep 300"),    # to (5, 7)
    ("Up", "sleep 300"),    # to (5, 6)
    ("Up", "sleep 300"),    # to (5, 5)
    ("Up", "sleep 300"),    # to (5, 4)
    ("Up", "sleep 300"),    # to (5, 3)
    ("Right", "sleep 300"), # to (6, 3)
    ("Up", "sleep 1500")    # enter Mansion door warp!
]
mgba.press_buttons([btn for btn, _ in path_outside])
time.sleep(4.0)

pos = mgba.get_coordinates()
print("Warped inside Mansion 1F, current pos:", pos)

# Now we should be on row 27 in State A!
# Let's walk Right to column 21
path_inside = []
current_x = pos['x']
for x in range(current_x + 1, 22):
    path_inside.append(('Right', x, 27))
path_inside.extend([
    ('Up', 21, 26), ('Up', 21, 25), ('Up', 21, 24)
])

print("Walking to B1F stairs inside Mansion 1F...")
step_index = 0
while step_index < len(path_inside):
    btn, target_x, target_y = path_inside[step_index]
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
            run_from_battle()
            time.sleep(1)
        else:
            print("Position changed, continuing...")

print("Reached B1F stairs!")
final_pos = mgba.get_coordinates()
print("Final Position:", final_pos)
