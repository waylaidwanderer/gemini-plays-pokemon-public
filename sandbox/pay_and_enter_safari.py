import mgba
import time

def press_and_wait(btn, delay=0.5):
    print(f"Pressing {btn}...")
    mgba.press_buttons([btn])
    time.sleep(delay)

# We are currently at (3, 4) with the Yes/No menu open for "first time here?".
# 1. Press Down to select NO
press_and_wait("Down")

# 2. Press A to confirm NO
press_and_wait("A", delay=1.0)

# 3. Press A to clear "That'll be ¥500, please!"
press_and_wait("A", delay=1.0)

# 4. Press A to confirm YES to "join the hunt?"
press_and_wait("A", delay=1.0)

# 5. Press A to clear "First-rate! Here are..."
press_and_wait("A", delay=1.0)

# 6. Press A to clear "ACE received 30 SAFARI BALLs!"
press_and_wait("A", delay=1.0)

# 7. Press A to clear "We'll call you..."
press_and_wait("A", delay=1.0)

# 8. Press A to walk forward and warp
press_and_wait("A", delay=2.0)

curr = mgba.get_coordinates()
print("Position after trying to enter Safari Zone:", curr)
mgba.take_screenshot()
