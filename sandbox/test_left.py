import mgba
import time

print("--- TESTING LEFT WALKABILITY ---")

def get_pos():
    return mgba.get_coordinates()

# Start at (23, 23) facing DOWN.
# Let's try to walk LEFT step-by-step
print("Walking LEFT...")
for step in range(15):
    pos = get_pos()
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    new_pos = get_pos()
    print(f"Step {step+1}: from {pos} to {new_pos}")
    if new_pos == pos:
        # Try once more in case we just turned
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        new_pos = get_pos()
        print(f"Step {step+1} (retry): from {pos} to {new_pos}")
        
    if new_pos == pos:
        print(f"BLOCKED at {pos} going Left!")
        break

mgba.take_screenshot()
print("Final Position:", get_pos())
