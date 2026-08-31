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
    
    # Let's walk Left along Row 3 to Column 10
    path = [
        ("Left", (23, 3)),
        ("Left", (22, 3)),
        ("Left", (21, 3)),
        ("Left", (20, 3)),
        ("Left", (19, 3)),
        ("Left", (18, 3)),
        ("Left", (17, 3)),
        ("Left", (16, 3)),
        ("Left", (15, 3)),
        ("Left", (14, 3)),
        ("Left", (13, 3)),
        ("Left", (12, 3)),
        ("Left", (11, 3)),
        ("Left", (10, 3))
    ]
    
    for dir, target in path:
        while True:
            pos = mgba.get_coordinates()
            if pos['x'] == target[0] and pos['y'] == target[1]:
                break
            new_pos = walk_step(dir, target)
            if new_pos == pos:
                time.sleep(0.5)
                
    print("Reached Column 10! Position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
