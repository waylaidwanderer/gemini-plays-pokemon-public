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

# Starting at (12, 5) inside the Lab hallway
pos = mgba.get_coordinates()
print("Starting definitive Mansion ingress from:", pos)

if pos['x'] == 12 and pos['y'] == 5:
    # 1. Walk to Lab lobby and exit
    print("Walking to Lab lobby...")
    walk_step(12, 6, 'Down')
    walk_step(12, 7, 'Down')
    for col in range(11, 1, -1):
        walk_step(col, 7, 'Left')
    print("Exiting Lab...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)

pos = mgba.get_coordinates()
print("Outside on Cinnabar Island:", pos)

if pos['x'] == 6 and pos['y'] == 10:
    # 2. Walk to Mansion entrance (6, 3)
    print("Walking to Mansion entrance...")
    cinnabar_path = [
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
    for target in cinnabar_path:
        tx, ty, d = target
        walk_step(tx, ty, d)
        
    print("At (6, 4). Stepping UP to enter Mansion...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)

pos = mgba.get_coordinates()
print("Position inside Mansion (expected at (5, 27)):", pos)
mgba.take_screenshot()
