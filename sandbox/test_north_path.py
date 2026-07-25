import mgba
import time

def test_path(steps):
    path_taken = []
    # Get initial coordinates
    pos = mgba.get_coordinates()
    path_taken.append(pos)
    
    for step in steps:
        mgba.press_buttons([step])
        # wait a tiny bit for the movement to register
        time.sleep(0.3)
        pos = mgba.get_coordinates()
        path_taken.append(pos)
        
    print(f"Path taken: {path_taken}")

# We are at (17, 16).
# First, let's walk:
# - Down (to 17, 17)
# - Down (to 17, 18)
# - Right (to 18, 18)
# - Right (to 19, 18)
# - Right (to 20, 18)
# - Right (to 21, 18)
# - Right (to 22, 18)
# - Up (to 22, 17)
# - Up (to 22, 16)
# - Up (to 22, 15)
steps = ["Down", "Down", "Right", "Right", "Right", "Right", "Right", "Up", "Up", "Up"]
test_path(steps)
