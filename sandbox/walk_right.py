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

# Start at (2, 7) inside the Mansion
print("Exiting entrance doormat...")
walk_step(2, 6, 'Up')

pos = mgba.get_coordinates()
print("Position after walking up:", pos)

if pos['x'] == 2 and pos['y'] == 6:
    # Walk right as far as possible on Row 6
    print("Walking RIGHT along Row 6...")
    for col in range(3, 15):
        if not walk_step(col, 6, 'Right'):
            print(f"Bumped at {mgba.get_coordinates()} going Right to ({col}, 6)")
            break
        else:
            print("Reached:", mgba.get_coordinates())

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
