import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def run_away():
    print("Battle detected! Running away...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 600"])
    mgba.press_buttons(["B", "sleep 300"])

def safe_step(direction):
    old_pos = get_pos()
    print(f"Current: {old_pos}. Stepping {direction}...")
    mgba.press_buttons([direction])
    time.sleep(0.45)
    new_pos = get_pos()
    
    if new_pos == old_pos:
        time.sleep(0.5)
        if get_pos() != old_pos:
            # We got into a battle! Let's run away.
            run_away()
            time.sleep(1.0)
            print("Ran away. Position is:", get_pos())
            mgba.take_screenshot()
            return False
          # If we got blocked by something other than a battle
        else:
            print("BLOCKED physically!")
            return False
    else:
        print(f"Moved successfully to: {new_pos}")
        mgba.take_screenshot()
        return True

# Change this direction as needed!
safe_step("Left")
