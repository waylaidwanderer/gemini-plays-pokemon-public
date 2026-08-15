import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    print("Starting dynamic buy ticket sequence...")
    
    start_pos = get_pos()
    print(f"Starting position: {start_pos}")
    if start_pos != (3, 4):
        print("Not standing at (3, 4) in the Gatehouse. Aborting.")
        return
        
    presses = 0
    while presses < 25:
        presses += 1
        print(f"Press {presses}: Pressing A...")
        bridge.press_buttons(["A", "sleep 600"])
        time.sleep(1.2) # Very safe delay for text box and transition
        
        pos = get_pos()
        print(f"Current position: {pos}")
        if pos is not None and pos != (3, 4):
            print(f"SUCCESS! Position changed to {pos}. Warp occurred!")
            return
            
    print("Reached 25 presses without position change.")

if __name__ == "__main__":
    main()
