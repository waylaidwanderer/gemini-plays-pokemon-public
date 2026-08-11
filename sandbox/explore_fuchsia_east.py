import time
import sys
import mgba

# Set stdout to use utf-8
sys.stdout.reconfigure(encoding='utf-8')

def walk_step(direction):
    mgba.press_buttons([direction, "sleep 350"])

def get_pos():
    pos = mgba.get_coordinates()
    if pos is None:
        return None
    return pos['x'], pos['y']

def main():
    print(f"Starting exploration from: {get_pos()}")
    
    # Let's walk right as far as possible along Row 32
    # We are at (9, 32)
    for i in range(25):
        curr = get_pos()
        if curr is None:
            time.sleep(0.5)
            continue
        print(f"Step {i}: At {curr}, walking Right...")
        walk_step("Right")
        next_pos = get_pos()
        if next_pos == curr:
            print("Bumped! Cannot go Right further.")
            break
            
    print(f"Stopped at: {get_pos()}")
    
    # Let's see if we can walk UP from here
    curr = get_pos()
    if curr is not None:
        print(f"Testing UP from {curr}...")
        walk_step("Up")
        after_up = get_pos()
        if after_up != curr:
            print(f"Successfully walked UP to {after_up}!")
        else:
            print("UP is blocked.")

if __name__ == "__main__":
    main()
