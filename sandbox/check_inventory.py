import time
import bridge

print("Opening item menu to check for Gold Teeth...")

# Press Start to open menu
bridge.press_buttons(["Start"])
time.sleep(0.5)

# Press Down 2 times, then A to open ITEM
bridge.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "A"])
time.sleep(1.0)

print("Menu opened. Checking screen next turn.")
