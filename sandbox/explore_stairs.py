import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

# Starting at (8, 11)
print("Navigating to find path to eastern B2F room...")

# Step 1: Walk to (10, 14) and slide to (15, 18) stopper
move(["Right", "Right", "Down", "Down", "Down"])
move(["Right", "sleep 2000"])

# Now we are at (15, 18). Let's see if we can walk Right or Up/Right
pos = mgba.get_coordinates()
print("At stopper:", pos)

# Let's try to walk to the right to reach the eastern room (Columns 23-28)
# We know Columns 23-28 on Row 13-15 is walkable. Let's see if we can walk Up/Right or Right
# Let's try going Right
move(["Right"])
# Let's try going Up
move(["Up"])
# Let's try going Right
move(["Right"])
# Let's see where we end up!
pos = mgba.get_coordinates()
print("Coordinates after attempting Right/Up:", pos)
