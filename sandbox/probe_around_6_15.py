import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def probe_step(direction, reverse_direction):
    old_pos = get_pos()
    print(f"Current: {old_pos}. Trying {direction}...")
    mgba.press_buttons([direction])
    time.sleep(0.3)
    new_pos = get_pos()
    if old_pos == new_pos:
        print(f"Blocked going {direction}")
        return False
    else:
        print(f"Walked {direction} to {new_pos}")
        # Backtrack
        mgba.press_buttons([reverse_direction])
        time.sleep(0.3)
        back_pos = get_pos()
        print(f"Returned to {back_pos}")
        return True

# Probe all 4 directions from current position
probe_step("Up", "Down")
probe_step("Down", "Up")
probe_step("Left", "Right")
probe_step("Right", "Left")
