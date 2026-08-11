import time
import bridge

print("Burning remaining steps with safe bridge library...")

# Alternate Up and Down to burn steps quickly
for i in range(50):
    direction = "Up" if i % 2 == 0 else "Down"
    bridge.press_buttons([direction, "sleep 100"])

print("Completed 50 steps. Checking coordinates...")
time.sleep(1.0)
coords = bridge.get_coordinates()
print(f"Coordinates: {coords}")
