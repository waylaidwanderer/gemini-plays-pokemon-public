import mgba
import time

def walk_step(direction):
    pos = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    print(f"Pressed {direction}: {pos} -> {new_pos}")
    return new_pos

def explore():
    print("Starting exploration...")
    # Dismiss any text
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # Try to walk Right
    walk_step("Right")
    # Let's walk Up to row 3
    for _ in range(9):
        walk_step("Up")
        
    # Let's try to walk Right horizontally
    for _ in range(10):
        walk_step("Right")
        
    mgba.take_screenshot()

if __name__ == "__main__":
    explore()
