import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def press_and_wait(btn):
    mgba.press_buttons([btn])
    time.sleep(0.3)
    return get_pos()

start = get_pos()
print(f"Starting walk to Route 8 from {start}...")

# Walk right until we warp or hit a wall (max 20 steps)
curr = start
for i in range(20):
    pos = press_and_wait("Right")
    if pos == curr:
        print(f"Blocked or hit wall at {curr}")
        break
    
    # Check for drastic coordinate change indicative of warp
    if abs(pos[0] - curr[0]) > 1 or abs(pos[1] - curr[1]) > 1:
        print(f"WARPED! New position: {pos}")
        break
        
    curr = pos

print("Walk complete. Final position:", get_pos())
