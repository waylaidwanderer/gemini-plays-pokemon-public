import time
import bridge

print("Starting test_realign.py")

# Walk Right to (27, 6)
print("Moving Right to (27, 6)...")
bridge.press_buttons(["Right"])
time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")
