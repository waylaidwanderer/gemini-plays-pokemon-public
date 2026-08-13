# Script to talk to the Safari clerk in the Gatehouse, pay 500 yen, and enter the Safari Zone.
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 250"])
    return get_pos()

def talk_and_confirm():
    print("Attempting to talk to clerk...")
    bridge.press_buttons(["A", "sleep 800"])
    
    # Check if a text box is open (usually we can check by pressing B, but let's just send A's to see if dialogue advances)
    # The dialogue takes several boxes. Let's press A 6 times to clear all dialogue and enter!
    print("Pressing A to accept and enter Safari Zone...")
    for i in range(6):
        bridge.press_buttons(["A", "sleep 1200"])
        
    time.sleep(1.0)
    pos = get_pos()
    print(f"Position after dialogue: {pos}")
    if pos == (15, 25):
         print("SUCCESS! Entered Safari Zone!")
         return True
    return False

def main():
    print("=== INTERACTING WITH SAFARI GATEKEEPER ===")
    pos = get_pos()
    print(f"Starting at {pos}")
    if pos is None:
        return
        
    # We are at (3, 5).
    # Try 1: Walk to (2, 5) facing LEFT
    print("Option 1: Standing at (2, 5) facing LEFT...")
    walk_step("Left")
    if talk_and_confirm():
        return
        
    # If option 1 failed, let's face UP at (2, 5)
    print("Option 2: Standing at (2, 5) facing UP...")
    walk_step("Up")
    if talk_and_confirm():
        return
        
    # If option 2 failed, let's stand at (3, 5) facing UP
    print("Option 3: Standing at (3, 5) facing UP...")
    walk_step("Right") # back to (3, 5)
    walk_step("Up")    # face Up
    if talk_and_confirm():
        return
        
    print("All interaction options failed. Please check the screen.")

if __name__ == "__main__":
    main()
