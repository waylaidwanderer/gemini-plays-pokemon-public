import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos[0], pos[1]
        time.sleep(0.1)
    return None

def burn_all_remaining_steps():
    print("=== STARTING ROBUST STEP BURNING ===")
    
    while True:
        pos = get_pos()
        print("Current position checked:", pos)
        
        if pos is None:
            # We are likely in a dialogue box (like "Ding-dong! Time's up!")
            print("Dialogue detected. Dismissing with B...")
            bridge.press_buttons(["B", "sleep 300"])
            time.sleep(0.5)
            continue
            
        # Check if we are out of our step-burning area
        if abs(pos[0] - 19) > 5 or abs(pos[1] - 24) > 5:
            print(f"Position shifted to {pos}. Warp detected!")
            break
            
        # Send a batch of Left/Right steps (48 steps = 96 buttons)
        print("Sending batch of 48 steps to burn steps...")
        batch = []
        for _ in range(24):
            batch.extend(["Left", "Right"])
            
        bridge.press_buttons(batch)
        # Sleep for step execution: 48 steps takes about 48 * 0.15s = ~7.2 seconds of emulator time
        # Let's sleep for 8 seconds to allow the batch to complete fully
        time.sleep(8.0)

    print("=== STEP BURNING COMPLETED SUCCESSFULLY! ===")

if __name__ == "__main__":
    burn_all_remaining_steps()
