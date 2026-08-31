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
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        print("No movement, checking for battle...")
        flee_battle()
        new_pos = mgba.get_coordinates()
    return new_pos

def main():
    pos = mgba.get_coordinates()
    print("Initial Position:", pos)
    
    # Path from (16, 4) to 3F West (Column 10)
    path = [
        ("Right", (17, 4)),
        ("Right", (18, 4)),
        ("Down", (18, 5)),
        ("Down", (18, 6)),
        ("Left", (17, 6)),
        ("Left", (16, 6)),
        ("Left", (15, 6)),
        ("Left", (14, 6)),
        ("Left", (13, 6)),
        ("Left", (12, 6)),
        ("Left", (11, 6)),
        ("Left", (10, 6))
    ]
    
    for dir, target in path:
        while True:
            pos = mgba.get_coordinates()
            if pos['x'] == target[0] and pos['y'] == target[1]:
                break
            new_pos = walk_step(dir, target)
            if new_pos == pos:
                time.sleep(0.5)
                
    print("Successfully reached 3F West Column 10! Position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
