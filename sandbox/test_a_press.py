import mgba
import time

def flee_battle():
    print("Wild battle! Fleeing...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def walk_step(direction, target):
    pos = mgba.get_coordinates()
    cx, cy = pos['x'], pos['y']
    print(f"Current: ({cx}, {cy}) | Pressing {direction} to go to {target}")
    mgba.press_buttons([direction])
    time.sleep(0.5)
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        print("No movement, checking for battle...")
        flee_battle()
        new_pos = mgba.get_coordinates()
    return new_pos

def main():
    # Standing at (3, 11)
    # Walk to (2, 12) facing UP
    path = [
        ("Down", (3, 12)),
        ("Left", (2, 12)),
        ("Up", (2, 12))  # Just turn UP
    ]
    
    for dir, target in path:
        while True:
            pos = mgba.get_coordinates()
            if pos['x'] == target[0] and pos['y'] == target[1]:
                # If we just need to turn, we can verify orientation or let it press
                if dir == "Up" and pos['x'] == 2 and pos['y'] == 12:
                    break
            new_pos = walk_step(dir, target)
            if new_pos == pos:
                time.sleep(0.5)
                
    # Now face UP and press A
    print("Facing UP at (2, 12), pressing A...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    scr = mgba.take_screenshot()
    print("Screenshot taken after A press at (2, 12):", scr)
    # Press B to close in case it opened
    mgba.press_buttons(["B"])
    time.sleep(0.5)

if __name__ == "__main__":
    main()
