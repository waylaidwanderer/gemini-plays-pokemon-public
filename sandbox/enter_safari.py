import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def enter_safari_game():
    print("=== ENTERING SAFARI ZONE GAME ===")
    # We need 5 presses of A with sleep delay
    for i in range(5):
        print(f"Pressing A ({i+1}/5)...")
        bridge.press_buttons(["A", "sleep 1200"])
        
    # Get coordinates after warp
    pos = bridge.get_coordinates()
    print("Warped! New position:", pos)

if __name__ == "__main__":
    enter_safari_game()
