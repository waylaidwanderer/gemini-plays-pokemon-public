import mgba
import time

def step_one(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    if pos_before == pos_after:
        return False
    return True

def main():
    print(f"Current position: {mgba.get_coordinates()}")
    # Let's try to go to (12, 5)
    print("Trying to go Right to (12, 5)...")
    step_one("Right")
    step_one("Right")
    print(f"Current position: {mgba.get_coordinates()}")
    
    # Try to go Down Column 12 as far as possible
    print("Trying to go Down Column 12...")
    for _ in range(10):
        if not step_one("Down"):
            print("Blocked moving Down.")
            break
    print(f"Current position: {mgba.get_coordinates()}")
    
    # Try to go Left as far as possible
    print("Trying to go Left...")
    for _ in range(15):
        if not step_one("Left"):
            print("Blocked moving Left.")
            break
    print(f"Current position: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
