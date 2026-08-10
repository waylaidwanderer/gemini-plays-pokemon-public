import time
import mgba

print("Burning all remaining Safari steps to get expelled...")

# Loop 350 times to press Up/Down to burn steps
for i in range(350):
    direction = "Up" if i % 2 == 0 else "Down"
    mgba.press_buttons([direction, "sleep 100"])

print("Successfully sent 350 steps. Waiting for expulsion warp...")
time.sleep(2.0)
coords = mgba.get_coordinates()
print(f"Coordinates after expulsion: {coords}")
