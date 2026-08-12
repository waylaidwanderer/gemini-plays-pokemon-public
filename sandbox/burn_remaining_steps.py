import mgba
import time

def burn_until_warp():
    print("=== BURNING SAFARI STEPS UNTIL WARP ===")
    
    # We are at (27, 8). Let's step Left to 26, 8 and Right to 27, 8.
    # We will do this in a loop. After each pair of steps, we'll check coordinates.
    # If coordinates are not around x=26/27, y=8, we have probably warped!
    
    steps_taken = 0
    while True:
        # Step Left
        mgba.press_buttons(["Left"])
        time.sleep(0.1)
        
        # Step Right
        mgba.press_buttons(["Right"])
        time.sleep(0.1)
        
        steps_taken += 2
        
        # Every 10 steps, check position and print status
        if steps_taken % 10 == 0:
            pos = mgba.get_coordinates()
            print(f"Steps taken: {steps_taken}, Current pos: {pos}")
            
            # If we warp, pos will change drastically.
            # Normal coords: x in {25,26,27,28}, y in {7,8,9}
            if not (24 <= pos['x'] <= 29 and 7 <= pos['y'] <= 9):
                print("Warp detected! Exiting loop.")
                break
                
            if steps_taken >= 300:
                print("Safety limit of 300 steps reached.")
                break

if __name__ == "__main__":
    burn_until_warp()
