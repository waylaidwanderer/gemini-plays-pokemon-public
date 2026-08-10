import time
import bridge

print("Burning 90 steps to run down the Safari step budget...")

buttons = []
for i in range(90):
    direction = "Up" if i % 2 == 0 else "Down"
    buttons.append(direction)
    # Adding a sleep to pace the taps
    buttons.append("sleep 50")

# Press the buttons
bridge.press_buttons(buttons)
time.sleep(1.0)

coords = bridge.get_coordinates()
print(f"Current Coordinates: {coords}")
