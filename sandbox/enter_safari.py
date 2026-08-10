import time
import bridge

print("Starting robust enter_safari.py")

for i in range(20):
    coords = bridge.get_coordinates()
    print(f"Check {i+1}: current coordinates are {coords}")
    if coords != (4, 2) and coords is not None:
        print("Success! Coordinates changed, we are in the Safari Zone!")
        break
    print("Pressing A...")
    bridge.press_buttons(["A"])
    time.sleep(0.4)

coords = bridge.get_coordinates()
print(f"Final Coordinates: {coords}")
