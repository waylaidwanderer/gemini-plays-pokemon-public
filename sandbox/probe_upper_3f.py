import mgba
import time
import sys

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("In battle! Running...")
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 100"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 800"])
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 100"])

button_count = 0

def walk_step_robust(direction):
    global button_count
    pos_before = mgba.get_coordinates()
    
    if button_count > 45:
        print("Button limit reached. Exiting probe.")
        sys.exit(0)
        
    mgba.press_buttons([direction, "sleep 180"])
    button_count += 1
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        run_from_battle()
        button_count += 8
        mgba.press_buttons([direction, "sleep 180"])
        button_count += 1
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 3:
            print(f"Blocked at {pos_before} attempting {direction}. Retrying...")
            time.sleep(0.3)
            if button_count > 45:
                print("Button limit reached. Exiting probe.")
                sys.exit(0)
            mgba.press_buttons([direction, "sleep 180"])
            button_count += 1
            pos_after = mgba.get_coordinates()
            if pos_before != pos_after:
                break
            run_from_battle()
            button_count += 8
            attempts += 1
    return pos_after

# Probe from (1, 10)
print("Starting probe from:", get_pos())

# 1. Walk UP Column 1 as far as we can (up to Row 4 or 3)
print("Probing UP Column 1...")
for _ in range(8):
    pos = get_pos()
    print("At:", pos)
    new_pos = walk_step_robust("Up")
    if pos == new_pos:
        print("Blocked walking UP Column 1 at:", pos)
        break

# 2. Try walking Right to Column 11 on the highest open Row we found
print("Probing RIGHT on highest open row...")
for _ in range(12):
    pos = get_pos()
    print("At:", pos)
    new_pos = walk_step_robust("Right")
    if pos == new_pos:
        print("Blocked walking RIGHT at:", pos)
        break

# 3. Take a screenshot
sc = mgba.take_screenshot()
print("Screenshot taken:", sc)
print("Final Position:", get_pos())
