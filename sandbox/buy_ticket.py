import time
import mgba

def get_pos():
    pos = mgba.get_coordinates()
    if pos is None:
        return None
    return pos["x"], pos[y] # Wait, get_coordinates returns {'x': int, 'y': int}

def main():
    print("Starting visual diagnostic buy ticket sequence...")
    
    # We are already at (3, 4) in the overworld facing Left
    print("Talking to clerk...")
    mgba.press_buttons(["Left", "sleep 300", "A", "sleep 1200"])
    time.sleep(2.0)
    
    # Take screenshot of the initial YES/NO prompt
    initial_scr = mgba.take_screenshot()
    print(f"Initial prompt screenshot saved to: {initial_scr}")
    
    # We want to select YES (A), then press A and capture a screenshot at each step to see exactly what is drawn!
    for step in range(1, 16):
        print(f"\n--- STEP {step} ---")
        mgba.press_buttons(["A", "sleep 800"])
        time.sleep(1.2)
        
        scr = mgba.take_screenshot()
        pos = mgba.get_coordinates()
        print(f"Step {step}: Player at {pos}, screenshot: {scr}")
        
if __name__ == "__main__":
    main()
