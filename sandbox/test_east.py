import mgba
import time

def get_state():
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    return pos

# Clear any text/menus
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = get_state()

# 1. Walk UP to (12, 6)
if pos == {"x": 12, "y": 8}:
    print("Walking UP to (12, 6)...")
    mgba.press_buttons(["Up", "sleep 450", "Up"])
    time.sleep(1.0)
    pos = get_state()

# 2. Walk RIGHT to (15, 6)
if pos == {"x": 12, "y": 6}:
    print("Walking RIGHT to (15, 6)...")
    mgba.press_buttons(["Right", "sleep 450", "Right", "sleep 450", "Right"])
    time.sleep(1.5)
    pos = get_state()

# 3. Walk DOWN to (15, 11)
if pos == {"x": 15, "y": 6}:
    print("Walking DOWN to (15, 11)...")
    mgba.press_buttons(["Down", "sleep 450", "Down", "sleep 450", "Down", "sleep 450", "Down", "sleep 450", "Down"])
    time.sleep(2.5)
    pos = get_state()

# 4. Step UP onto stairs at (15, 11) to warp UP to 3F East
if pos == {"x": 15, "y": 11}:
    print("Stepping UP onto stairs to warp...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = get_state()
