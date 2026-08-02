import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting search_stairs_down_real from {pos}")

# List of coordinates to test
# Format: list of paths to visit each walkable coordinate
# We can just write a step-by-step path that covers all walkable tiles!
path_to_test = [
    # Currently at (2, 9)
    # Test (1, 9)
    'Left',
    # Test (1, 8)
    'Up',
    # Test (1, 7)
    'Up',
    # Test (2, 7)
    'Right',
    # Test (3, 7)
    'Right',
    # Test (4, 7)
    'Right',
    # Test (5, 7)
    'Right',
    # Walk back to (3, 7)
    'Left', 'Left',
    # Test (3, 9)
    'Down', 'Down',
    # Test (3, 10)
    'Down',
    # Test (4, 10)
    'Right',
    # Walk to (3, 11)
    'Left', 'Down',
    # Test (1, 11)
    'Left', 'Left',
    # Test (1, 12)
    'Down',
    # Test (1, 13)
    'Down',
    # Test (2, 13)
    'Right',
    # Test (3, 13)
    'Right',
    # Test (4, 13)
    'Right',
    # Test (3, 12)
    'Up', 'Left',
]

for step in path_to_test:
    old_pos = mgba.get_coordinates()
    pos = move([step])
    time.sleep(0.2)
    # Check if we transitioned maps (usually y changes significantly, or we spawn somewhere else)
    new_pos = mgba.get_coordinates()
    if abs(new_pos['x'] - old_pos['x']) > 5 or abs(new_pos['y'] - old_pos['y']) > 5:
        print(f"MAP TRANSITION DETECTED! Spawned at: {new_pos}")
        break

mgba.take_screenshot()
