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

# Start at (4, 11) on Cinnabar Island
pos = mgba.get_coordinates()
print("Starting Cinnabar East probe from:", pos)

if pos['x'] == 4 and pos['y'] == 11:
    # 1. Walk right along Row 11 to Column 18
    print("Walking Right to Column 18...")
    for col in range(5, 19):
        if not walk_step(col, 11, 'Right'):
            print(f"Bumped at {mgba.get_coordinates()} going Right to ({col}, 11)")
            break
            
    # 2. Try walking UP Column 18 to Row 4
    pos = mgba.get_coordinates()
    print("Currently at:", pos)
    if pos['x'] == 18:
        print("Walking UP Column 18...")
        reached = pos['y']
        for r in range(pos['y'] - 1, 3, -1):
            if walk_step(18, r, 'Up'):
                reached = r
            else:
                break
        print(f"Reached Row {reached} on Column 18")

print("Final position after East probe:", mgba.get_coordinates())
mgba.take_screenshot()
