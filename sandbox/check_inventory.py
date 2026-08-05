import mgba
import time

# Scroll down to see items 5-8
mgba.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200"])
sc1 = mgba.take_screenshot()
print(f"Screenshot 1 taken and saved to {sc1}")

# Scroll down to see items 9-12
mgba.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200"])
sc2 = mgba.take_screenshot()
print(f"Screenshot 2 taken and saved to {sc2}")

# Scroll down to see items 13-16
mgba.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200"])
sc3 = mgba.take_screenshot()
print(f"Screenshot 3 taken and saved to {sc3}")

# Scroll down to see items 17-20
mgba.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200"])
sc4 = mgba.take_screenshot()
print(f"Screenshot 4 taken and saved to {sc4}")
