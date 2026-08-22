import mgba
import time

def walk_step(direction):
    mgba.press_buttons([direction, "sleep 300"])
    time.sleep(0.1)

def run_to_destination(path):
    for i, direction in enumerate(path):
        pos_before = mgba.get_coordinates()
        walk_step(direction)
        pos_after = mgba.get_coordinates()
        
        if pos_before == pos_after:
            print(f"Bump or Battle detected at step {i} ({direction}) from {pos_before}")
            for escape_attempt in range(5):
                mgba.press_buttons(["B", "sleep 200"])
                mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 500"])
                pos_check = mgba.get_coordinates()
                if pos_check != pos_after:
                    print("Successfully fled battle or cleared block! New pos:", pos_check)
                    break
            else:
                print("Failed to move, still stuck at:", mgba.get_coordinates())

# Starting at (7, 11) on 2F West (State B)
# Walk to (3, 11):
# 1. Left to (6, 11)
# 2. Up to (6, 10)
# 3. Left 3 times to (3, 10)
# 4. Down to (3, 11)
path = ["Left", "Up", "Left", "Left", "Left", "Down"]

print("Walking to switch on 2F West...")
run_to_destination(path)

print("Arrived near switch! Current pos:", mgba.get_coordinates())

# Stand at (3, 11) facing LEFT towards (2, 11)
mgba.press_buttons(["Left", "sleep 300"])

# Interact with the statue at (2, 11)
mgba.press_buttons(["A", "sleep 1000"])

# Select YES to toggle switch to State A
mgba.press_buttons(["A", "sleep 1000"])

# Clear the text box
mgba.press_buttons(["A", "sleep 500"])

print("Switch toggled back to State A!")
print("Final coordinates:", mgba.get_coordinates())
screentype = mgba.take_screenshot()
print("Saved screenshot:", screentype)
