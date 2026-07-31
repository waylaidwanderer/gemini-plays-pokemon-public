import mgba
import time

def main():
    print("Walking around the defeated grunt to take B3F stairs at (23, 13)...")
    # Current pos: (19, 13)
    # Path: Up to (19, 12), Right to (20, 12), Right to (21, 12), Down to (21, 13), Right to (22, 13), Right to (23, 13) (stairs)
    buttons = ["Up", "Right", "Right", "Down", "Right", "Right"]
    mgba.press_buttons(buttons)
    time.sleep(2)
    
    pos = mgba.get_coordinates()
    print(f"Current position: {pos}")
    mgba.take_screenshot()

if __name__ == '__main__':
    main()
