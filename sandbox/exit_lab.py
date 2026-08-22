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

# Currently at (12, 5) inside the Lab hallway.
# Let's walk to the lobby doormat (2, 7) and exit the Lab.
print("Walking to Lab lobby...")
walk_step(12, 6, 'Down')
walk_step(12, 7, 'Down')
for col in range(11, 1, -1):
    walk_step(col, 7, 'Left')

print("Exiting Lab...")
mgba.press_buttons(["Down"])
time.sleep(2.0)

pos = mgba.get_coordinates()
print("Position outside on Cinnabar:", pos)

if pos['x'] == 6 and pos['y'] == 10:
    # Walk around the Lab to the Mansion door (6, 3)
    print("Walking around Lab to Mansion front door...")
    path = [
        (6, 11, 'Down'),
        (5, 11, 'Left'),
        (4, 11, 'Left'),
        (4, 10, 'Up'),
        (4, 9, 'Up'),
        (4, 8, 'Up'),
        (4, 7, 'Up'),
        (4, 6, 'Up'),
        (4, 5, 'Up'),
        (4, 4, 'Up'),
        (5, 4, 'Right'),
        (6, 4, 'Right'),
    ]
    for target in path:
        tx, ty, d = target
        walk_step(tx, ty, d)

print("At (6, 4) ready to enter Mansion. Final position:", mgba.get_coordinates())
mgba.take_screenshot()
