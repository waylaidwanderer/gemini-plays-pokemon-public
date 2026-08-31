import mgba
import time

def main():
    pos = mgba.get_coordinates()
    print("Starting position:", pos)
    
    # Path to (7, 10)
    steps = [
        ("Up", (9, 12)),
        ("Up", (9, 11)),
        ("Up", (9, 10)),
        ("Left", (8, 10)),
        ("Left", (7, 10))
    ]
    
    for dir, target in steps:
        print(f"Pressing {dir} to go to {target}...")
        mgba.press_buttons([dir])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print("Current position:", pos)
        
    print("Final check after reaching (7, 10):")
    time.sleep(1.0)
    pos_final = mgba.get_coordinates()
    print("Final position:", pos_final)
    
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
