import time
import bridge

print("Starting robust step burning...")

# We will alternate UP and DOWN with a 400ms delay to ensure every step registers
# We will do this in a loop up to 90 steps per script execution to avoid the 100 button limit.
buttons = []
for i in range(45): # 45 pairs = 90 buttons
    buttons.append("Up")
    buttons.append("sleep 400")
    buttons.append("Down")
    buttons.append("sleep 400")

print("Sending 90 paced step buttons to mGBA...")
bridge.press_buttons(buttons)
time.sleep(1.0)

coords = bridge.get_coordinates()
print(f"Coords after paced burn: {coords}")
