import mgba
import time

def handle_battle():
    # Flee if wild battle occurs
    mgba.press_buttons(["B", "sleep 100", "B", "sleep 100", "Down", "Right", "A", "sleep 1500", "B", "sleep 200", "B"])
    time.sleep(1.0)

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.35)
    pos_after = mgba.get_coordinates()
    if pos_before == pos_after:
        handle_battle()
        pos_after = mgba.get_coordinates()
    return pos_after

# We are at (3, 7) inside Mansion 1F (State A).
# Let's walk to Row 5, and then walk Right along Row 5 to Column 12.
# Then try to walk Down Column 12 to Row 11 to see if it is open or closed in State A!

print("Walking Up to Row 5...")
walk_step("Up") # to (3, 6)
walk_step("Up") # to (3, 5)
print("Position:", mgba.get_coordinates())

print("Walking Right along Row 5 to Column 12...")
for x in range(4, 13):
    pos = walk_step("Right")
    print(f"At: {pos}")

time.sleep(1.0)
pos_12_5 = mgba.get_coordinates()
print("Arrived at Column 12 Row 5:", pos_12_5)

if pos_12_5['x'] == 12 and pos_12_5['y'] == 5:
    print("Walking Down Column 12 to see where we get blocked...")
    # Walk Down to (12, 6)
    pos_12_6 = walk_step("Down")
    print("Position:", pos_12_6)
    
    # Walk Down to (12, 7)
    pos_12_7 = walk_step("Down")
    print("Position:", pos_12_7)
    
    # Try to walk Down to (12, 8)
    pos_12_8 = walk_step("Down")
    print("Position after trying to step on (12, 8):", pos_12_8)
    if pos_12_8['y'] == 8:
        print("Column 12 Row 8 is OPEN in State A!")
    else:
        print("Column 12 Row 8 is BLOCKED/CLOSED in State A!")

time.sleep(1.0)
print("Final Position:", mgba.get_coordinates())
mgba.take_screenshot()
