import mgba
import time

def main():
    print("Walking to (25, 8) to test if it's the pitfall...")
    path = [
        (26, 10),
        (26, 9),
        (26, 8),
        (25, 8)
    ]
    
    for i, target in enumerate(path):
        pos = mgba.get_coordinates()
        print(f"Current Position: {pos}")
        tx, ty = target
        dx = tx - pos['x']
        dy = ty - pos['y']
        
        if dx > 0: direction = "Right"
        elif dx < 0: direction = "Left"
        elif dy > 0: direction = "Down"
        elif dy < 0: direction = "Up"
        else: continue
        
        print(f"Moving {direction} to {target}...")
        mgba.press_buttons([direction])
        time.sleep(0.5)
        
    pos = mgba.get_coordinates()
    print(f"Final Position: {pos}")
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
