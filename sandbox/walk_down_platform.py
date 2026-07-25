import mgba
import time

def main():
    print("Walking down the platform on column 25...")
    # Starting at (25, 9)
    # Target: row 23 (14 steps Down)
    
    for i in range(14):
        pos_before = mgba.get_coordinates()
        mgba.press_buttons(["Down", "sleep 300"])
        pos_after = mgba.get_coordinates()
        print(f"Step {i+1}: Before={pos_before}, After={pos_after}")
        if pos_before == pos_after and pos_after['x'] != 0:
            print("Blocked! Stopping.")
            break
            
    img = mgba.take_screenshot()
    print(f"Final screenshot: {img}")

if __name__ == "__main__":
    main()
