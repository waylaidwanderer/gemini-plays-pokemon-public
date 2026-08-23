import mgba
import time

print("Dismissing text box...")
mgba.press_buttons(["B", "sleep 300"])

pos = mgba.get_coordinates()
print("Current position:", pos)

def walk_to_overworld(target_x, target_y):
    max_steps = 50
    steps = 0
    while steps < max_steps:
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        if x == target_x and y == target_y:
            return True
            
        if x < target_x:
            mgba.press_buttons(["Right", "sleep 200"])
        elif x > target_x:
            mgba.press_buttons(["Left", "sleep 200"])
        elif y < target_y:
            mgba.press_buttons(["Down", "sleep 200"])
        elif y > target_y:
            mgba.press_buttons(["Up", "sleep 200"])
        steps += 1
    return False

print("Walking to (6, 5)...")
walk_to_overworld(6, 5)

print("Walking to (6, 3)...")
walk_to_overworld(6, 3)

print("Entering the Mansion...")
mgba.press_buttons(["Up", "sleep 500"])
time.sleep(1.5)

print("Position inside Mansion:", mgba.get_coordinates())
sc = mgba.take_screenshot()
print("Screenshot saved to:", sc)
