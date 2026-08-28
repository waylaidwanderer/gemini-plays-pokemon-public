import mgba
import time

def probe_step(direction, reverse_direction):
    old_pos = mgba.get_coordinates()
    print(f"Current: {old_pos}. Trying {direction}...")
    mgba.press_buttons([direction])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if old_pos == new_pos:
        print(f"Blocked going {direction}")
        return False
    else:
        print(f"Walked {direction} to {new_pos}")
        # Backtrack
        mgba.press_buttons([reverse_direction])
        time.sleep(0.3)
        back_pos = mgba.get_coordinates()
        print(f"Returned to {back_pos}")
        return True

# Probe Right, Down, Left from current position (5, 8)
probe_step("Right", "Left")
probe_step("Down", "Up")
probe_step("Left", "Right")
