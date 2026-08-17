import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def press_and_wait(btn):
    mgba.press_buttons([btn])
    time.sleep(0.35)
    return get_pos()

# We start on 1F at (1, 2)
curr = get_pos()
print(f"Starting walk to Route 8 on Row 2 from {curr}...")

# Walk Right up to 20 steps
for i in range(20):
    pos = press_and_wait("Right")
    if pos == curr:
        print(f"Blocked Right at {curr}")
        # If we are blocked, let's see if we can go Down and then Right
        break
    
    # Check for warp (drastic coordinate change)
    if abs(pos[0] - curr[0]) > 1 or abs(pos[1] - curr[1]) > 1:
        print(f"WARPED! New position: {pos}")
        break
        
    curr = pos

print("Walk complete. Final position:", get_pos())
