import time
import bridge

print("Starting test_realign.py")

# Walk Left to (27, 9)
print("Moving Left to (27, 9)...")
bridge.press_buttons(["Left"])
time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")
