import time
import bridge

print("Scrolling down item menu to see more items...")

# Scroll down to see more items (from current position at the first item)
bridge.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200"])
time.sleep(0.5)

print("Scrolled down. Checking screen next turn.")
