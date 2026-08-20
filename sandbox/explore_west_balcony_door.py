import mgba
import time

def main():
    print("Continuing exploration down Column 2...")
    pos = mgba.get_coordinates()
    print("Starting at:", pos)
    
    # Walk DOWN until blocked
    curr_y = pos['y']
    for i in range(15):
        curr_y += 1
        pos_before = mgba.get_coordinates()
        print(f"Step {i+1}: Trying Down to row {curr_y}...")
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
        pos_after = mgba.get_coordinates()
        print("Position after Down:", pos_after)
        
        if pos_after == pos_before:
            print("Blocked! Taking screenshot...")
            mgba.take_screenshot()
            break
            
        if pos_after['y'] < 5: # Map transition
            print("Map Transition Detected! Landed at:", pos_after)
            mgba.take_screenshot()
            return

if __name__ == "__main__":
    main()
