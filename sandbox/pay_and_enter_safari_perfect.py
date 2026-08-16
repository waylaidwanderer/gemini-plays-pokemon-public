import mgba
import time

print("--- PAYING AND ENTERING SAFARI ZONE ---")

def get_pos():
    return mgba.get_coordinates()

# Talk to clerk at (3, 2) from (3, 3) facing UP.
mgba.press_buttons(["A"])
time.sleep(1.0)

# The clerk says: "Would you like to join the hunt for ¥500?"
# Press A to select YES.
mgba.press_buttons(["A"])
time.sleep(1.0)

# The clerk says: "That'll be ¥500, please! We only use special Poké Balls here..."
# Let's press A to clear the rest of the dialogue (around 5-6 A presses needed)
print("Clearing dialogue...")
for i in range(8):
    mgba.press_buttons(["A"])
    time.sleep(0.8)

time.sleep(2.0) # wait for map transition to Safari Zone Center

pos_after = get_pos()
print("Position after warp:", pos_after)
mgba.take_screenshot()
