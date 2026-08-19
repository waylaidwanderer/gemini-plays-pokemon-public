import mgba
import time

# 1. Warp out of the room to Mansion 1F (16, 5)
print("Warping out of the room...")
mgba.press_buttons(["Right", "sleep 300", "Down", "sleep 1500"])
time.sleep(2.0)

pos = mgba.get_coordinates()
print("Current Position inside Mansion:", pos)

# 2. Walk to (17, 6) on Mansion 1F
print("Walking to (17, 6)...")
mgba.press_buttons(["Right", "sleep 300", "Down", "sleep 300"])
time.sleep(1.0)

pos = mgba.get_coordinates()
print("Position before test:", pos)

# 3. Try to walk Right to (18, 6)
print("Testing Right to (18, 6)...")
mgba.press_buttons(["Right"])
time.sleep(0.5)

final_pos = mgba.get_coordinates()
print("Position after test:", final_pos)
