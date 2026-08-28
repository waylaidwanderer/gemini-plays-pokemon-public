import mgba
import time

def handle_any_menu_or_battle():
    time.sleep(0.15)
    mgba.press_buttons(["B"])
    time.sleep(0.3)
    # Check for battle and run if needed
    # Simple escape for battle: press Down, Right, A
    # Let's just return if we get any coordinates
    return False

# Starting at (2, 10). Let's systematically walk to every coordinate in x=1..3, y=10..16
# and see which steps succeed and which ones are blocked!
# We will use single-step moves.
solids = {}
visited = []

# Move to (2, 10)
curr = mgba.get_coordinates()
print("Starting position for solids scan:", curr)

# We want to test walkability of adjacent tiles.
# Since we are at (2, 10), let's try walking:
# - Left to (1, 10)
# - Right to (3, 10)
# - Down to (2, 11)
# - Up to (2, 9)

def test_move(direction, target):
    mgba.press_buttons([direction])
    time.sleep(0.45)
    pos = mgba.get_coordinates()
    if pos == target:
        # Walked successfully! Walk back.
        opposite = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[direction]
        mgba.press_buttons([opposite])
        time.sleep(0.45)
        return "walkable"
    else:
        return "solid"

print("At (2, 10):")
print("  (1, 10) Left:", test_move("Left", {"x": 1, "y": 10}))
print("  (3, 10) Right:", test_move("Right", {"x": 3, "y": 10}))
print("  (2, 9) Up:", test_move("Up", {"x": 2, "y": 9}))

# Walk down to (2, 11)
mgba.press_buttons(["Down"])
time.sleep(0.45)
pos = mgba.get_coordinates()
print("Moved to:", pos)

if pos == {"x": 2, "y": 11}:
    print("At (2, 11):")
    print("  (1, 11) Left:", test_move("Left", {"x": 1, "y": 11}))
    print("  (3, 11) Right:", test_move("Right", {"x": 3, "y": 11}))
    
# Walk down to (2, 12)
mgba.press_buttons(["Down"])
time.sleep(0.45)
pos = mgba.get_coordinates()
print("Moved to:", pos)

if pos == {"x": 2, "y": 12}:
    print("At (2, 12):")
    print("  (1, 12) Left:", test_move("Left", {"x": 1, "y": 12}))
    print("  (3, 12) Right:", test_move("Right", {"x": 3, "y": 12}))

# Walk down to (2, 13)
mgba.press_buttons(["Down"])
time.sleep(0.45)
pos = mgba.get_coordinates()
print("Moved to:", pos)

if pos == {"x": 2, "y": 13}:
    print("At (2, 13):")
    print("  (1, 13) Left:", test_move("Left", {"x": 1, "y": 13}))
    print("  (3, 13) Right:", test_move("Right", {"x": 3, "y": 13}))

# Walk down to (2, 14)
mgba.press_buttons(["Down"])
time.sleep(0.45)
pos = mgba.get_coordinates()
print("Moved to:", pos)

if pos == {"x": 2, "y": 14}:
    print("At (2, 14):")
    print("  (1, 14) Left:", test_move("Left", {"x": 1, "y": 14}))
    print("  (3, 14) Right:", test_move("Right", {"x": 3, "y": 14}))

# Walk back up to (2, 10) to restore original position
for _ in range(4):
    mgba.press_buttons(["Up"])
    time.sleep(0.45)
print("Finished solids scan. Position restored:", mgba.get_coordinates())

