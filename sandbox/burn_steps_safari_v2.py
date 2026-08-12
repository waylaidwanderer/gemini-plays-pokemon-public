import bridge
import time

def burn_96_steps():
    print("=== BURNING 96 SAFARI STEPS SAFELY ===")
    
    # We will press exactly 96 buttons (48 steps Left/Right).
    # Since 96 < 100, this will stay safely within the emulator harness button limit.
    batch = []
    for _ in range(24):
        batch.extend(["Left", "Right"])
        
    print("Sending batch of 48 steps (96 buttons)...")
    res = bridge.press_buttons(batch)
    print(f"Harness response: {res}")
    
    pos = bridge.get_coordinates()
    print(f"Current position: {pos}")

if __name__ == "__main__":
    burn_96_steps()
