import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def enter_safari_zone():
    print("=== PROCESSING TIME'S UP AND RE-ENTERING SAFARI ZONE ===")
    
    # 1. Dismiss "Ding-dong!" and "Your SAFARI GAME is over!" and warp to Gatehouse (4, 3)
    print("Dismissing PA announcement...")
    bridge.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "A", "sleep 2500"])
    
    pos = bridge.get_coordinates()
    print(f"Current coordinates after warp: {pos}")
    
    # Verify we are in the Gatehouse at (4, 3)
    if pos is None or pos != (4, 3):
        # Maybe we need one more press or wait?
        print("Warning: Not at (4, 3). Retrying dialogue dismiss...")
        bridge.press_buttons(["A", "sleep 1500"])
        pos = bridge.get_coordinates()
        print(f"New coordinates: {pos}")
        
    # 2. Talk to Clerk at (4, 2)
    print("Talking to the Gatekeeper clerk...")
    bridge.press_buttons(["A", "sleep 1200"]) # Talk
    
    # 3. Clerk says: "Would you like to join?" -> press A to select YES
    print("Selecting YES to join the Safari Game...")
    bridge.press_buttons(["A", "sleep 1200"]) # Select YES
    
    # 4. Clerk says "That'll be ¥500...", gives 30 SAFARI BALLS, says "OK! Please go on out!"
    print("Advancing dialogue to receive Safari Balls and enter...")
    bridge.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "A", "sleep 3000"])
    
    # Verify we are inside Safari Zone Center at (15, 25)
    final_pos = bridge.get_coordinates()
    print(f"Final coordinates (inside Safari Zone Center): {final_pos}")
    if final_pos == (15, 25):
        print("SUCCESS! Successfully re-entered the Safari Zone at (15, 25)!")
        return True
    else:
        print("Failed to re-enter Safari Zone automatically. Please check screen.")
        return False

if __name__ == "__main__":
    enter_safari_zone()
