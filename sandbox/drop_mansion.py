import mgba
import time

def main():
    print("Currently at:", mgba.get_coordinates())
    
    # Walk Left from (20, 15) as far as we can to find the balcony drop edge!
    for i in range(10):
        print(f"Step {i+1}: Pressing Left...")
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        pos = mgba.get_coordinates()
        print("Position:", pos)
        
        # If we warped/dropped, our coordinates or map will change.
        # Inside B1F or 1F, we will land at some coordinate.
        # Let's check if the Y coordinate changed significantly or if we are no longer at Row 15.
        if pos['y'] != 15:
            print("Landed! Coordinates:", pos)
            mgba.take_screenshot()
            break
            
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
