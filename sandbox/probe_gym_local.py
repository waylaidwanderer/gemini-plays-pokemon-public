import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

print("Starting local probe from current position:", get_pos())

# Walk Down Column 1: (1, 10) -> (1, 11) -> (1, 12) -> (1, 13) -> (1, 14)
for y in range(11, 15):
    mgba.press_buttons(["Down"])
    time.sleep(0.55)
    print(f"Stepped Down, current position: {get_pos()}")
    
# Try to go Right to (2, 14)
mgba.press_buttons(["Right"])
time.sleep(0.55)
print(f"Stepped Right, current position: {get_pos()}")

# Try to go Right to (3, 14)
mgba.press_buttons(["Right"])
time.sleep(0.55)
print(f"Stepped Right, current position: {get_pos()}")
