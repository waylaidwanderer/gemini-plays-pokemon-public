import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Walking to 2F from (5, 27) on 1F...")

# Step 1: Walk up column 5 from 27 to 10
current_y = 27
target_y = 10

while current_y > target_y:
    pos = mgba.get_coordinates()
    print(f"1F: At {pos}, walking UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    
    if new_pos['y'] < pos['y'] and new_pos['x'] == 5:
        current_y = new_pos['y']
    else:
        # Check if we warped to 2F
        # On 2F, we land at (5, 11) because of the automatic step down
        if new_pos['y'] == 11 and new_pos['x'] == 5:
            print("Warped to 2F successfully!")
            break
            
        print("Blocked or in battle, checking...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            run_from_battle()
            time.sleep(1.0)
            new_pos_after = mgba.get_coordinates()
            current_y = new_pos_after['y']
        else:
            current_y = new_pos['y']

print("Arrived on 2F at:", mgba.get_coordinates())

# Step 2: Walk to (2, 11) on 2F to check for Mewtwo statue
# From (5, 11), we go Left 3 times to (2, 11)
left_path = [
    ('Left', 4, 11),
    ('Left', 3, 11),
    ('Left', 2, 11)
]

for btn, tx, ty in left_path:
    pos = mgba.get_coordinates()
    print(f"2F: At {pos}, moving {btn} to ({tx}, {ty})...")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == tx and new_pos['y'] == ty:
        print("Moved successfully.")
    else:
        print("Blocked, checking for battle...")
        run_from_battle()
        break

print("Facing UP at (2, 11) and interacting...")
mgba.press_buttons(["Up", "sleep 100", "A", "sleep 1000"])

# Check screenshot
img = mgba.take_screenshot()
print("Interacted at (2, 11). Screenshot:", img)
