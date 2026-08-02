import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting B1F elevator activation from:", pos)

if pos['x'] == 25 and pos['y'] == 15:
    # 1. Turn Down to face the elevator door at (25, 16)
    print("Turning Down...")
    pos = move(["Down"])
    
    # 2. Press A to interact with the elevator door
    print("Facing Down! Pressing A to use Lift Key...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # 3. Step Down into the elevator
    print("Stepping Down into the elevator...")
    pos = move(["Down"])
    time.sleep(2.0)
    print("Final position:", mgba.get_coordinates())

mgba.take_screenshot()
