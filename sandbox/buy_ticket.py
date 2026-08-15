import time
import mgba

def main():
    print("Starting slow NO diagnostic sequence...")
    
    # Clear any open dialogue first
    print("Clearing dialogue with B...")
    mgba.press_buttons(["B", "sleep 600", "B", "sleep 600", "B", "sleep 600"])
    time.sleep(2.5)
    
    # Talk to clerk
    print("Talking to clerk...")
    mgba.press_buttons(["Left", "sleep 300", "A", "sleep 1200"])
    time.sleep(2.0)
    
    # We should be at YES/NO prompt. Select NO.
    print("Selecting NO...")
    mgba.press_buttons(["Down", "sleep 600", "A", "sleep 1200"])
    time.sleep(2.0)
    
    # Take screenshot 1
    s1 = mgba.take_screenshot()
    print(f"Screenshot 1 (after selecting NO) saved to: {s1}")
    
    # Press A once
    print("Pressing A (1)...")
    mgba.press_buttons(["A", "sleep 1000"])
    time.sleep(1.5)
    s2 = mgba.take_screenshot()
    print(f"Screenshot 2 saved to: {s2}")
    
    # Press A twice
    print("Pressing A (2)...")
    mgba.press_buttons(["A", "sleep 1000"])
    time.sleep(1.5)
    s3 = mgba.take_screenshot()
    print(f"Screenshot 3 saved to: {s3}")
    
    # Press A thrice
    print("Pressing A (3)...")
    mgba.press_buttons(["A", "sleep 1000"])
    time.sleep(1.5)
    s4 = mgba.take_screenshot()
    print(f"Screenshot 4 saved to: {s4}")
    
    # Press A four times
    print("Pressing A (4)...")
    mgba.press_buttons(["A", "sleep 1000"])
    time.sleep(2.5)
    s5 = mgba.take_screenshot()
    print(f"Screenshot 5 saved to: {s5}")

if __name__ == "__main__":
    main()
