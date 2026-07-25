import mgba
import time

def step(direction):
    print(f"Stepping {direction}...")
    mgba.press_buttons([direction, "sleep 350"])
    pos = mgba.get_coordinates()
    print(f"Post-step coords: {pos}")
    # We won't use take_screenshot on every step to avoid spam, but we will print coordinates

def main():
    print("Systematic snake exploration of B1F Platform 1...")
    # Currently at (25, 15)
    
    path = [
        "Left",   # (24, 15)
        "Up",     # (24, 14)
        "Right",  # (25, 14)
        "Right",  # (26, 14)
        "Right",  # (27, 14)
        "Down",   # (27, 15)
        "Left",   # (26, 15)
        "Down",   # (26, 16)
        "Right",  # (27, 16)
        "Left",   # (26, 16)
        "Left",   # (25, 16)
        "Left"    # (24, 16)
    ]
    
    for i, move in enumerate(path):
        print(f"Step {i+1}:")
        step(move)
        
    final_img = mgba.take_screenshot()
    print(f"Final Screenshot: {final_img}")

if __name__ == "__main__":
    main()
