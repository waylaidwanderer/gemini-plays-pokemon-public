import mgba
import time

def handle_any_menu_or_battle():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    print("Screenshot captured:", scr_file)

def walk_step(direction, expected_coords):
    mgba.press_buttons([direction])
    time.sleep(0.5)
    pos = mgba.get_coordinates()
    print(f"Pressed {direction}, expected {expected_coords}, actual {pos}")
    return pos == expected_coords

print("Initial position:", mgba.get_coordinates())

# Move Down to (3, 12)
walk_step("Down", {"x": 3, "y": 12})

# Move Left to (2, 12)
walk_step("Left", {"x": 2, "y": 12})

# Move Left to (1, 12)
walk_step("Left", {"x": 1, "y": 12})

# Move Up to (1, 11)
walk_step("Up", {"x": 1, "y": 11})

# Move Up to (1, 10)
walk_step("Up", {"x": 1, "y": 10})

# Move Up to (1, 9)
walk_step("Up", {"x": 1, "y": 9})

# Move Up to (1, 8)
walk_step("Up", {"x": 1, "y": 8})

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
