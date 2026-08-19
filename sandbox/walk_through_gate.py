import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    # Wait for battle transition to fully end and overworld to accept input
    time.sleep(1.5)

print("Starting definitive 3F gate passage and State B toggle script...")
print("Current position:", mgba.get_coordinates())

# Step 1: Wait/Walk to (8, 11)
attempts = 0
while True:
    pos = mgba.get_coordinates()
    print(f"At {pos}, attempting to step Up to (8, 11)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == 8 and new_pos['y'] == 11:
        print("Successfully reached (8, 11)!")
        break
    else:
        # Check if we got into a battle
        if new_pos != pos:
             # This shouldn't happen unless we warped or something weird, but let's handle battle just in case
             run_from_battle()
        else:
             print("Blocked by NPC. Waiting...")
             time.sleep(0.5)
             attempts += 1
             if attempts > 15:
                  print("NPC blocking too long. Trying to step Down to clear path...")
                  mgba.press_buttons(["Down"])
                  time.sleep(0.4)
                  attempts = 0

# Step 2: Walk Right to (11, 11)
path = [
    ('Right', 9, 11),
    ('Right', 10, 11), # Shutter gate (OPEN in State A!)
    ('Right', 11, 11)
]

for btn, tx, ty in path:
    while True:
        pos = mgba.get_coordinates()
        print(f"3F: At {pos}, moving {btn} to ({tx}, {ty})...")
        mgba.press_buttons([btn])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        if new_pos['x'] == tx and new_pos['y'] == ty:
             print("Moved successfully.")
             break
        else:
             print("Blocked or battle! Checking battle...")
             # If we stayed at same position, it might be NPC block.
             # If it was a battle, new_pos could be same if it reset, but battle screen was open.
             # Let's run from battle and then the loop will retry this step!
             run_from_battle()
             time.sleep(0.5)

# Step 3: Face Right and interact with Mewtwo statue at (12, 11) to toggle to State B
pos = mgba.get_coordinates()
if pos['x'] == 11 and pos['y'] == 11:
    print("Reached (11, 11)! Toggling switch to State B...")
    mgba.press_buttons(["Right", "sleep 200", "A", "sleep 1000"])
    # Dialogue: "A secret switch! Press it?" -> YES (press A)
    print("Selecting YES...")
    mgba.press_buttons(["A", "sleep 1000"])
    # Clear dialogue
    print("Clearing dialogue...")
    mgba.press_buttons(["B", "sleep 500"])
    print("Switch set to State B!")

print("Final Position:", mgba.get_coordinates())
mgba.take_screenshot()
