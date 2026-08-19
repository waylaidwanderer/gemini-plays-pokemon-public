import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Verifying walkable directions from (21, 15)...")
initial_pos = mgba.get_coordinates()
print("Initial position:", initial_pos)

# Test DOWN
print("Testing DOWN move...")
mgba.press_buttons(["Down"])
time.sleep(0.4)
pos_after_down = mgba.get_coordinates()
print("Position after DOWN:", pos_after_down)

if pos_after_down != initial_pos:
    print("DOWN is WALKABLE! We entered row 16!")
    # Move back UP
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
else:
    print("DOWN is BLOCKED! Row 16 gates are closed.")

# Test RIGHT
initial_pos = mgba.get_coordinates()
print("Testing RIGHT move...")
mgba.press_buttons(["Right"])
time.sleep(0.4)
pos_after_right = mgba.get_coordinates()
print("Position after RIGHT:", pos_after_right)

if pos_after_right != initial_pos:
    print("RIGHT is WALKABLE!")
    # Move back LEFT
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
else:
    print("RIGHT is BLOCKED.")

# Test LEFT
initial_pos = mgba.get_coordinates()
print("Testing LEFT move...")
mgba.press_buttons(["Left"])
time.sleep(0.4)
pos_after_left = mgba.get_coordinates()
print("Position after LEFT:", pos_after_left)

if pos_after_left != initial_pos:
    print("LEFT is WALKABLE!")
    # Move back RIGHT
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
else:
    print("LEFT is BLOCKED.")

# Test UP
initial_pos = mgba.get_coordinates()
print("Testing UP move...")
mgba.press_buttons(["Up"])
time.sleep(0.4)
pos_after_up = mgba.get_coordinates()
print("Position after UP:", pos_after_up)

if pos_after_up != initial_pos:
    print("UP is WALKABLE!")
    # Move back DOWN
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
else:
    print("UP is BLOCKED.")

mgba.take_screenshot()
