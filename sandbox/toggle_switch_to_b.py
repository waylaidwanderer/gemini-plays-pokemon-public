import mgba
import time

def walk_step(tx, ty, d):
    pos = mgba.get_coordinates()
    if pos['x'] == tx and pos['y'] == ty:
        return True
    mgba.press_buttons([d])
    time.sleep(0.55)
    new_pos = mgba.get_coordinates()
    return new_pos['x'] == tx and new_pos['y'] == ty

# Start at (2, 5) on 2F West
pos = mgba.get_coordinates()
print("Starting switch B toggle from:", pos)

if pos['x'] == 2 and pos['y'] == 5:
    # Walk DOWN Column 2 to Row 12
    path = [
        (2, 6, 'Down'),
        (2, 7, 'Down'),
        (2, 8, 'Down'),
        (2, 9, 'Down'),
        (2, 10, 'Down'),
        (2, 11, 'Down'),
        (2, 12, 'Down'),
    ]
    for target in path:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("At (2, 12) on 2F West. Facing UP to toggle switch to State B...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 300", "A", "sleep 500", "B"])
    time.sleep(1.5)

print("Final position after toggle:", mgba.get_coordinates())
mgba.take_screenshot()
