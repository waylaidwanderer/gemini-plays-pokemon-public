import time
import bridge

def main():
    print("Fleeing from battle...")
    # Dismiss "Wild NIDORINA appeared!" with A/B
    bridge.press_buttons(["A", "sleep 1000"])
    bridge.press_buttons(["B", "sleep 500"])
    
    # Now in battle menu. Press Down, Right, A to RUN
    print("Selecting RUN...")
    bridge.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    
    # Check post-flee text or if we are back in overworld
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 300"])
        
    pos = bridge.get_coordinates()
    print(f"Coordinates after fleeing: {pos}")

if __name__ == "__main__":
    main()
