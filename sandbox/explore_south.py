import mgba
import time

def travel_to_route5_perfect():
    print("Starting perfect travel to Route 5...")
    
    # We are currently at (20, 23)
    # 1. Walk Up 5 steps to row 18
    # 2. Walk Left 18 steps to column 2
    # 3. Walk Down 12 steps to row 30
    # 4. Walk Right 18 steps to column 20
    # 5. Walk Down 5 steps to enter Route 5
    path = ["Up"] * 5 + ["Left"] * 18 + ["Down"] * 12 + ["Right"] * 18 + ["Down"] * 5
    
    print(f"Total steps to execute: {len(path)}")
    
    for idx, btn in enumerate(path):
        mgba.press_buttons([btn])
        time.sleep(0.40) # 400ms sleep is extremely safe and registers 100% of steps!
        if (idx + 1) % 5 == 0 or idx == len(path) - 1:
            print(f"Step {idx + 1}/{len(path)} executed: {btn}")
            
    screenshot_file = mgba.take_screenshot()
    print("Screenshot taken:", screenshot_file)

if __name__ == "__main__":
    travel_to_route5_perfect()
