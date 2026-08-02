import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    return pos

pos = mgba.get_coordinates()
print("Starting systematic walk test from:", pos)

# We are at (25, 13).
# We want to test walking Left at each row from Row 13 to Row 22.
# Let's walk Down one step at a time, and at each step, try to walk Left, then walk back Right if successful.

results = {}

for y in range(13, 23):
    # Ensure we are at (25, y)
    pos = mgba.get_coordinates()
    if pos['x'] != 25 or pos['y'] != y:
        print(f"Repositioning to (25, {y})...")
        # Walk to Column 25
        if pos['x'] < 25:
            for _ in range(25 - pos['x']):
                pos = move(["Right"])
        elif pos['x'] > 25:
            for _ in range(pos['x'] - 25):
                pos = move(["Left"])
        # Walk to Row y
        if pos['y'] < y:
            for _ in range(y - pos['y']):
                pos = move(["Down"])
        elif pos['y'] > y:
            for _ in range(pos['y'] - y):
                pos = move(["Up"])
                
    pos = mgba.get_coordinates()
    print(f"Now at (25, {pos['y']}). Testing Left...")
    
    # Try to walk Left
    new_pos = move(["Left"])
    if new_pos['x'] == 24:
        print(f"-> Row {y} Column 24 is WALKABLE!")
        results[y] = "Walkable"
        # Walk back Right to Column 25
        move(["Right"])
    else:
        print(f"-> Row {y} Column 24 is SOLID/BLOCKED.")
        results[y] = "Blocked"

print("Walk Test Results:")
for row, res in results.items():
    print(f"Row {row}: {res}")

mgba.take_screenshot()
