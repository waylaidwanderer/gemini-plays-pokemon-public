import time
import bridge

print("Scrolling down further to find Gold Teeth...")

# Press Down 4 times to scroll past TM06
bridge.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200"])
time.sleep(0.5)

print("Scrolled down further. Checking screen next turn.")
