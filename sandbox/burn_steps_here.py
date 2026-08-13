import mgba
import time

def burn_until_warp():
    print("=== BURNING SAFARI STEPS UNTIL WARP ===")
    
    steps_taken = 0
    while True:
        # Step Right
        mgba.press_buttons(["Right"])
        time.sleep(0.15)
        
        # Step Left
        mgba.press_buttons(["Left"])
        time.sleep(0.15)
        
        steps_taken += 2
        
        # Every 10 steps, check position and print status
        if steps_taken % 10 == 0:
            pos = mgba.get_coordinates()
            print(f"Steps taken: {steps_taken}, Current pos: {pos}")
            
            # If we warp, pos will change drastically.
            # Normal coords: x in [2, 3], y == 14
            if not (pos['x'] in [2, 3] and pos['y'] == 14):
                print("Warp detected! Exiting loop.")
                break
                
            if steps_taken >= 600:
                print("Safety limit of 600 steps reached.")
                break

if __name__ == "__main__":
    burn_until_warp()
