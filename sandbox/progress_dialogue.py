import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def progress_dialogue():
    print("=== PROGRESSING DIALOGUE IN SECRET HOUSE ===")
    for i in range(12):
        print(f"Pressing A (step {i})...")
        bridge.press_buttons(["A", "sleep 1200"])
        
if __name__ == "__main__":
    progress_dialogue()
