import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

print("Starting deep B3F southern descent test...")

# Step 1: Walk UP to (27, 11)
move(["Up"])

# Step 2: Walk Left 4 steps to (23, 11)
move(["Left", "Left", "Left", "Left"])

# Step 3: Walk Down to (23, 13)
move(["Down", "Down"])

# Step 4: Systematically explore DOWN from (23, 13)
pos = mgba.get_coordinates()
for i in range(15):  # try walking down up to 15 times
    mgba.press_buttons(["Down"])
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        print(f"Hit obstacle going Down at: {pos}")
        break
    pos = new_pos
    print(f"Walked Down, current coordinates: {pos}")

# Step 5: If we are at the bottom (Row 22 or similar), try walking Left to Column 21
print("Descent phase finished. Attempting Left exploration from final position...")
pos = mgba.get_coordinates()
for i in range(5):  # try walking left up to 5 times
    mgba.press_buttons(["Left"])
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        print(f"Hit obstacle going Left at: {pos}")
        break
    pos = new_pos
    print(f"Walked Left, current coordinates: {pos}")

print("Final B3F Southern exploration coordinates:", mgba.get_coordinates())
