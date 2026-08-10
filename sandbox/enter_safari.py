import time
import bridge

print("Starting enter_safari.py")

# Let's press A multiple times with delay to clear all dialogue screens
for i in range(8):
    print(f"Pressing A ({i+1}/8)...")
    bridge.press_buttons(["A"])
    time.sleep(0.5)

time.sleep(1.0) # Wait for potential map load transition
coords = bridge.get_coordinates()
print(f"Current Coordinates after dialogue: {coords}")
