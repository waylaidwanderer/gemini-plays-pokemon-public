import mgba
import time

def step(direction):
    print(f"Stepping {direction}...")
    mgba.press_buttons([direction, "sleep 350"])
    pos = mgba.get_coordinates()
    print(f"Post-step coords: {pos}")

def main():
    print("Testing rows 17-20 on Platform 1...")
    # Currently at (25, 15)
    
    path = [
        "Down", "Down",  # (25, 17)
        "Left",          # (24, 17)
        "Right", "Right", "Right",  # (25, 17), (26, 17), (27, 17)
        "Down",          # (27, 18)
        "Left", "Left", "Left",    # (26, 18), (25, 18), (24, 18)
        "Down",          # (24, 19)
        "Right", "Right", "Right",  # (25, 19), (26, 19), (27, 19)
        "Down",          # (27, 20)
        "Left", "Left", "Left"      # (26, 20), (25, 20), (24, 20)
    ]
    
    for i, move in enumerate(path):
        print(f"Step {i+1}:")
        step(move)
        
    final_img = mgba.take_screenshot()
    print(f"Final Screenshot: {final_img}")

if __name__ == "__main__":
    main()
