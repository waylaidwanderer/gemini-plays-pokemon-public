import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting explore_b2f_top from {pos}")

if pos['x'] == 24 and pos['y'] == 15:
    # Walk Up to (24, 14)
    pos = move(['Up'])
    # Walk Right 4 steps to (28, 14)
    for _ in range(4):
        pos = move(['Right'])
    # Walk Up 3 steps to (28, 11)
    for _ in range(3):
        pos = move(['Up'])
    # Walk Left 5 steps to (23, 11)
    for _ in range(5):
        pos = move(['Left'])
    # Walk Up 8 steps to (23, 3)
    for _ in range(8):
        pos = move(['Up'])

# Now we are at (23, 3). Let's explore Left and Right on Row 3 and Row 2.
print("Exploring Row 3 Left...")
# Let's walk Left as far as possible (checking if we hit a wall)
for _ in range(5):
    next_pos = move(['Left'])
    if next_pos['x'] == pos['x']:
        print("Blocked Left on Row 3!")
        break
    pos = next_pos

# Walk back Right to (23, 3)
pos = mgba.get_coordinates()
if pos['x'] < 23:
    for _ in range(23 - pos['x']):
        pos = move(['Right'])

print("Exploring Row 3 Right...")
# Let's walk Right as far as possible
for _ in range(5):
    next_pos = move(['Right'])
    if next_pos['x'] == pos['x']:
        print("Blocked Right on Row 3!")
        break
    pos = next_pos

# Walk back Left to (23, 3)
pos = mgba.get_coordinates()
if pos['x'] > 23:
    for _ in range(pos['x'] - 23):
        pos = move(['Left'])

# Let's see if we can go to Row 2 from (23, 3)? (Wait, the stairs are at (23, 2), walking Up on them warps us!)
# So let's try to walk to Row 2 from other columns!
# Let's walk Left to (21, 3)
for _ in range(2):
    pos = move(['Left'])

# Try to walk Up to Row 2
print("Testing if (21, 2) is walkable...")
pos = move(['Up'])

mgba.take_screenshot()
